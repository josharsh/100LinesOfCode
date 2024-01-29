import random


def roller():
    num = random.randint(1, 6)

    if num == 1:
        print("[-  -  -]")
        print("[-  X  -]")
        print("[-  -  -]")
    elif num == 2:
        print("[-  X  -]")
        print("[-  -  -]")
        print("[-  X  -]")
    elif num == 3:
        print("[X  -  -]")
        print("[-  X  -]")
        print("[-  -  X]")
    elif num == 4:
        print("[X  -  X]")
        print("[-  -  -]")
        print("[X  -  X]")
    elif num == 5:
        print("[X  -  X]")
        print("[-  X  -]")
        print("[X  -  X]")
    elif num == 6:
        print("[X  -  X]")
        print("[X  -  X]")
        print("[X  -  X]")
    print("---------")
    print("You rolled a",  num, "!")
    print("---------")

roller()

inp = input("Type y if you want to roll again and n if you don't: ")

while inp == "y" or inp == "Y":
    roller()
    inp = input("Type y if you want to repeat and n if you don't: ")
