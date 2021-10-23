import subprocess, os
import readline
while True:
    try:
        currentDir = u"\u001b[33m" + os.getcwd() + "  " + u"\u001b[0m"
        commandToRun = input(currentDir).split(" ")

        if commandToRun[0] == "cd":

            if len(commandToRun) > 2:
                os.chdir(" ".join(commandToRun[1: len(commandToRun)])) # To The end
                continue

            os.chdir(commandToRun[1]) # to change directories
            continue
    
        exitCode = subprocess.run(commandToRun, check=True)
    
    except subprocess.CalledProcessError as e:
        for i in e:
            if  e == "\n":
                pass
            else:
                print(e)

    except FileNotFoundError:
        print("Command Not found: This may be because you have a custom command or an alias")
        print("NOTE: Custom Commands or aliases don't work here")

    except KeyboardInterrupt:
        print("")
        break

    except EOFError:
        print("")
        break

    except PermissionError:
        pass
exit()