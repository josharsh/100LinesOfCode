# NodeJS Scraper

A WebScraping application which scrapes websites using NodeJS. Currently only
[HackerNews](https://news.ycombinator.com/) website is supported but the code
is modularised in such a way that adding additional websites is very easy.

# Packages used:

-   puppeteer
-   chalk
-   p-queue

# How to use the app

-   Download all the dependencies of the project using `npm i` command.
-   Run either of the three commands to execute the program
    -   `npm start`
    -   `npm run scrape`
    -   `node scrape`
-   A new folder will be created in the `src` directory. This folder contains a
    json file of top 10 articles on hackernews website in json format and a
    screenshot of the website.
-   To add a new website support add its info in the URLs array and write the
    scrapping function similar to `scrapeHackerNews` to get all the data that is
    required.
