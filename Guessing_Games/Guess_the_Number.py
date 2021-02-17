import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))

def start_game():
    random_number = int(random.randint(1, 30))
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts = 0
    show_score()

    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 30 ")
            if int(guess) < 1 or int(guess) > 30:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 30))
                if play_again.lower() == "no":
                    print("Cool then!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("That is not a valid value.")
            print("({})".format(err))
    else:
        print("Cool then!")
        
if __name__ == '__main__':
    start_game()