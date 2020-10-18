const movieQuote = require("popular-movie-quotes");

console.log(movieQuote.getAll()); //returns an object with all available quotes.

console.log(movieQuote.getSomeRandom(10)); // returns an object of 10 random quotes.

console.log(movieQuote.getRandomQuote()); // returns a random quote

console.log(movieQuote.getQuoteByYear(2000, 2019)); // returns a sorted object within the range of year 2000 -2019

console.log(movieQuote.getQuotesByMovie("Joker")); //If present returns and array with all quotes of joker movie,
//else returns empty.

console.log(movieQuote.getQuotesByType("anime")); //If present returns and array
// with all quotes of type anime, else returns empty.
