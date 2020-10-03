import random

all_options = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air',
               'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']

game_mode = True

double_all_options = all_options * 2
all_losing_options = {}
for key in range(len(all_options)):
    all_losing_options[all_options[key]] = double_all_options[key + 1:key + 8]


player = str(input("Enter Your name: "))
print("Hello, " + player)

file = open("rating.txt", "rt")
data_read = file.readlines()
data = [plr.split(" ") for plr in data_read]
score = 0
file.close()

for plr in data:
    if plr[0] == player:
        print("Loaded Score from Last Game")
        score = int(plr[1])
        break

user_choose = str(input("Press Enter to cont. with default options or give options\n"))
if user_choose == "":
    values = ["rock", "paper", "scissors"]
else:
    values = user_choose.split(",")

active_options = {}
for key in all_losing_options:
    if key in values:
        temp = []
        for op in all_losing_options[key]:
            if op in values:
                temp.append(op)
        active_options[key] = temp

print("Okay, let's start")


def save_in_txt():
    print(player,score)
    for plr in data:
        if plr[0] == player:
            plr[1] = str(score)
            break
    else:
        data.append([str(player),str(score)])
    write_data = ["{0} {1}\n".format(x1, x2) for (x1, x2) in data]
    with open('rating.txt', 'w') as out_file:
        out_file.writelines(write_data)
    print("Data Saved")


while game_mode:
    try:
        system_choice = values[random.randrange(len(values))]
        user_choice = str(input())
        if user_choice == system_choice:
            score += 50
            print("There is a draw " + system_choice)
        elif user_choice == "!exit":
            game_mode = False
            save_in_txt()
            print("Bye!")
            break
        elif user_choice == "!rating":
            print("Your rating: ", score)
        elif system_choice in active_options[user_choice] :
            print("Sorry, but computer chose " + system_choice)
        elif user_choice in active_options[system_choice] :
            score += 100
            print("Well done. Computer chose " + system_choice + " and failed")
    except KeyError:
        print("Invalid input")

