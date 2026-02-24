"""A basic terminal emulator in Python.
It allows you to run commands and change directories.
The script uses the subprocess module to execute commands
and the os module to handle directory changes."""

import subprocess
import os
import sys

while True:
    try:
        currentDir = "\u001b[33m" + os.getcwd() + "  " + "\u001b[0m"
        commandToRun = input(currentDir).split(" ")

        if commandToRun[0] == "cd":

            if len(commandToRun) > 2:
                os.chdir(" ".join(commandToRun[1: len(commandToRun)])) # To The end
                continue

            os.chdir(commandToRun[1]) # to change directories
            continue

        exitCode = subprocess.run(commandToRun, check=True)

    except subprocess.CalledProcessError as e:
        # CalledProcessError is not iterable. Print useful output if available,
        # otherwise fall back to the exception representation.
        OUTPUT = getattr(e, "output", None)
        if OUTPUT:
            try:
                if isinstance(OUTPUT, bytes):
                    OUTPUT = OUTPUT.decode(errors="replace")
                for line in str(OUTPUT).splitlines():
                    if line.strip():
                        print(line)
            except Exception:
                print(e)
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
sys.exit()
