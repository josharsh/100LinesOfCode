import random
def int_input():
	try:
		return int(input("? "))
	except ValueError:
		print("That's not a number!")
		return int_input()
number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100.")
while (guess:=int_input())!=number:
	if guess<number:
		print("Too low!")
	elif guess>number:
		print("Too high!")
print("Correct!")
