const crypto = require('crypto');
const prompt = require('prompt');
const algorithm = 'aes-256-ctr';

let password;
let iv = crypto.createHash('sha256').update(String("vsdjkdhg")).digest('base64').substr(0, 16);

const decrypt = () => {

  try
  {
    prompt.get({name: "encrypted", message: "Encrypted String"}, (error, result) => {
      if(!error)
      {
        let encrypted = result.encrypted;
        prompt.get("Password", (err, result) => {
          if(!err)
          {
            password = result.Password;
            const decipher = crypto.createDecipheriv(algorithm,password, iv);
            let dec = decipher.update(encrypted,'hex','utf8');
            dec += decipher.final('utf8');
            console.log("Decrypted String: ", dec);
          }
        });
      }
    });
  }
  catch(e)
  {
    console.error(e);
  }
  
}

const encrypt = () => {

  try
  {
    prompt.get({name: "string", message: "Enter the String"}, (error, result) => {
      if(!error)
      {
        let string = result.string;
        prompt.get({name: "password", message: "Choose a password (32 characters)"}, (err, result) => {
          if(!err)
          {
            password = result.password;
            const cipher = crypto.createCipheriv(algorithm, password, iv);
            let enc = cipher.update(string, 'utf8', 'hex');
            enc += cipher.final('hex');
            console.log("Encrypted String: ", enc);
          }
        });
      }
    });
  }
  catch(e)
  {
    console.error(e);
  }
}


prompt.start();

console.log("Encrypt/Decrypt Text using AES 256-bit Encryption\n");

console.log("1. Encrypt");
console.log("2. Decrypt");

prompt.get({name: "choice", message: "Please enter your choice (1/2)"}, (err, result) => {
  if(!err)
  {
    switch(parseInt(result.choice))
    {
      case 1: encrypt(); break;
      case 2: decrypt(); break;
      default: console.log("Invalid input.");
    }
  }
});
