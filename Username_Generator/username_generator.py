import random
def generateUsername(name):
    names = name.split()
    firstname = names[0].lower()
    lastname = names[-1].lower()
    firstLength = random.randint(int(len(firstname)/2),len(firstname))
    lastLength = random.randint(int(len(lastname)/2),len(lastname))
    firstLetter = firstname[:firstLength]
    surname = lastname[:lastLength]
    specialCharacters = ['','_']
    number = str(random.randrange(1,999999))
    username = (firstLetter + specialCharacters[random.randint(0,1)] + surname + number)
    return username
name = str(input("Enter Your Name (Firstname and Lastname Separated with Spaces)"))
print(generateUsername(name))