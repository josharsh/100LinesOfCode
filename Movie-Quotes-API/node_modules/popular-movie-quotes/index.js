let array = require("./data/data.json");

const randomNum = () => {
  return Math.floor(Math.random() * array.length);
};

const getQuoteByYear = (start, end) => {
  return array
    .filter(i => i.year >= start && i.year <= end)
    .sort((a, b) => (a.year > b.year ? 1 : b.year > a.year ? -1 : 0));
};

const getRandomQuote = () => {
  let randNum = randomNum();
  return array[randNum].quote;
};

const getSomeRandom = count => {
  let randomQuotesArray = [];
  let randomQuotesSet = new Set(); // to prevent duplicate quotes
  while (randomQuotesArray.length < count) {
    let quote = array[randomNum()];
    if (!randomQuotesSet.has(quote)) {
      randomQuotesArray.push(quote);
    }
  }
  return randomQuotesArray;
};

const getQuotesByObject = (quote, obj) => {
  let resultArray = [];
  quote = quote.toLowerCase();
  object = obj;
  array.forEach(item => {
    item[object] = item[object].toLowerCase();
    if (item[object] && item[object].includes(quote)) {
      resultArray.push(item);
    }
  });

  return resultArray;
};

const getQuotesByMovie = quote => {
  return getQuotesByObject(quote, "movie");
};

const getQuotesByType = quote => {
  return getQuotesByObject(quote, "type");
};

const getAll = () => {
  return array;
};

module.exports = {
  getAll,
  getRandomQuote,
  getSomeRandom,
  getQuoteByYear,
  getQuotesByMovie,
  getQuotesByType
};
