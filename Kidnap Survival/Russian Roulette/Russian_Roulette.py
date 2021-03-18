from time import sleep
import random



clipSize = 6
bullets = 0
playerDone = False
compDone = False
gameOver = False

print("Today we play a game. If you win you get to talk out of here and never see us again.")
print("If you lose... ")
print("We'll get there when we get there, uh if we get there.")
for x in range(3):
    sleep(1)
    print("...")




print("The rules of the game are as follows:")
print("The revolver we are using today can hold a max of 6 bullets.")
print("We will each take turns adding a bullet into the cylender.")
print("If one of us chooses not to add a bullet, their opponent my continue to add bullets uptill they are happy.")
print("If there is an even number of bullets when we decide to play you will go first.")
print("If there is an odd number of bullers I will go first.")
print("Last one alive wins.")
print("Because we want a fair game we will never add the sixth bullet.")

while (playerDone is False or compDone is False) and bullets < 6:
    print("There are currently " + str(bullets) + " bullets in the cylender")

    if bullets % 2 == 0 and playerDone != True:
         choice = input("Would you like to add a bullet? (Y/N)")
         if choice == 'y' or choice == 'Y':
            bullets = bullets + 1
         else:
            playerDone = True

    elif bullets == 0:
        print("We add a bullet")
        bullets = bullets + 1

    elif bullets %2 != 0 and compDone != True:
        rand = random.randint(1,2)
        if rand == 1:
            print("We will add a bullet")
            bullets = bullets + 1
        else:
            print("We wont add any more bullets")
            compDone = True

    elif playerDone == True:
        rand = random.randint(1,2)
        if rand == 1:
            print("We will add a bullet")
            bullets = bullets + 1
        else:
            print("We wont add any more bullets")
            compDone = True

    elif compDone == True:
          choice = input("Would you like to add a bullet? (Y/N)")
          if choice == 'y' or choice == 'Y':
            bullets = bullets + 1
          else:
            playerDone = True

print("Looks like we are done")
print("Let the game begin")

while gameOver == False:
    shot = random.randint(0,clipSize)
    if bullets % 2 == 0:
        print("You raise the revolver to your head.")
        sleep(1)
        print("Start to pull the trigger.")
        if shot > bullets:
            print("*click*")
            print("You survive")
            bullets = bullets +1
            sleep(2)
        else:
            print("BANG!")
            print("You died")
            gameOver = True
            
    else:
        if bullets % 2 != 0:
            print("Your opponent raises the revolver to their head.")
            sleep(1)
            print("Starts to pull the trigger.")
        if shot > bullets:
            print("*click*")
            print("Looks like its your turn")
            bullets = bullets +1 
            sleep(2)
        else:
            print("BANG!")
            print("Their body slumps down on the table in front of you")
            print("You walk away with your life.")
            gameOver = True
            