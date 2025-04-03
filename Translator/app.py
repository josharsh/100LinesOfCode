import requests
from deepl import Translator
from deepl.exceptions import DeepLException
import threading
import time
from os import environ

metadApiKey = environ.get('metadAPI_key') or 'INSERT API KEY HERE'
deepLApiKey = environ.get('deepl_key') or 'INSERT API KEY HERE'
trigger = threading.Event()
#Matrix with the languges that needs a specification about zone
languages_specification = [
                            ['EN', ['EN-GB', 'EN-US']],
                            ['PT', ['PT-BR', 'PT-PT']]
                        ]

def backgroundProgress(message):
    '''Background function that shows a status message while processing the request'''
    global trigger

    print(f"\n{message}", end = '', flush = True)
    while not trigger.is_set():
        print(".", flush = True, end = '')
        time.sleep(1)


def createThread(targetFunctionMessage = "Processing your request"):
    '''Creates a thread to be executed concurrently the main thread is executing an heavy operation\n
    Returns `Thread` object'''
    global trigger
    daemonThread = threading.Thread(target = backgroundProgress, daemon = True, args = [targetFunctionMessage])
    trigger.clear()
    daemonThread.start()
    return daemonThread

def stopThread():
    '''Stops the thread and prints a success message (if the trigger variable is not already set to `True`)'''
    global trigger
    if(not trigger.is_set()):
        trigger.set()
        print("\nDone.")

def get_prompt():
    '''Asks the user a word or phrase to translate and the target language\n
    Returns the word/phrase (`prompt`) and the target language code (`langCode`)'''
    prompt = input("Please input a word or phrase that you'd like to translate: ").strip()
    while(prompt == ''):
        prompt = input("Please input something to translate: ").strip()
    targetLanguage = input("Great! Now input the target language that you'd like to translate to: ").capitalize().strip()
    while(targetLanguage == ''):
        targetLanguage = input("Please input a language for translating the phrase (example: english, italian, etc): ").capitalize().strip()
    langCode = get_languageCode(targetLanguage)
    return [prompt, langCode]

def get_languageCode(target):
    '''Gets the languages list and the target languages and gets the relative language ISO code\n
    Returns the language code if found, otherwise `False`'''
    createThread()
    headers = {'Accept': 'application/json', 'Ocp-Apim-Subscription-Key': metadApiKey}
    languagesList = makeApiRequest('https://global.metadapi.com/lang/v1/languages/', headers)['data']
    
    for language in languagesList:
        if(target in language['langEnglishName']):
            stopThread()
            return validateLanguageInput(language['langCode'].upper())
    stopThread()
    return False

def validateLanguageInput(langCode):
    '''Makes the user choose a valid target language for the translation.\n
    Returns the validated selected language code'''
    while(not langCode):
        targetLang = input("The selected language was not valid, try again: ").strip().capitalize()
        while(not targetLang):
            targetLang = input("The language input was not valid, try again: ").strip().capitalize()
        langCode = get_languageCode(targetLang)
    #Checking if the selected language code is inside the languages list that require "dialect" specification
    if(langCode in [lang[0] for lang in languages_specification]):
        #Getting from the user the right language dialect and appending it to the variable
        langCode = chooseLanguageFormat([lang[1] for lang in languages_specification if lang[0] == langCode])
    return langCode

def chooseLanguageFormat(language):
    '''Lets the user choose between the correct dialect options.\n
    Returns the selected dialect code'''
    #Prints out all the supported language dialects and asks for language selection
    print("\nSelect a language: ")
    for counter, dialect in enumerate(language[0], start = 1):
        print(f"{counter}) {dialect}")
    while True:
        try:
            userChoice = int(input('Select an option: '))
            while userChoice <= 0 or userChoice > len(language[0]):
                userChoice = int(input('Please choose a number from the provided list: '))
        except ValueError:
            print("Invalid input... Try again.")
        else:
            break
    #Returning `userChoice - 1` because the selection input starts at 1
    return language[0][userChoice - 1]

def makeApiRequest(url, headers = None, data = None, method = 'GET'):
    '''Makes an API request using values passed to function call\n
    Returns the response in JSON format'''
    if(method == 'GET'):
        apiResponse = requests.get(url, headers = headers, data = data).json()
    else:
        apiResponse = requests.post(url, headers = headers, data = data)
    return apiResponse

def translate_prompt(prompt, targetLangCode):
    '''Translates the prompt to the desired target language\n
    Returns the translated text in form of string'''
    global trigger
    createThread('Translating your message')
    #`updatedTarget` is a flag variable used to report that the target language has changed, so the translation process needs to be repeated
    updatedTarget = False
    #Getting the Deepl API key from from the virtual environment and translating the text
    translator = Translator(deepLApiKey)
    #Managing Bad target language error by re-requesting the language and re-executing the translation function until the target language is correct
    try:
        translatedText = translator.translate_text(prompt, target_lang = targetLangCode)
    except DeepLException:
        targetLanguage = validateLanguageInput(False)
        return translate_prompt(prompt, targetLanguage)
    #Validating input (checking if the detected source language is the same as the target one)
    #Repeating input until the two languages are different
    while(translatedText.detected_source_lang == targetLangCode or targetLangCode == ''):
        trigger.set()
        #Updating variable to avoid repeated API request
        updatedTarget = True
        #Repeating the target language input
        targetLangCode = input(f"\nThe target language you have chosen is the same as the detected language ({translatedText.detected_source_lang})\nPlease input a valid target language: ").capitalize().strip()
        targetLangCode = get_languageCode(targetLangCode)
    #Repeating the translation process if the target language has changed, otherwise just returning the already translated prompt
    if(updatedTarget == True):
        createThread('Translating your message')
        #Translating text again with the correct destination language
        translatedText = translator.translate_text(prompt, target_lang = targetLangCode)
    stopThread()
    return (translatedText.detected_source_lang, translatedText.text)


def main():
    prompt, targetLanguage = get_prompt()
    detectedLang, translatedText = translate_prompt(prompt, targetLanguage)
    print(f"Translated from {detectedLang} to {targetLanguage} => {translatedText}")


if __name__ == '__main__':
    main()