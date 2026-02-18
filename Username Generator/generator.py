import random

def main():
    d = {'i':'1', 'e':'3', 's':'5', 'o':'0'}
    first = input("Please tell me your first name: ").lower()
    last = input("Please tell me your last name: ").lower()[:4]

    for i in d:
        first = first.replace(i, d[i])
        last = last.replace(i, d[i])

    final_name = first + "_" + last + str(random.randint(100, 1000))
    
    print("Generated username for you:\n\n" + final_name + "\n")


if __name__ == '__main__':
    main()
