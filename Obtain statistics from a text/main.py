file = open('No se culpe a nadie.txt', 'r')
text = file.read()
sentences = text.split(".")
suspensionPoints = text.split("...")
words = text.split(" ")

print("STATISTICS")
print("Characters:",len(text))
print("Sentences:", len(sentences))
print("Words:",len(words))

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
