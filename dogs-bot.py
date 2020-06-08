import os
import discord
import youtube_dl
from youtube_search import YoutubeSearch
from discord.ext import commands
import random
from dotenv import load_dotenv
import sys
sys.path.append('./')
import save_mechanik as save

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

dogsbody = commands.Bot(command_prefix="!")

@dogsbody.command(name="leckerli", help="Füttern")
async def balders(ctx):
    await ctx.send("wuf wuf", tts=True)

@dogsbody.command(name="pet", help="Streicheln")
async def pet(ctx):
    await ctx.send("bork bork", tts=True)

@dogsbody.command(name="search_yt", help="Suche auf Youtube")
async def suche (ctx, such:str, tiefe:int):
    i = 0
    ergebnisse = YoutubeSearch(such, max_results=tiefe).to_dict()
    while i<tiefe:
        ergebnisse_dict = ergebnisse[i]
        for item in ergebnisse_dict:
            if item == 'title':
                await ctx.send("{0}".format(ergebnisse_dict[item]))
            elif item == 'id':
                await ctx.send("{0}: {1}".format(item, ergebnisse_dict[item]))
        i = i+1

@dogsbody.command(name="post_id", help="Poste Video mit dieser ID")
async def post (ctx, post_id:str):
    await ctx.send("https://youtube.com/watch?v="+post_id)

@dogsbody.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} ist da'.format(member), tts=True)

"""

@dogsbody.command(name="roll", help="Würfeln")
async def roll(ctx, anzahl_wuerfel: int, seitenzahl: int):
        wurf = [
            str(random.choice(range(1, seitenzahl +1)))
            for _ in range(anzahl_wuerfel)
        ]
        ergebnis = ','.join(wurf)
        await ctx.send('{0.author} hat {1} gewürfelt'.format(ctx, ergebnis))
"""

@dogsbody.command(name="roll", help="Würfel würfeln")
async def roll(ctx, dicepool: str):
    dice_elemente = list(dicepool.split(','))
    endergebnis: str = ""
    x = len(dice_elemente)
    i = 0
    while x>i:
        anzahl = int(dice_elemente[i])
        seitenzahl = int(dice_elemente[i+1])
        wurf = [
            str(random.choice(range(1, seitenzahl +1)))
            for _ in range(anzahl)
        ]
        ergebnis = ','.join(wurf)
        endergebnis = ergebnis + ',' + endergebnis
        i = i+2
    await ctx.send('{0.author} hat {1} gewürfelt'.format(ctx, endergebnis))

@dogsbody.command(name="raise", help="Raise/See für Dogs in the Vinyard, nimmt einen Würfelpool und einen Raise/See")
async def pool_updater(ctx, pool1: str, pool2: str):
    pool2_elemente = list(pool2.split(','))
    pool1_elemente = list(pool1.split(','))#[key for key in pool1.split(',') if key not in pool2_elemente]
    
    i = len(pool2_elemente)
    while i>0:
        pool1_elemente.remove(pool2_elemente[i-1])
        i = i-1

    antwort = ','.join(pool1_elemente)

    await ctx.send('Neuer Pool von {0.author}: {1}'.format(ctx, antwort))


@dogsbody.command(name="see", help="Raise/See für Dogs in the Vinyard, nimmt einen Würfelpool und einen Raise/See")
async def pool_updater_see(ctx, pool1: str, pool2: str):
    pool2_elemente = list(pool2.split(','))
    pool1_elemente = list(pool1.split(','))#[key for key in pool1.split(',') if key not in pool2_elemente]
    
    i = len(pool2_elemente)
    while i>0:
        pool1_elemente.remove(pool2_elemente[i-1])
        i = i-1

    antwort = ','.join(pool1_elemente)

    await ctx.send('Neuer Pool von {0.author}: {1}'.format(ctx, antwort))


@dogsbody.command(name="stat", help="Zufälliger Stat-Block für Dogs")
async def stats (ctx):
    i = 0
    stat_liste = []
    while i < 4:
        stat_liste.append(random.randint(2,6))
        i = i+1
    await ctx.send(str(stat_liste))


@dogsbody.command(name="trait", help="Zufälliger Trait / Zufällige Beziehung für Dogs")
async def relations (ctx, n:int):
    i = 0
    relation = []
    relation_liste = ["2d4", "1d4", "1d6", "1d8", "1d10", "2d6", "2d8", "2d10", "3d6", "3d8"]
    while i < n:
        relation.append (relation_liste[random.randint(0,9)])
        i = i+1
    await ctx.send(str(relation))

dogsbody.run(TOKEN)
