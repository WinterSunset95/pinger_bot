import discord
import pyjokes
from discord.ext import commands
from webapp import keep_alive
import os
import requests
from time import sleep
from replit import db

# all is forsaken without the holy token
TOKEN = os.environ['TOKEN']
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)

# "Are you ready honey?"
@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))



#below is an example format
# 'ctx' argument lets you send and recieve data to and from the server
# if the following commands were Greek gods, 'ctx' would be hermes
  
@client.command()
async def list_commands(ctx):
  commands = '''
!hello - Says hello
!whats_my_id - gives you your id
!annoy_everyone - mentions everyone in the server
!joke - tells you a one liner joke
!insult <me/username> - use at your own discretion
  '''
  await ctx.send(commands)  


# say hello
@client.command()
async def hello (ctx):
  await ctx.send("Hello World!")

# wanna know your discord id?
@client.command()
async def whats_my_id(ctx):
  await ctx.send(ctx.author.id)

# just to piss someone off
@client.command()
async def annoy(ctx, who, how_long):
  try:
    if who == 'everyone':
      await ctx.send(f"I am so sorry for this. But my author is evil")
      for member in ctx.guild.members:
        member_id = member.id
        await ctx.send(f"<@{member_id}>")
    else:
      await ctx.send(f"Sorry {who}")
      for i in range(0, int(how_long)):
        text = requests.get('https://insult.mattbas.org/api/insult') 
        sleep(1) 
        insult = text.text
        await ctx.send(f"{who} {insult}")
  except:
    await ctx.send("correct usage is !annoy <user> <number>. Please recheck your command")

# oooo this bot got them jokes!
@client.command()
async def joke(ctx):
  the_joke = pyjokes.get_joke(language='en', category='neutral')
  await ctx.send(the_joke)  

# he dissing the homies
@client.command()
async def insult(ctx, arg):
  if arg == 'me':
    text = requests.get('https://insult.mattbas.org/api/insult')
    await ctx.send(text.text)
  else:
    to_search = str(arg)
    text = requests.get("https://insult.mattbas.org/api/insult?who=" + to_search)
    insult_string = text.text
    await ctx.send(f"{arg} {insult_string}")

# well we all gotta know how long he's been up :v
@client.command()
async def uptime(ctx):
  try:
    await ctx.send(str(db['minutes']) + " mins")
  except:
    await ctx.send('Database not available')

# O bot of the server, what is your wisdom

@client.command()
async def quote_here(ctx):
  if db['quote_on'] == 'true':
    await ctx.send('Quotes are active in another channel. !stop it first and try again')
  else:
    db['quote_on'] = 'true'
    while db['quote_on'] == 'true':
      url = "https://motivational-quotes1.p.rapidapi.com/motivation"
      payload = {
	      "key1": "value",
	      "key2": "value"
      }
      headers = {
	      "content-type": "application/json",
	      "X-RapidAPI-Key": "b0286087bfmshfa69e2cad96216ep15190cjsn57eb91b3cf1b",
	      "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
      }
      response = requests.request("POST", url, json=payload, headers=headers)
      quote = response.text
      await ctx.send("Hourly quote")
      await ctx.send(quote)
      sleep(3600)

@client.command()
async def quote(ctx):
  url = "https://motivational-quotes1.p.rapidapi.com/motivation"
  payload = {
	  "key1": "value",
	  "key2": "value"
  }
  headers = {
	  "content-type": "application/json",
	  "X-RapidAPI-Key": "b0286087bfmshfa69e2cad96216ep15190cjsn57eb91b3cf1b",
	  "X-RapidAPI-Host": "motivational-quotes1.p.rapidapi.com"
  }
  response = requests.request("POST", url, json=payload, headers=headers)
  quote = response.text
  await ctx.send(quote)
    
# Thou shalt introduce yourself
@client.command()
async def hello_world(ctx):
  await ctx.send('hello world!')

# oh dont mind my comments XD I like to have fun with words
# HALT I COMMAND YOU
@client.command()
async def stop(ctx):
  db['quote_on'] = 'false'  
  await ctx.send('killed the loop')  
  
# thou shalt not slumber
keep_alive()
# damn u work pretty fast man!
# hehe
# I command thee, RISE!!
client.run(TOKEN)