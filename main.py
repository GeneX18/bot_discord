import os
import discord
import random
from DBmanager import DBmanager
from PG import PG
from PG import getPGinfo
from Map import Map
from discord.ext import commands
#from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.messages = True

#Parole da lodare
right_words = [
    "luca fa schifo", "viva i biscotti", "flavio deve venire sul server"
]

#Ele Smettila
forbidden_name_Ele = ["rory", "roy", "ruairi", "inglese", "kinder", "edmund"]

#Cose da trovare
cose = [
    "{} euro!", "nulla...", "una famiglia di procioni...",
    "la dignità di Eleonora..."
]
pesi = [.75, .2, .04, .01]

bot = commands.Bot(command_prefix='-', intents=intents)
#slash = SlashCommand(bot, sync_commands=True)


@bot.command(name='cerca', help='fa cose belle')
async def cerca(ctx):
    r = random.randint(1, 18)
    await ctx.send(
        str(ctx.author.name) + ' ha trovato, ' +
        ''.join(random.choices(cose, pesi, k=1)).format(r))


# COMANDI RPG
dbtest = DBmanager("./data/saves.json")
dbtest.loadFromFile()
map = Map()


@bot.command(name='creaPG', help='fa quello che dice')
async def creaPG(ctx, *args):
    id = str(ctx.guild.id) + str(ctx.author.id)

    if id in dbtest.getKeys():
        await ctx.reply("Hai già un PG.")
    elif len(args) != 2:
        await ctx.reply(
            """Costruzione errata,\nEs: -creaPg "nomePG" "classePG" """)
    else:
        pg = PG(args[0], args[1], 1, 0.0, random.randint(-1, 5),
                random.randint(-1, 5))
        #updatePGinDB(id, pg)
        dbtest.updateDB(id, pg)
        await ctx.reply("Creazione completata.\n" + pg.printInfo())


@bot.command(name='vediPG', help='fa quello che dice')
async def vediPG(ctx):
    id = str(ctx.guild.id) + str(ctx.author.id)
    if id not in dbtest.getKeys():
        await ctx.reply("Non hai un PG da visualizzare.")
    else:
        pg = getPGinfo(dbtest.dictFromDB(id))
        await ctx.reply(pg.printInfo())


@bot.command(name='eliminaPG', help='fa quello che dice')
async def eliminaPG(ctx, arg):
    id = str(ctx.guild.id) + str(ctx.author.id)
    if arg == "confermo" and id in dbtest.getKeys():
        #del db[id]
        dbtest.deleteDB(id)
        await ctx.reply("Eliminazione completata.")
    else:
        await ctx.reply("""Eliminazione errata,\nEs: -eliminaPG confermo """)


@bot.command(name='mappa', help='fa quello che dice')
async def apriMappa(ctx):
    await ctx.reply("La mappa mostra:\n" + map.locationList())


@bot.command(name='esplora', help='fa quello che dice')
async def esplora(ctx, idluogo: int):
    id = str(ctx.guild.id) + str(ctx.author.id)
    if not (id in dbtest.getKeys()):
        await ctx.reply("Non hai un PG con cui esplorare!")
    elif (map.canExplore(idluogo)):
        nome = dbtest.dictFromDB(id)['nome']
        location = map.locationName(idluogo)
        enc = map.explore(idluogo)
        await ctx.reply(nome + " esplorando <" + location +
                        "> ha incontrato un " + enc)
    else:
        await ctx.reply("Luogo non valido.")


@bot.event
async def on_ready():
    print('Bot is ready')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content

    if any(word in msg.lower() for word in right_words):
        txt = "Hai ragione!".format(message)
        await message.reply(txt)
    elif any(word in msg.lower() for word in forbidden_name_Ele):
        txt = "<@1030221184605884426> smettila...".format(message)
        await message.reply(txt)
    await bot.process_commands(message)


bot.run(TOKEN)
