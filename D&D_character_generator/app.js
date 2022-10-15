const characters = require('./characters.json');

function rand(min,max){
  console.log(Math.floor(Math.random() * (max-min) + min));
  
}

function getRandChar(data){
  characters[data][rand(0, characters[data].length)];
}

let charClassRace = [];
Object.keys(characters).forEach(key => {
  console.log(key);
  charClassRace.push(getRandChar(key))
});
console.log(charClassRace);

const char = `Class: ${charClassRace[0]} ⚔️ Race: ${charClassRace[1]}`;
console.log(char);