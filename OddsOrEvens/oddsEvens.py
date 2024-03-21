import random as rd

choice = input("Do you choose odds (O) or evens (E)? \n")

choice = choice.capitalize()

if choice not in ["O", "E"]:
    print ("Invalid input.")
    quit()

number = int(input("What number do you choose? 1 or 2? \n"))

if number not in [1, 2]:
    print ("Invalid input.")
    quit()

machineNbr = round(rd.random()*100)
total = machineNbr + number

if total % 2 == 0 and choice == "O" or total % 2 == 1 and choice == "E":
    print("Sorry, you lost :( better luck next time!")

else:
    print("Congratulations, you won!!! :)")