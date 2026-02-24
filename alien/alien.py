"""Alien Invasion Game
A simple text-based game where the player encounters aliens and battles them."""

import time

# Define the player's spaceship
class Spaceship:
    """Represents the player's spaceship with health and damage attributes."""
    def __init__(self):
        self.health = 100
        self.damage = 10

# Define the alien enemy
class Alien:
    """Represents an alien enemy with health and damage attributes."""
    def __init__(self):
        self.health = 50
        self.damage = 5

# Function to simulate a battle between the player and an alien
def battle(player, alien):
    """Simulates a battle between the player and an alien."""
    while player.health > 0 and alien.health > 0:
        # Player attacks alien
        alien.health -= player.damage
        print("You hit the alien for", player.damage, "damage.")
        time.sleep(1)

        # Check if alien is defeated
        if alien.health <= 0:
            print("You defeated the alien!")
            break

        # Alien attacks player
        player.health -= alien.damage
        print("The alien hits you for", alien.damage, "damage.")
        time.sleep(1)

        # Check if player is defeated
        if player.health <= 0:
            print("Game Over! The alien defeated you.")
            break

# Main game loop
def play_game():
    """Starts the Alien Invasion Game."""
    print("Welcome to the Alien Invasion Game!")
    player = Spaceship()
    while True:
        choice = input("Do you want to encounter an alien? (yes/no): ").lower()
        if choice == "yes":
            alien = Alien()
            print("You encounter an alien!")
            battle(player, alien)
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
