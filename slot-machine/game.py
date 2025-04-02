import random
import time
import os

class SlotMachine:
    def __init__(self):
        self.symbols = ["🍒", "🍋", "🍊", "🍇", "🔔", "💎", "7️⃣", "🍀"]
        self.payouts = {
            "🍒🍒🍒": 5,
            "🍋🍋🍋": 10,
            "🍊🍊🍊": 15,
            "🍇🍇🍇": 20,
            "🔔🔔🔔": 25,
            "💎💎💎": 50,
            "7️⃣7️⃣7️⃣": 100,
            "🍀🍀🍀": 200
        }
        self.balance = 100
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def display_intro(self):
        self.clear_screen()
        print("\n" + "="*50)
        print("🎰 PYTHON SLOT MACHINE 🎰".center(50))
        print("="*50)
        print("\nWelcome to the Python Slot Machine!")
        print(f"Current balance: ${self.balance}")
        print("\nPAYOUT TABLE:")
        for symbols, payout in self.payouts.items():
            print(f"{symbols}: ${payout}")
        print("="*50)
        
    def get_bet(self):
        while True:
            try:
                bet = int(input("\nEnter your bet (0 to quit): $"))
                if bet == 0:
                    return 0
                if bet > self.balance:
                    print("You don't have enough money!")
                    continue
                if bet <= 0:
                    print("Bet must be positive!")
                    continue
                return bet
            except ValueError:
                print("Please enter a valid number.")
                
    def spin_reels(self):
        print("\nSpinning the reels...")
        time.sleep(0.5)
        print("🎰 Spinning... 🎰")
        time.sleep(1)
        reels = []
        for _ in range(3):
            reels.append(random.choice(self.symbols))
            
        return reels
        
    def check_win(self, reels, bet):
        result = "".join(reels)
        print(f"\n[ {reels[0]} | {reels[1]} | {reels[2]} ]")
        
        if reels[0] == reels[1] == reels[2]:
            multiplier = self.payouts[result]
            winnings = bet * multiplier
            self.balance += winnings
            print(f"🎉 YOU WON ${winnings}! 🎉")
            return winnings
        else:
            self.balance -= bet
            print("Better luck next time!")
            return -bet
            
    def run(self):
        while True:
            self.display_intro()
            bet = self.get_bet()
            if bet == 0:
                print("\nThanks for playing!")
                print(f"Final balance: ${self.balance}")
                break
            reels = self.spin_reels()
            self.check_win(reels, bet)
            if self.balance <= 0:
                print("\nYou're out of money!")
                print("Game over!")
                break
            play_again = input("\nPress Enter to play again or 'q' to quit: ")
            if play_again.lower() == 'q':
                print("\nThanks for playing!")
                print(f"Final balance: ${self.balance}")
                break
if __name__ == "__main__":
    game = SlotMachine()
    game.run()