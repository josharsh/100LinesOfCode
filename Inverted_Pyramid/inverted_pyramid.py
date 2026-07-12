height = int(input("Enter the height of the inverted pyramid: "))

while height <= 0:
    print("Please enter a positive integer for the height.")
    height = int(input("Enter the height of the inverted pyramid: "))

for i in range(height, 0, -1):
    spaces = height - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)