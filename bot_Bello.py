import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command(name='cerca', help='fa cose belle')
async def cerca(ctx):
    r = random.randint(1,7)
    await ctx.send("hai trovato {} euro!".format(r))
    
    
bot.run(TOKEN)