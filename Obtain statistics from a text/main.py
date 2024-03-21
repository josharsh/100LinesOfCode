import re
file = open('No se culpe a nadie.txt', 'r')
text = file.read()
sentences = text.split(".")
suspensionPoints = text.split("...")
words = text.split(" ")

#Calculating number of syllables (Works only for English texts)
def count_syllables(text):
    count = 0
    vowels = "aeiouy"
    text = text.lower()
    text = re.sub(r"[^a-z]", "", text)
    if text[0] in vowels:
        count += 1
    for index in range(1, len(text)):
        if text[index] in vowels and text[index-1] not in vowels:
            count += 1
    if text.endswith("e"):
        count -= 1
    if text.endswith("le"):
        count+=1
    if count == 0:
        count +=1
    return count


#Counter of a specific word 
print("Input the word of which you want to find its frequency in the text:")
word1 = input()
occurances = words.count(word1)

print("Number of occurances of",word1,"is : ", occurances);

print("STATISTICS")
print("Characters:",len(text))
print("Sentences:", len(sentences))
print("Words:",len(words))
print("Syllables:",count_syllables(text))

#Store words with more than 8 characters
sentence = []
#Additional element to store words 
aux = []  

#Convert uppercase to lowercase and also remove the dots,
#comas and \n from the word list
for i in words:
    aux.append(i.lower().replace(",", "").replace(".", "").replace("\n", ""))

for i in aux:
    if len(i) > 8:
        sentence.append(i)

#Counter for how often words with more than 8 characters appear
rep = [] 
for i in sentence:
    rep.append(sentence.count(i))

print("The most frequently repeated word with more than 8 characters is:",sentence[rep.index(max(rep))])
file.close()
