const insults = require('./insults');

const randomRange = (min, max) => (Math.floor(Math.random() * (max - min) + min));
const getRandomStringFromCollection = (collection) => (insults[collection][randomRange(0, insults[collection].length)])

let generated = [];
Object.keys(insults).forEach(key => {
    generated.push(getRandomStringFromCollection(key))
});

const insult = `🥀 Thou ${generated.join(' ')}! 💀`
console.warn(insult)
