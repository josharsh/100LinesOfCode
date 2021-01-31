const fs = require('fs')
const mime = require('mime-types')
const venom = require('venom-bot')
venom.create().then((client) => start(client))
function start(client) {
client.onMessage(async (message) => {
    if (message.isMedia) {
      const buffer = await client.decryptFile(message)
      const fileName = `image.${mime.extension(message.mimetype)}`
      await fs.writeFile(fileName, buffer, async (err) => {
        if(err){
          console.log(err)
        } else {
            await client.sendImageAsSticker(message.from, `./${fileName}`).catch((err) => { })
        }
      })
    }
  })
}