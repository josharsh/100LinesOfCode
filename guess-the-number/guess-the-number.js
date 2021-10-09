let randomNum = Math.floor(Math.random() * (10 - 1) + 1);

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
 
readline.question('Guess the number between 1 and 10?', guess => {
  if (guess == randomNum) {
    console.log(`The number I was thinking of was ${randomNum}, and you guessed ${guess}. Beginners luck!`);
  } else {
    console.log(`Oof sorry! You guessed ${guess}, but the number I was expecting was ${randomNum}`);
  }
  readline.close();
});