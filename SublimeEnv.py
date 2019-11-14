import sublime, sublime_plugin
from os import environ
import subprocess
import re

settings = {}
default_path = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin:/opt/X11/bin"

def debug(*args):
  global settings

  if settings.get("debug"):
    print("[SublimeEnv]", *args)

def run_command(command):
  result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
  output = result.stdout.read().decode("utf-8").rstrip()

  return output

def retrieve_path(command):
  if not command:
    return

  path = run_command(command.format(user=environ["USER"], shell=environ["SHELL"]))

  system_dirs = []
  user_dirs = []
  dirs = path.split(":")

  for dir in dirs:
    if re.match(r"^/(usr|bin|sbin|opt)", dir):
      system_dirs.append(dir)
    else:
      user_dirs.append(dir)

  path = ":".join(user_dirs + system_dirs)

  return path

def plugin_loaded():
  global settings

  settings = sublime.load_settings("SublimeEnv.sublime-settings")

  debug("Starting")
  platform = sublime.platform()
  env = settings.get("env")
  commands = settings.get("commands")

  debug("Setting environment for", platform)

  if not "PATH" in env:
    debug("PATH is not set, so infer from system")
    path = retrieve_path(commands[platform])

    if path:
      debug("Inferred PATH is", path)
      env["PATH"] = path
    else:
      debug("Couldn't infer PATH, so defaulting to", default_path)
      env["PATH"] = default_path

  for name, value in env.items():
    debug("Setting %s=%s" % (name, value))
    environ[name] = value

  debug("Finished")

class ReloadEnvCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    plugin_loaded()
