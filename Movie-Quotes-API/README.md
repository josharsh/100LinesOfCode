## Movie Quotes API
An API to get some movie quotes

### Run the API
- cd Movie-Quotes-API
- npm install
- node app.js

### API callbacks
1. /all -> get all quotes availaible

2. /quotes-by-year -> get quotes between two particular years, provided in the query header. Ex - 2003 to 2009

3. /random-quotes -> get some random quotes, returns 1 random quotes if not specified the number. Ex - 10

4. /quotes-by-movie -> get quotes by a particular movie, provided in the query header. Ex - Joker

5. /quotes-by-type -> get quotes by a specific type of movie. Ex - Anime