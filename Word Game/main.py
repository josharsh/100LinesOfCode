import random
import os

level_easy = ["button", "doctor", "essay", "supper", "television", "classic", "banking"] # 6+ letters
level_medium = ["order", "books", "table", "phone", "carry", "south", "fence", "room"] # 5 letters
level_hard = ["old", "ant", "hop", "tea", "eat", "bot", "tug", "who", "how", "bee", "sip"] # 3 letters

def gameplay(score, lives, question, missing_letter):
    while True:
        if lives <= 0:
            return score, lives
        
        print(f"Current score: {score}")
        print(f"Number of lives: {lives}")
        print(f"Word: {question}")

        guess = input("What is the missing letter: ").lower()

        if guess == missing_letter:
            score += 1
            print("Correct\n")
            os.system("cls")
            return score, lives
        else:
            lives -= 1
            print("Incorrect\n")
    
def question_generator(word):
    question = ""
    random_index = random.randint(0, len(word) - 1)
    missing_letter = str(word[random_index])
    for i in range(len(word)):
        if i == random_index:
            question += "_ "
        else:
            question += f"{word[i]} "
    return question, missing_letter


def word_generator(mode):
    converter = {1: level_easy, 2: level_medium, 3: level_hard}
    return random.choice(converter[mode])

def game_loop(mode, lives, score):
    used = []
    for i in range(5):
        word = word_generator(mode)

        while word in used:
            word = word_generator(mode)
        used.append(word)
        question, missing_letter = question_generator(word)
        score, lives = gameplay(score, lives, question, missing_letter)

        if lives <= 0:
            break

    return mode, lives, score

def game():
    mode = 1
    lives = 3
    score = 0

    while lives > 0:
        mode, lives, score = game_loop(mode, lives, score)
        if lives <= 0:
            print("Out of lives, game over.")
            break
        if score % 5 == 0:
            mode += 1
            print(f"Level cleared! Score: {score}\n")
            if mode == 4:
                print("Game over! You fininshed all levels")
                break

def main():
    print("Welcome to the Word Game!")
    game()

main()