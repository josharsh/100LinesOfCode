//var kjoke=require('knock-knock-jokes');
//console.log(kjoke());
var joke=require('give-me-a-joke');
joke.getRandomDadJoke (function(joke) {
    console.log(joke);
});