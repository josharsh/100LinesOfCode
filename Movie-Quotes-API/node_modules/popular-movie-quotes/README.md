![GitHub license](https://img.shields.io/github/license/NikhilNamal17/popular-movie-quotes.svg?style=for-the-badge&logo=github) ![NPM MODULE](http://img.shields.io/badge/popularmovie-quotes-orange.svg?style=for-the-badge&logo=imdb) ![NPM MODULE](https://img.shields.io/github/issues/NikhilNamal17/popular-movie-quotes?style=for-the-badge&logo=appveyor) ![NPM MODULE](https://img.shields.io/github/forks/NikhilNamal17/popular-movie-quotes?logo=github&style=for-the-badge) ![NPM MODULE](https://img.shields.io/github/stars/NikhilNamal17/popular-movie-quotes?color=yellow&logo=github&style=for-the-badge) ![NPM MODULE](https://img.shields.io/github/languages/code-size/NikhilNamal17/popular-movie-quotes?style=for-the-badge&logo=docusign) ![NPM MODULE](https://img.shields.io/github/languages/top/NikhilNamal17/popular-movie-quotes?style=for-the-badge&logo=javascript)
[![npm](https://img.shields.io/npm/dy/popular-movie-quotes.svg?logo=npm&style=for-the-badge)](https://www.npmjs.com/package/popular-movie-quotes) [![GitHub last commit](https://img.shields.io/github/last-commit/NikhilNamal17/popular-movie-quotes.svg?logo=git&style=for-the-badge)](https://github.com/NikhilNamal17/popular-movie-quotes) [![Maintenance](https://img.shields.io/maintenance/yes/2019.svg?logo=npm&style=for-the-badge)](https://github.com/NikhilNamal17/NikhilNamal17)
![Mergify Status](https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/NikhilNamal17/popular-movie-quotes&style=for-the-badge)

#### A simple [NPM](https://www.npmjs.com/package/popular-movie-quotes) package to get popular movie quotes.

## Getting started

[![NPM](https://nodei.co/npm/popular-movie-quotes.png?compact=true)](https://nodei.co/npm/popular-movie-quotes/)

```bash
$ npm i popular-movie-quotes --save
```

## Installation

[![NPM INSTALL](http://img.shields.io/badge/npm-install-blue.svg?style=for-the-badge&logo=npm)](https://docs.npmjs.com/getting-started/installing-npm-packages-locally) [![NODE JS](http://img.shields.io/badge/Node-JS-teal.svg?style=for-the-badge&logo=node.js)](https://nodejs.org/en/) [![NODE JS](https://img.shields.io/npm/v/popular-movie-quotes?logo=npm&label=popular-movie-quotes&style=for-the-badge)](https://www.npmjs.com/package/popular-movie-quotes)

This is a [Node.js](https://nodejs.org/en/) module available through the
[npm registry](https://www.npmjs.com/).

Before installing, [download and install Node.js](https://nodejs.org/en/download/).

Installation is done using the
**[`npm install`](https://docs.npmjs.com/getting-started/installing-npm-packages-locally)** command:

```bash
$ npm i popular-movie-quotes --save
```

## Usage

[![usage](https://forthebadge.com/images/badges/you-didnt-ask-for-this.svg)](https://github.com/NikhilNamal17/popular-movie-quotes)

- **getAll()** method returns an array of objects, each containing **quote** and **movie**.

```json
{
  "quote": "Frankly, my dear, I don't give a damn.",
  "movie": "Gone with the Wind",
  "type": "movie",
  "year": 1939
}
```

- **getQuoteByYear(startYear, endYear)** method returns a sorted object within the range of year startYear -endYear\*\*

```json
[
    {
        "quote": "Frankly, my dear, I don't give a damn.",
        "movie": "Gone with the Wind",
        "type": "movie",
        "year": startYear
    }
    ...
    .....
    {
        "quote": "Frankly, my dear, I don't give a damn.",
        "movie": "Gone with the Wind",
        "type": "movie",
        "year": endYear
    }
]
```

- **getSomeRandom(count)** method returns an array (of length 'count') of non-duplicate random objects containing **quote** and **movie**.

```json
[
  {
    "quote": "Frankly, my dear, I don't give a damn.",
    "movie": "Gone with the Wind",
    "type": "movie",
    "year": 1939
  }
  // with 'count' number of quote objects.
]
```

- **getRandomQuote()** method returns a random **movie** quote :

```javascript
I used to think that my life was a tragedy. But now I realize, it’s a comedy.
```

- **getQuotesByMovie("MovieName")** method returns an array with all quotes of MovieName movie, else returns empty.

```json
[
  {
    "quote": "Frankly, my dear, I don't give a damn.",
    "movie": "Gone with the Wind",
    "type": "movie",
    "year": 1939
  }
]
```

- **getQuotesByType("movie/anime/tv")** method returns an array with all quotes of type movie/anime/tv, else returns empty.

```json
[
   {
        "quote": "Frankly, my dear, I don't give a damn.",
        "movie": "Gone with the Wind",
        "type": "movie",
        "year": 1939
    }
    ...
    .....
    {
        "quote": "You all love twisting the knife into one another.",
        "movie": "Knives Out",
        "type": "movie",
        "year": 2019
  }
]
```

```javascript
const movieQuote = require("popular-movie-quotes");

console.log(movieQuote.getAll()); //returns an object with all available quotes.

console.log(movieQuote.getSomeRandom(10)); // returns an object of 10 random quotes.

console.log(movieQuote.getRandomQuote()); // returns a random quote

console.log(movieQuote.getQuoteByYear(2000, 2019)); // returns a sorted object within
// the range of year 2000-2019

console.log(movieQuote.getQuotesByMovie("Joker")); //If present returns and array
// with all quotes of joker movie, else returns empty.

console.log(movieQuote.getQuotesByType("anime")); //If present returns and array
// with all quotes of type anime, else returns empty.
```

## Testing

- Check if quote is duplicate/already present.

```bash
$ npm test
```

## Want to contribute?

[![Open Source Love](https://badges.frapsoft.com/os/v3/open-source-175x29.png?v=103)](https://github.com/NikhilNamal17) [![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://github.com/NikhilNamal17/popular-movie-quotes)

> Please check issues **[here](https://github.com/NikhilNamal17/popular-movie-quotes/issues)**!

## License

![GitHub license](https://img.shields.io/github/license/NikhilNamal17/popular-movie-quotes.svg?style=for-the-badge&logo=github)

## Let's get connected

[![Twitter Follow](https://img.shields.io/twitter/follow/Nikhil17_namal.svg?style=for-the-badge&logo=twitter)](https://twitter.com/Nikhil17_namal) [![GitHub followers](https://img.shields.io/github/followers/NikhilNamal17.svg?label=Follow&style=for-the-badge&logo=github)](https://github.com/NikhilNamal17/) [![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@nikhilnamal&color=9cf&logo=facebook&style=for-the-badge&logoColor=white&colorA=informational)](https://www.facebook.com/nikhil.namal) [![Instagram](https://img.shields.io/static/v1.svg?label=follow&message=@NikhilNamal&color=grey&logo=instagram&style=for-the-badge&logoColor=white&colorA=critical)](https://www.instagram.com/nikhil_namal17/) [![LinkedIn](https://img.shields.io/static/v1.svg?label=connect&message=@nikhilnamal&color=success&logo=linkedin&style=for-the-badge&logoColor=white&colorA=blue)](https://www.linkedin.com/in/nikhil_namal17/)

## Special Thanks

#### Karan Bhatt [![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@KaranBhatt&color=9cf&logo=facebook&style=for-the-badge&logoColor=white&colorA=informational)](https://www.facebook.com/karan.bhatt.7524) [![Instagram](https://img.shields.io/static/v1.svg?label=follow&message=@KaranBhatt&color=grey&logo=instagram&style=for-the-badge&logoColor=white&colorA=critical)](https://www.instagram.com/karanbhatt/) [![GitHub followers](https://img.shields.io/github/followers/ItachiHyuga.svg?label=Follow&style=for-the-badge&logo=github)](https://github.com/ItachiHyuga/)

#### Rishabh Kanojia [![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@RishabhKanojia&color=9cf&logo=facebook&style=for-the-badge&logoColor=white&colorA=informational)](https://www.facebook.com/rishabh.kanojiya.18) [![Instagram](https://img.shields.io/static/v1.svg?label=follow&message=@RishabhKanojia&color=grey&logo=instagram&style=for-the-badge&logoColor=white&colorA=critical)](https://www.instagram.com/rishabhkanojiya/) [![GitHub followers](https://img.shields.io/github/followers/rishabhkanojiya.svg?label=Follow&style=for-the-badge&logo=github)](https://github.com/rishabhkanojiya/)

## Support me for a couple of coffee

Hey! Help me out with a couple of coffee!

<a href="https://www.buymeacoffee.com/nikhilnamal" target="_blank"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I215TEM)

<hr>

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-javascript.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
