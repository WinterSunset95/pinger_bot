import discord
import pyjokes
from discord.ext import commands
from webapp import keep_alive
import os
import requests

TOKEN = os.environ['TOKEN']
intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", intents=intents)


#events
@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))

#commands

#below is an example format
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

@client.command()
async def hello (ctx):
  await ctx.send("Hello World!")

@client.command()
async def whats_my_id(ctx):
  await ctx.send(ctx.author.id)

@client.command()
async def annoy_everyone(ctx):
  await ctx.send(f"I am so sorry for this. But my author is evil")
  for member in ctx.guild.members:
    member_id = member.id
    await ctx.send(f"<@{member_id}>")

@client.command()
async def joke(ctx):
  the_joke = pyjokes.get_joke(language='en', category='neutral')
  await ctx.send(the_joke)  

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
keep_alive()
client.run(TOKEN)