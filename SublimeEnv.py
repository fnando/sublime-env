import sublime, sublime_plugin
import os
import subprocess
import re

default_path = "/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/sbin:/opt/X11/bin"


def settings(key):
    return sublime.load_settings("SublimeEnv.sublime-settings").get(key)


def debug(*args):
    if settings("debug"):
        print("[SublimeEnv]", *args)


def run_command(command):
    result = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.read().decode("utf-8").rstrip()

    return output


def retrieve_path(command):
    if not command:
        return

    path = run_command(
        command.format(user=os.environ["USER"], shell=os.environ["SHELL"]))

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
    debug("Starting")
    platform = sublime.platform()
    env = settings("env")
    commands = settings("commands")

    debug("Setting environment for", platform)

    if "PATH" in env:
        path = env["PATH"]
    else:
        debug("PATH is not set, so infer from system")
        path = retrieve_path(commands[platform])

        if not path:
            debug("Couldn't infer PATH, so defaulting to", default_path)
            path = default_path

    env["PATH"] = ":".join(
        [os.path.expanduser(item) for item in path.split(":")])

    for name, value in env.items():
        debug("Setting %s=%s" % (name, value))
        os.environ[name] = value

    debug("Finished")


class ReloadEnvCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        plugin_loaded()
