import os
from sys import argv

print(argv)

class modules:
    class options:
        def set():
            return

        def list():
            return

        def version():
            return
        
        def help():
            return

    class commands:
        def install():
            return

        def update():
            return

        def list():
            return

variables = {
    }
options = {
    "--set": ["Set URM-API variables.", modules.options.set],
    "--list": ["List URM-API variable values.", modules.options.list],
    "--version": ["Show URM-API version.", modules.options.version],
    "--help": ["Show this message or module information.", modules.options.help]
    }
commands = {
    "install": ["Install a package using URM-API.", modules.commands.install],
    "update": ["Checks for updates in all packages, then updates.", modules.commands.update],
    "list": ["List all installed packages", modules.commands.list]
    }

if len(argv) == 1:
    modules.options.help()
    print(os.path.dirname(__file__))