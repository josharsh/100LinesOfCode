"""This program fetches the definition of a word from the Dictionary API
and displays it to the user.
The user is prompted to enter a word, and the program makes a GET request to the API
to retrieve the definition.
The program then extracts and displays the word,
its phonetics, and the number of meanings it has."""
# many line breaks here because the default line length is
# 100 characters but the docstring is longer than that lol
import requests

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_definition(word):
    """Fetches the definition of a word from the Dictionary API and displays it to the user."""
    response = requests.get(f"{URL}{word}", timeout=10)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        word1 = data[0]['word']
        phonetics = data[0]['phonetics'][1]['text']
        number_of_meanings =  len(data[0]['meanings'])
        print(f"Word: {word1}")
        print(f"Phonetics: {phonetics}")
        print(f"Number of meanings: {number_of_meanings}")
        for i in range(0, number_of_meanings):
            try:
                meaning = data[0]['meanings'][i]
                definition = meaning['definitions'][i]
                antonyms = definition.get('antonyms') or 'No antonyms'
                print(
                    f"Meaning {i}: {meaning.get('partOfSpeech','')} "
                    f"Definition {i}: {definition.get('definition','')} "
                    f"Antonyms: {antonyms}"
                )
                # for definition in meaning['definitions']:
                #     print(f"Definition: {definition['definition']}")
            except IndexError:
                continue

def main():
    """Main function to run the program."""
    word = input("Enter a word to get its definition: ")
    get_definition(word)

main()
