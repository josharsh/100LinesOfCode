//* ----------HTML tags----------
let quote = document.querySelector("#text");
let author = document.querySelector("#author");
let tweet = document.querySelector("#tweet-quote");
let body = document.querySelector("body");
let buttons = document.querySelectorAll(".button");
let getNewQuoteButton = document.querySelector("#new-quote");

//* ----------CSS Variables----------

const colors = [
  "#16a085",
  "#27ae60",
  "#2c3e50",
  "#f39c12",
  "#e74c3c",
  "#9b59b6",
  "#FB6964",
];
const family = [
  "Nothing You Could Do",
  "Shadows Into Light",
  "Indie Flower",
  "Pacifico",
  "Caveat",
  "Kalam",
  "Mali",
];

//* ----------Handle Functions----------
const getNewQuote = () => {
  let randNum = parseInt(Math.random() * 7);
  fetch("https://api.quotable.io/random?minLength=40&maxLength=50")
    .then((res) => res.json())
    .then((data) => {
      let url = `https://twitter.com/intent/tweet?hashtags=quotes${encodeURIComponent(
        data.tags.map((tag) => `,${tag}`)
      )}&text=${encodeURIComponent('"' + data.content + '" ' + data.author)}`;

      quote.textContent = data.content;
      author.textContent = data.author;
      tweet.setAttribute("href", url);

      //* styling
      body.style.color = colors[randNum];
      quote.style.fontFamily = family[randNum];
      body.style.backgroundColor = colors[randNum];
      buttons[0].style.backgroundColor = colors[randNum];
      buttons[1].style.backgroundColor = colors[randNum];
    });
};

//  element.setAttribute("class", "democlass");

// * ----------Event Listners----------
document.addEventListener("DOMContentLoaded", getNewQuote);

getNewQuoteButton.addEventListener("click", getNewQuote);
