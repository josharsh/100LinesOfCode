const express = require('express');
const app = express()
const axios = require('axios')
const cheerio = require('cheerio')
const BASE_URL="http://knowyourmeme.com/";
const port = process.env.PORT || 3000;
const NodeCache = require( "node-cache" );
global.nodeCache = new NodeCache();


app.get('/api/search',async (req,res)=>{
        const searchParam = req.query.q.toLowerCase()
        // console.log(searchParam)
        const finalURL = BASE_URL+"search?q="+searchParam;
        let imgArray = []
        try {
            if(global.nodeCache.has(searchParam)) {
              imgArray = global.nodeCache.get(searchParam)  
            } else {
              let response = await axios.get(finalURL);
              let $ = cheerio.load(response.data);
              const grid = $('.entry-grid-body');
              const searchItem = grid.find('tr td a')[0];
              let photos = BASE_URL+searchItem.attribs.href+'/photos';
              response = await axios.get(photos);
              $ = cheerio.load(response.data);
              const imgTop = $('meta[property="og:image"]').attr('content')
              const imgGallery =  $("a[rel=photo_gallery]")
              for(let i=0;i<imgGallery.length;i++){
                imgArray.push({url:imgGallery[i].attribs.href,top:false})
              }
              imgArray.push({url:imgTop,top:true})
              global.nodeCache.set(searchParam,imgArray,86400)
            }
            const index = Math.floor(Math.random()*imgArray.length)
            let img
            if(imgArray[index].top === true ) {
                img = imgArray[index].url
            } else {
                const randomUrl = BASE_URL+imgArray[index].url
                if(global.nodeCache.has(randomUrl)) {
                  img = global.nodeCache.get(randomUrl)
              } else {
                response = await axios.get(randomUrl);
                $ = cheerio.load(response.data);
                img = $('meta[property="og:image"]').attr('content')
                global.nodeCache.set(randomUrl,img,8640)
                }
            }
            return res.status(200).json({
              url: img
              })  
        } catch(e) {
              console.log('Error '+e.toString())
              return res.status(200).json({
                  message:'Sorry could not find your meme. Please search again'
               })
    }
       
})

app.listen(port,()=>{
     console.log('Listening on '+port)
})