const fs = require('fs')
const path = require("path")

var extensions = [""]

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Your files will be sorted into folders, write any filenames that you don\'t want sorted.\nSeperate them by spaces (index.js main.py) ', files => {
  var exclude = files.split(/[ ,]+/);
  fs.readdir(__dirname, (err, files) => {
    if (err)
      console.log(err);
    else {
      
      files.forEach(file => {
        let ext = path.extname(file)

        if (ext == ""){
          extensions.push(file)
        }

        if (!exclude.includes(file)){
          if (!extensions.includes(path.extname(file))){
            extensions.push(ext)
      
            fs.mkdir(path.join(__dirname, ext), {}, err => {
              if(err) throw err;
            })

            fs.rename(path.join(__dirname, file), path.join(__dirname, ext, file), function (err) {
              if (err) throw err
            })

          } else {
            fs.rename(path.join(__dirname, file), path.join(__dirname, ext, file), function (err) {
              if (err) throw err
            })
          }
        }
      })
    }
  })

  readline.close();
});