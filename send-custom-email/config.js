const dotenv = require('dotenv');
dotenv.config();

module.exports = {
    MAIL_ID: process.env.MAIL_ID,
    MAIL_PASS: process.env.MAIL_PASS,
}

