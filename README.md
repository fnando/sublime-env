# Env for Sublime Text

Set environment variables in the scope of Sublime Text. Useful when you want to run commands from Sublime Text, or set default environment variables for language compilers.

## Installation

### Setup Package Control Repository

1. Follow the instructions from https://sublime.fnando.com.
2. Open the command pallete, run “Package Control: Install Package“, then search for “Sublime Env“.

### Git Clone

Clone this repository into the Sublime Text “Packages” directory, which is located where ever the “Preferences” -> “Browse Packages” option in sublime takes you.

## Usage

You can set environment variables by editing the settings file. You can either open the command palette and search for “SublimeEnv: Settings” or use “Sublime Text -> Preferences -> Package Settings -> SublimeEnv -> Settings”. The default settings are:

```jsonc
{
  // Set environment variables from this list.
  // `PATH` has a special behaviour: if it's not set on the following
  // dictionary, then value is fetched out of the system using the `.commands`.
  "env": {},

  // The commands that will be used to fetch `PATH`.
  // They will only be called when `PATH` is not defined directly on `.env`.
  // You can use the variables `{user}` and `{shell}` like the OSX command.
  "commands": {
    "osx": "/usr/bin/login -fqpl {user} {shell} -l -c 'echo $PATH'",
    "linux": "su - {user} -c 'echo $PATH'"
  },

  // Enable debug mode.
  "debug": false
}
```

To reload the environment variables, open the command palette and search for “SublimeEnv: Reload Environment“.

## License

Copyright (c) 2019 Nando Vieira

MIT License

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
