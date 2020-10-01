var express = require('express');
var router = express.Router();
var nodemailer = require("nodemailer");
const config = require('../config');


router.get('/', function(req, res, next) {
  res.render('login', { title: 'LOGIN PAGE' });
});

module.exports = router;
