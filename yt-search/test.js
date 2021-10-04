const yt = require('./yt_search.js');
yt.search("Waka Waka", 10)
.then(function(result) {
console.log(result)
});
