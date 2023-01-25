import random
import time
import copy

grid = [ [ '_' for _ in range(20) ] for _ in range(20) ]  # 20x20 placeholder grid
orientations = ["horizontal", "vertical", "diagonal_up", "diagonal_down"]

all_words = open('words_alpha.txt', 'r').readlines()
word_list = []
while len(word_list) < 20:  # Choose random word and check if below length limit
    picked_word = random.choice(all_words)
    if len(picked_word) <= 20:
        word_list.append(picked_word.strip().upper())

for word in word_list:
    timeout = time.time()+10  # Store timeout to end program when taking too long
    is_placed = False

    while not is_placed:
        if time.time() > timeout:  # Check if loop is taking too long to avoid program running indefinitely
            raise Exception("Program took too long to generate grid. Please try again.")

        orientation = random.choice(orientations)
        is_reversed = True if random.random() > 0.5 else False

        if orientation == "horizontal":
            step_x = 1
            step_y = 0
        if orientation == "vertical":
            step_x = 0
            step_y = 1
        if orientation == "diagonal_up":
            step_x = 1
            step_y = -1
        if orientation == "diagonal_down":
            step_x = 1
            step_y = 1
        if is_reversed:
            step_x *= -1
            step_y *= -1

        start_x = random.randrange(20)
        start_y = random.randrange(20)
        end_x = start_x + len(word)*step_x
        end_y = start_y + len(word)*step_y

        # Check if word is outside of grid; if outside, try new orientation
        if end_x < 0 or end_x > 20: continue
        if end_y < 0 or end_y > 20: continue

        can_fit = True  # Check if letters don't overlap other letters
        for i in range(len(word)):
            letter = word[i]

            position_x = start_x + i*step_x
            position_y = start_y + i*step_y

            letter_at_position = grid[position_x][position_y]

            if letter_at_position == '_' or letter_at_position == letter:
                continue  # Check next letter
            else:
                can_fit = False
                break  # Cannot place word

        if not can_fit: continue  # Restart and choose another orientation
        else:  # Word can be placed, actually place word on grid
            for i in range(len(word)):
                letter = word[i]
                position_x = start_x + i*step_x
                position_y = start_y + i*step_y
                grid[position_x][position_y] = letter

        is_placed = True  # Current word done. Go for next word

revealed_grid = copy.deepcopy(grid)  # Save unfilled grid for answer reveal

for x in range(20):  # Fill grid blanks with random letters
    for y in range(20):
        if grid[x][y] == '_':
            grid[x][y] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

for row in grid:
    print(' '.join(row))

print("\nYour words are:")
for word in word_list:
    print(word)

input("\nPress ENTER to reveal answers \n")
for row in revealed_grid:
    print(' '.join(row))
print("\n")