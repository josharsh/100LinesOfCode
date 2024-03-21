This package gets beating time from HLTB and Metacritic scores for the same game.

Usage:
```
const pkg=require('./index.js')
pkg.getScores('xbox-360', 'alan wake').then(res=>console.log(res))
```

The function getScores expects 2 arguments: platform and game. Eveything lowercase. An object with game name, platform, time to beat, time to beat + extras, time for full completion, metascore and userScore is returned as a promise.

```
{ name: 'Alan Wake',
  platform: 'xbox-360',
  time: 11,
  timeExtras: 14.5,
  timeFull: 26,
  metascore: '83',
  userScore: '8.2' }
```

DEPENDENCIES, CREDITS AND DISCLAIMER

Axios: https://github.com/axios/axios

Cheerio: https://github.com/cheeriojs/cheerio#readme

howlongtobeat: https://github.com/ckatzorke/howlongtobeat

This is a personal learning project. I do not recommend using this code in production environments nor do I offer any guarantee. 