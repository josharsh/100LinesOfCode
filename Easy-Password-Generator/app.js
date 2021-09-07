// Required library to generate random words
const faker = require('faker')

// Number of characters, numbers and words to generate the password
const WORDS = 2
const CHARACTERS = 1
const NUMBERS = 4

// Check if the inputs are positive, at least one word is selected and all are integers
if (WORDS < 1 || CHARACTERS < 0 || NUMBERS < 0 || !Number.isInteger(WORDS) || !Number.isInteger(CHARACTERS) || !Number.isInteger(NUMBERS)) {
console.log("Invalid Input")
} else {
    // Generate words separated by a hyphen (-)
    var pass = faker.random.word()
    for (let i = 0; i < WORDS - 1; i++) {
        pass += '-' + faker.random.word()
    }
    
    // Some non-alphanumeric characters to append and a function to get one random
    const characters = [ "~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", "|", ":", ";", "<", ",", ">", ".", "?", "/"]
    const randomChar = () => characters[Math.floor(Math.random()*characters.length)]

    // Append numbers to the end of the word
    for (let i = 0; i < NUMBERS; i++) {
        let num = Math.floor(Math.random()*10) 
        pass += num.toString()
    }
    // Append characters to the beginning of the word
    for (let i = 0; i < CHARACTERS; i++) {
        pass = randomChar() + pass
    }

    // Logging out password
    console.log("Your password is: " + pass)
}