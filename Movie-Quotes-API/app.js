const express = require('express');
const app = express();
const movieQuotes = require('popular-movie-quotes');

app.get("/", (req, res) => {
    res.send("Movie quotes API");
});

// Get all available quotes
app.get("/all", (req, res) => {
    const quotes = movieQuotes.getAll();
    res.json(quotes);
});

// Get quotes between particular years, default start -> 2010, end -> current year
app.get("/quotes-by-year", (req, res) => {
    let startYear = 2010;
    let endYear = new Date().getFullYear();
    if(req.query.startYear) {
        startYear = req.query.startYear;
    }
    if(req.query.endYear) {
        endYear = req.query.endYear;
    }
    const quotes = movieQuotes.getQuoteByYear(startYear, endYear);
    res.json(quotes);

});

// Get certain number of random quotes. If no value given, return 1 random quote
app.get("/random-quotes", (req, res) => {
    let quotes;
    if(req.query.number) {
        quotes = movieQuotes.getSomeRandom(req.query.number);
    } else {
        quotes = movieQuotes.getRandomQuote();
    }
    res.json(quotes);
});

// Get quotes by movie name
app.get("/quotes-by-movie", (req, res) => {
    if(!req.query.movie) {
        return res.status(400).json({error: "No movie name found!"});
    }
    else {
        const movieName = req.query.movie;
        const quotes = movieQuotes.getQuotesByMovie(movieName);
        res.json(quotes);
    }
});

// Get quotes by movie type, example -> anime
app.get("/quotes-by-type", (req, res) => {
    if(!req.query.type) {
        return res.status(400).json({error: "No type given!"});
    }
    else {
        const quotes = movieQuotes.getQuotesByType(req.query.type);
        res.json(quotes);
    }
});

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`Server running on port ${port}`);
})