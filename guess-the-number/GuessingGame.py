from random import randint

logo = """     
   _____                        _   _                                   _               
  / ____|                      | | | |                                 | |              
 | |  __ _   _  ___  ___ ___   | |_| |__   ___    _ __  _   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|  | __| '_ \ / _ \  | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \  | |_| | | |  __/  | | | | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/   \__|_| |_|\___|  |_| |_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                        
                                                                                        
"""

# A function to set the difficulty of the game
def set_difficulty(level):
    if level.lower() == "easy":
        return 15
    elif level.lower() == "medium":
    	return 10
    else:
        return 5

def game():
    print(logo)
    print("""Welcome to the Number Guessing Game!
I have a number between 1 and 100 in my mind, try to guess it!
====================""")
    answer = randint(1,100)#Choosing a random number
    turns = set_difficulty(input("Choose a difficulty. Type 'easy','medium' or 'hard': "))
    # Repeat the guessing functionality if they get it wrong.
    while True:
        #letting the user make a guess
        print(f"You have {turns} attempts remaining to guess the number.\n====================")
        guess = int(input("Make a guess: "))
        #Game logic
        if turns == 0:#Out Of Turns
            print("You've run out of guesses, you lose.")
            break
        elif guess != answer:#Turns left but guess is wrong
            if guess > answer:
            	print("Too high!")
            elif guess < answer:
            	print("Too low!")
            print("Guess again.\n====================")
            turns -=1
        else:#guess is correct
        	print(f"You got it! The answer was {answer}.")
        	break

game()