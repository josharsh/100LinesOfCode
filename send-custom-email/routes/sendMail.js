var express = require('express');
var router = express.Router();
var nodemailer = require("nodemailer");
const config = require('../config');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('editor', { title: 'HTML EDITOR' });
});

router.post('/', async (req, res) => {
    console.log(req.body)

    var smtpTransport = nodemailer.createTransport({

        service: "Gmail",
        auth: {
            user: req.body.senderEmail,
            pass: req.body.password,
        }
    });

    var mailOptions = {
        from:`${req.body.senderEmail}`,
        to : `${req.body.recerverEmail}`,
        subject : `${req.body.subject}`,
        html: `${req.body.body}`,
    }

    await smtpTransport.sendMail(mailOptions, (error, response) => {
        if(error){
            console.log("ERROR");
            console.log(error);
            res.statusCode = 404;
            res.render('editor', { title: 'HTML EDITOR' });
        }else{
            console.log(response);
            // console.log("Message sent: " + response);
            res.statusCode = 200;
            res.setHeader('Content-Type', 'application/json');
            res.json({success: true, status: 'Mail sent successfully !'});
        }
        // smtpTransport.close();
    })
})

module.exports = router;
