import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game logic."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        # User input
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        # Computer selection
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display choices and result
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        if result == 'user':
            print("You win!")
            user_score += 1
        elif result == 'computer':
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        # Display scores
        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        # Play again?
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
