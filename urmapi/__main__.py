from sys import argv
import __init__

print(argv)

class modules:
    executed = False
    error = ""

    class options:
        def version():
            executed = True
            print(f"URM-API Version: {__init__.__version__}")
            print(f"URM-API Accepted Config Versions:\n {__init__.__accepted_versions__}")
        
        def help():
            print("Variables:")
            for vKey, vVal in variables.items():
                print(f"{vKey}\t\t{vVal[0]}")
                
            print()

            print("Options:")
            for oKey, oVal in options.items():
                print(f"{oKey}\t\t{oVal[0]}")

            print()

            print("Commands:")
            for cKey, cVal in commands.items():
                print(f"{cKey}\t\t{cVal[0]}")



    class commands:
        def install():
            if len(argv) > 1:
                if argv[1].startswith("http"):
                    api = __init__.API(server = argv[1])
                else:
                    api = __init__.API(directory = argv[1])
                
                api.install()
                executed = True

            else:
                error = "Please specify a link or config file"

        def update():
            return

variables = {
    }
options = {
    "--version": ["Show URM-API version.", modules.options.version],
    "--help": ["Show this message or module information.", modules.options.help]
    }
commands = {
    "install": ["Install a package using URM-API.", modules.commands.install],
    "update": ["Checks for updates in all packages, then updates.", modules.commands.update]
    }

if len(argv) == 1:
    modules.options.help()

else:
    argv.pop(0)
    executed = False

    for option in options:
        if argv[0] == option:
            options[option][1]()
            executed = True

    for command in commands:
        if argv[0] == command:
            commands[command][1]()
            executed = True

    if not executed:
        print(f"Command: '{argv[0]}' not found.")
        print("For help on commands, type 'urmapi --help'")