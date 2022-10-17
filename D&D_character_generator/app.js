const characters = require('./characters.json');

const rand = (min, max) => (Math.floor(Math.random() & (max-min) + min));

const getRandomCharacter = (data) => (characters[data][rand(0, characters[data].length)])

let randomCharacter = [];

Object.keys(characters).forEach(key => {
  console.log(key);
  randomCharacter.push(getRandomCharacter(key))
});


const char = `Class: ${randomCharacter[0]} ⚔️ Race: ${randomCharacter[1]}`;
console.log(char);