import random
import time
import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def game_over():
    clear_screen()
    print("Game Over!")
    print("Asteroid hit your spaceship. You're lost in space.")
    print("Thanks for playing!")

def play_space_game():
    spaceship = "^"
    space = " "
    asteroid = "*"
    game_board = [space] * 20
    spaceship_position = 9
    score = 0

    print("Welcome to the Space Game!")
    print("Dodge the asteroids and survive as long as you can.")

    while True:
        clear_screen()

        # Move the spaceship
        game_board[spaceship_position] = spaceship

        # Generate random asteroids
        if random.randint(0, 10) < 2:
            asteroid_position = random.randint(0, 19)
            game_board[asteroid_position] = asteroid

        # Display the game board
        print("".join(game_board))
        print("Score:", score)

        # Check for collision with asteroid
        if game_board[spaceship_position] == asteroid:
            game_over()
            break

        # Move the spaceship back to space
        game_board[spaceship_position] = space

        # Get user input
        try:
            move = input("Press 'a' to move left, 'd' to move right, or 'q' to quit: ").lower()

            if move == 'a':
                spaceship_position -= 1
            elif move == 'd':
                spaceship_position += 1
            elif move == 'q':
                break

            # Ensure spaceship stays within bounds
            spaceship_position = max(0, min(spaceship_position, 19))

            score += 1

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    play_space_game()
