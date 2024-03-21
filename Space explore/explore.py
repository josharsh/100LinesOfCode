import random
import time

def explore_space():
    player_name = input("Welcome, space explorer! What's your name? ")
    print(f"Hello, {player_name}! You're about to embark on a space adventure.")
    time.sleep(1)

    def make_choice():
        choice = input("\nWhat do you want to do?\n1. Explore a nearby planet\n2. Visit a distant star\n3. Quit\nEnter the number of your choice: ")
        return choice

    while True:
        choice = make_choice()

        if choice == "1":
            planet_name = random.choice(["Mars", "Venus", "Jupiter", "Saturn", "Neptune"])
            print(f"You explore the planet {planet_name}.")
            time.sleep(2)
            print("You gather interesting data and continue your journey.")
        elif choice == "2":
            star_name = random.choice(["Proxima Centauri", "Sirius", "Betelgeuse", "Alpha Centauri"])
            print(f"You visit the distant star {star_name}.")