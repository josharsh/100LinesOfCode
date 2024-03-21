#Importing Modules Needed
import discord as ds
from discord.ext import commands
import random, sys
import requests
import json
import nest_asyncio
nest_asyncio.apply() #needed to keep the python script running in Spyder IDE!

#Nebula Tuple
nebulaList = ("Orion Nebula.jpg","Eagle Nebula.jpg","Crab Nebula.jpg",\
              "Ring Nebula.jpg","Helix Nebula.jpg","Horsehead Nebula.jpg",\
              "Carina Nebula.jpg","Lagoon Nebula.jpg","Cat's Eye Nebula.jpg",\
              "Butterfly Nebula.jpg","Veil Nebula.jpg","Hourglass Nebula.jpg")
#Planet Factopedia Tuple
planetList = ("Mercury is hot, but not too hot for ice",\
              "Venus doesn’t have any moons, and we aren’t sure why.",\
              "The Earth’s Molten Iron Core Creates a Magnetic Field",\
              "Mars had a thicker atmosphere in the past.",\
              "Jupiter is a great comet catcher.",\
              "No one knows how old Saturn’s rings are",\
              "Uranus is more stormy than we thought.",\
              "Neptune has supersonic winds.")
#Tuple of emojis (Can add more)
emojiList = ('💖','❤','😒','😎','😜','👌','🌹','😁','🤳',\
             '🎃','😍','🤩','😪','🥳')

"""LIST OF HELPER FUNCTIONS"""
#Helper function to get quotes from zenquotes
def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  print(json_data)
  quote = json_data[0]['q']+" -"+json_data[0]['a']
  return quote

#Token of Bot - Copy from Developer Discord Portal
token = <bot_token>

#2. Making Bot Object with prefix as $(prefix symbol can be changed)
client = commands.Bot(command_prefix="$")

"""LIST OF COMMANDS"""

#$hello - Says hello to the user
@client.command(name = "hello")
async def hello(ctx):
  await ctx.message.channel.send("Hello!!! {0.author.display_name}".format(ctx.message))
  await ctx.message.add_reaction('👋')
#$inspire - Returns a quote scraped from zenquotes.io
@client.command(name = "inspire")
async def inspire(ctx):
  await ctx.message.channel.send(get_quotes())
#$emotion - Returns a random emoji from emoji tuple
@client.command(name = "emotion")
async def giveEmoji(ctx):
  await ctx.message.channel.send(random.choice(emojiList))
#$planet <n> - Gives a fact and picture of the nth planet
@client.command(name = "planet")
async def planet(ctx,arg1):
  num = int(arg1)-1
  if num in range(0,8):
    s = planetList[num]
    fs = "planets/"+arg1+".jpg"
    await ctx.send(s)
    await ctx.send(file = ds.File(fs))
  else:
    await ctx.send("Invalid Planet Number Given! Try giving number between 1-8 🤔")
#$nebula - Gives the name and picture of a nebula randomly
@client.command(name = "nebula")
async def nebula(ctx):
    fs = "nebulas/"+random.choice(nebulaList)
    s = fs[8:-4]
    await ctx.send(s)
    await ctx.send(file = ds.File(fs))

#When Bot comes Online, prints the message below on console
@client.event
async def on_ready():
    print("We are logged in as {0.user}".format(client))


#Event carried out when a user send a message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    #Says hello back when greeted with "Hello Botname" message
    if msg.startswith('hello') and "bot-name" in msg:
        await message.channel.send("Hello👋 {}".format(message.author.display_name))  
        await message.add_reaction('👋')
    await client.process_commands(message)

#Starts running the Bot
client.run(token)

