import os


def print_the_menu():
    print("**********************************")
    print("*           Python Hub           *")
    print("*         List of Modules:       *")
    print("**********************************")
    print("1. Rock-Paper-Scissors")
    print("2. Post-It Note")
    print("3. Selection Sort Visualizer")
    print("4. Password Generator")
    print("5. Morse-Code Translator")
    print("6. Morse-Code Translator w/ GUI")
    print("7. Species Status")
    print("8. CodeForces User Search")
    print("9. String Decryption/Encryption")
    print("10. Github Followers")
    print("11. Create a LAN Chat")


def main():
    user_input = ""
    while user_input != "-1" and user_input != "exit":
        print_the_menu()
        print()
        user_input = input("Enter the Module # you would like to use: ")
        if user_input == "1":
            os.chdir("..")
            os.chdir("Rock-Paper-Scissors")
            os.system('python rock-paper-scissors.py')
            continue
        if user_input == "2":
            os.chdir("..")
            os.chdir("post_it_notes")
            os.system('python notes.py')
            continue
        if user_input == "3":
            os.chdir("..")
            os.chdir("PythonAlgoVisualizer")
            os.system('python SelectionSortVisualizer.py')
            continue
        if user_input == "4":
            os.chdir("..")
            os.chdir("password_generator")
            os.system('python main.py')
            continue
        if user_input == "5":
            os.chdir("..")
            os.chdir("morse_translator")
            os.system('python morse_translator.py')
            continue
        if user_input == "6":
            os.chdir("..")
            os.chdir("Morse Code GUI")
            os.system('python morse.py')
            continue
        if user_input == "7":
            os.chdir("..")
            os.chdir("Species-Status")
            os.system('python species_status.py')
            continue
        if user_input == "8":
            os.chdir("..")
            os.chdir("Codeforces-Scraper")
            os.system('python gui.py')
            continue
        if user_input == "9":
            os.chdir("..")
            os.chdir("Encryption")
            os.system('python enc.py')
            continue
        if user_input == "10":
            os.chdir("..")
            os.chdir("Github-Follower-Bot")
            os.system('python main.py')
            continue
        if user_input == "11":
            os.chdir("..")
            os.chdir("LANComm")
            os.system('python bleh2.py')
            continue
        if user_input == "-1": {}
        if user_input == "exit": {}
        else:
            print("non-valid entry, please try again with a valid numeric input: ")
            continue


if __name__ == '__main__':
    main()
