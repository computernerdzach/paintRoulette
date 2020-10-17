import os
import random
import discord
from dotenv import load_dotenv

technique = ('Speed Paint: 40 Minutes / 16 color palette / 2 brushes', 'Speed Paint: 60 Minutes / extended '
             'palette and tools', 'Personal Demon: Unlimited Time / Strive for Personal Best', 'Technique '
             'Feature', 'Theme Challenge')
techFeat = ('Non Metallic Metal', 'Loaded Brush Blending', 'Object Source Lighting', 'Glazing', 'Wet Blend', 'Freehand'
            'Two Brush Blending','Drybrush', 'Edge Highlight', 'Weathering')
themeCh = ('Grimdark', 'Neon', 'Gem Tones', 'Oldschool Warhammer', 'Pastel', 'Comic Book')
color = ('Red-Violet', 'Violet', 'Blue-Violet', 'Blue', 'Blue-Green', 'Green', 'Yellow-Green', 'Yellow', 'Yellow-Orange',
         'Orange', 'Orange-Red', 'Red', 'Brown', 'Black', 'Gray', 'White')
setting = ('Mountain', 'Forest', 'Swamp', 'Dungeon', 'Snow', 'Sewer')
quotes = ("We don't make mistakes, just happy little accidents.",
          "Talent is a pursued interest. Anything that you're willing to practice, you can do.",
          "There's nothing wrong with having a tree as a friend.", "I guess I’m a little weird. I like to talk to trees"
          " and animals. That’s okay though; I have more fun than most people.", "Let's get crazy.", "Believe that you "
          "can do it cause you can do it.", "What can be painted can be punished.")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()


def roulette():
    theRoll = '```Challenge: '
    tech = random.choice(technique)
    theRoll += tech + "\n"
    if tech == 'Technique Feature':
        feat = random.choice(techFeat)
        theRoll += 'Technique Feature: ' + feat + '\n'
    elif tech == 'Theme Challenge':
        chall = random.choice(themeCh)
        theRoll += 'Theme Challenge: ' + chall + '\n'
    color1 = random.sample(color, 1)
    color2 = random.sample(color, 1)
    theRoll += 'Colors: ' + str(color1) + ', and ' + str(color2) + '\n'
    sett = random.choice(setting)
    theRoll += 'Setting: ' + sett + '```'
    return theRoll


def quote():
    return random.choice(quotes)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    user = str(message.author)
    if message.author == client.user:
        return
    if '!paint' in message.content.lower():
        await message.channel.send(roulette())
    elif '!bob' in message.content.lower():
        await message.channel.send(quote())
    elif '!bye' in message.content.lower():
        await message.channel.send('Thanks for painting with me!')
        await client.close()

client.run(TOKEN)