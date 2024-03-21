import express from "express";
import bodyParser from "body-parser";


const app=express();
const port=3000;



app.use(express.static("public"));
app.use(bodyParser.urlencoded({extended:true}));

const data=new Date();
const today=data.getDate()+"/"+"0"+(data.getMonth()+1)+"/"+data.getFullYear();

app.listen(port,()=>{
     console.log(`Listening on port ${port}`);
});
 var day=[];
 var work=[];

app.get("/",(req,res)=>{
     res.render("index.ejs",{listTitle:today,
    ListItem:day });
});
  
app.get("/work",(req,res)=>{
     res.render("index.ejs",{listTitle:"Work",ListItem:work});
});


app.post("/submit",(req,res)=>{
       let value=req.body[""];
       if(req.body["listsubmit"]=="Work"){ work.push(req.body["newItem"]);
       res.redirect("/work");}
       else{
       day.push(req.body["newItem"]);
       res.redirect("/");}
});




// app.post("/submit",(req,res)=>{
//        let value=req.body["newItem"];
// day.push(value);
// res.render("index.ejs",{listTitle:today,
//      ListItem:day });
// });


// app.post("/submit",(req,res)=>{
//      let value=req.body["newItem"];
// day.push(value);
// res.render("index.ejs",{listTitle:today,
//    ListItem:day });
// });



// app.post("/submit", (req,res)=>{
    
//      data.push(req.body["newItem"]);
     
//      res.render("index.ejs",{to:data});
// })
