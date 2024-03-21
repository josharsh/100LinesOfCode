var express= require('express');
var app=express();
var path= require('path');

app.use((request, response, next) => {
    response.header('Access-Control-Allow-Origin', '*');
    response.header('Access-Control-Allow-Headers', 'Authorization, X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Allow-Request-Method');
    response.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    response.header('Allow', 'GET, POST, OPTIONS, PUT, DELETE');
    next();
});

app.get('/', (req,res) =>{
    res.sendFile(path.resolve(__dirname+'/public/index.html'));
});

app.get('/script.js', (req,res) =>{
    res.sendFile(path.resolve(__dirname+'/public/script.js'));
});

app.listen(3000, ()=>{
    console.log('running server on 3000');
});