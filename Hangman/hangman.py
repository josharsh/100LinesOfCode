import random
from art import stages, logo  # Imports the ASCII art
from words import word_list

# Chooses a random word and saves its length

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
previous_guesses = []

# Prints the game's logo

print(logo)

# Creates blanks

display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:

    guess = input("Guess a letter: ").lower()

    # Lets the user know if they enter a letter that they've already guessed

    if guess in previous_guesses:
        print(f"\nYou've already guessed the letter '{guess}' before!")
        lives += 1

    else:
        previous_guesses.append(guess)

    # Checks guessed letter

    for position in range(word_length):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Checks if user is wrong.

    if guess not in chosen_word:

        print(f"\nThe letter '{guess}' is not in the word.")
        lives -= 1

        if lives == 0:
            end_of_game = True
            print("\nYou lose!")
            print(f"The word was '{chosen_word}'.")
            print(stages[lives])
            break

    # Joins all the elements in the list and turns it into a string

    print(f"{' '.join(display)}")

    # Checks if user has got all letters

    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Shows the hangman art

    print(stages[lives])
