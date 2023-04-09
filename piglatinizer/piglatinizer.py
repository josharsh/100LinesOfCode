def pig_latin(word):
    if word[0] in "aeiou":
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"


def pig_latin_sentence(sentence):
    words = sentence.split()
    pig_latin_words = [pig_latin(word.lower()) for word in words]
    return " ".join(pig_latin_words)

input = input("Enter text to be converted: ")
pig_latin_text = pig_latin_sentence(input)
print("Pig Latin:", pig_latin_text)