const axios = require('axios');
const cheerio = require('cheerio');
const hltb = require('howlongtobeat');
const hltbService = new hltb.HowLongToBeatService();
const game = {
    name: '',
    platform: '',
    time: '',
    timeExtras: '',
    timeFull: '',
    metascore: '',
    userScore: ''
}
class GetGameTimeScore {
    async getScores (platform, gameName) {
        hltbService.search(gameName).then(result => {
            game.name=result[0].name
            game.time=result[0].gameplayMain
            game.timeExtras=result[0].gameplayMainExtra
            game.timeFull=result[0].gameplayCompletionist
            game.platform=platform
        }).catch(err=>console.error(err));
        try{
            const nameCleaned = gameName.replace(/\s/g, '-')
            const URL = 'https://www.metacritic.com/game/'+platform+'/'+nameCleaned
            const { data } = await axios.get(URL)
            const $ = cheerio.load(data);
    
            game.metascore=$('div.metascore_w').filter('.xlarge').filter('.game').first().text()
            game.userScore=$('div.metascore_w').filter('.user').filter('.large').first().text()

            return game;
        }catch(err){
            console.error(err.response.status);
        }
        
    };
    
}
module.exports = new GetGameTimeScore();