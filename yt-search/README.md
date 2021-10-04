# yt-search
Youtube Crawler with no API that returns 3 first videos by default.

## Install
```sh
npm i @citoyasha/yt-search
```

## Usage
```sh
yt.search(search_term) //returns the first 3 videos
yt.search(search_term, nb) //returns nb videos
```

```sh
const yt = require('@citoyasha/yt_search');
let query = "Tunisia88";
yt.search(query, 10)
.then(function(result) {
//result returns the first 10 videos
});
```

## Returns
```sh
[
  {
    id: 'pRpeEdMmmQ0',
    title: 'Shakira - Waka Waka (This Time for Africa) (The Official 2010 FIFA World Cup™ Song)',
    time: '3:31',
    link: 'https://www.youtube.com/watch?v=pRpeEdMmmQ0',
    thumbnail: 'https://i.ytimg.com/vi/pRpeEdMmmQ0/hqdefault.jpg'
  },
  {
    id: '1zacYmrdexA',
    title: 'Waka Waka (This Time for Africa) - Shakira (Lyrics) 🎵',
    time: '4:02',
    link: 'https://www.youtube.com/watch?v=1zacYmrdexA',
    thumbnail: 'https://i.ytimg.com/vi/1zacYmrdexA/hqdefault.jpg'
  },
  {
    id: 'gVfgTw_W_JY',
    title: 'Just Dance 2018 • Waka Waka (Football Version)',
    time: '3:59',
    link: 'https://www.youtube.com/watch?v=gVfgTw_W_JY',
    thumbnail: 'https://i.ytimg.com/vi/gVfgTw_W_JY/hqdefault.jpg'
  }
]
```

