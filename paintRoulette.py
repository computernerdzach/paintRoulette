import os
import random
import discord
from dotenv import load_dotenv

technique = ('Speed Paint: 40 Minutes / 16 color palette / 2 brushes', 'Speed Paint: 60 Minutes / extended '
             'palette and tools', 'Personal Demon: Unlimited Time / Strive for Personal Best', 'Technique '
             'Feature', 'Theme Challenge')
techFeat = ('Non Metallic Metal', 'Loaded Brush Blending', 'Object Source Lighting', 'Glazing', 'Wet Blend', 'Freehand'
            'Two Brush Blending', 'Dry-brush', 'Edge Highlight', 'Weathering')
themeCh = ('Grimdark', 'Neon', 'Gem Tones', 'Old-School WarHammer', 'Pastel', 'Comic Book')
values = ('Black', 'White', 'Gray', 'Brown')
warm = ('Yellow-Green', 'Yellow', 'Yellow-Orange', 'Orange', 'Orange-Red', 'Red')
cool = ('Red-Violet', 'Violet', 'Blue-Violet', 'Blue', 'Blue-Green', 'Green')
color = (warm, cool, values)
setting = ('Mountain', 'Forest', 'Swamp', 'Dungeon', 'Snow', 'Sewer')
quotes = ("We don't make mistakes, just happy little accidents.",
          "Talent is a pursued interest. Anything that you're willing to practice, you can do.",
          "There's nothing wrong with having a tree as a friend.", "I guess I’m a little weird. I like to talk to trees"
          " and animals. That’s okay though; I have more fun than most people.", "Let's get crazy.", "Believe that you "
          "can do it cause you can do it.", "What can be painted can be punished.", "It's the imperfections that make "
          "something beautiful, that's what makes it different and unique from everything else.",
          "Ever make mistakes in life? Let's make them birds. Yeah, they're birds now.",
          "Put light against light - you have nothing. Put dark against dark - you have nothing. It's the contrast of "
          "light and dark that each give the other one meaning.", "Whatever makes you happy, you put in your world."
          "Let's build us a happy, little cloud that floats around the sky.", "It's so important to do something every "
          "day that will make you happy", "Trees don't grow even, they don't grow straight just however it makes them "
          "happy.", "We have no limits to our world. We're only limited by our imagination.",
          "People might look at you a bit funny, but it's okay. Artists are allowed to be a bit different."
          "It's hard to see things when you're too close. Take a step back and look.",
          "We don't laugh because we feel good; we feel good because we laugh.",
          "Talent is a pursued interest. Anything that you're willing to practice, you can do.")

# use dotenv to retrieve bot's token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# set shortcut for discord.Client()
client = discord.Client()


# assigns and returns two colors
def colorSet():

    # select ranges for each color
    c1 = random.choice(color)
    c2 = random.choice(color)

    # select random colors from each range, first color 1 than color2
    if c1 == values:
        c1 = f'(Value) {random.choice(values)}'
    elif c1 == cool:
        c1 = f'(Cool Color) {random.choice(cool)}'
    elif c1 == warm:
        c1 = f'(Warm Color) {random.choice(warm)}'

    if c2 == values:
        c2 = f'(Value) {random.choice(values)}'
    elif c2 == cool:
        c2 = f'(Cool Color) {random.choice(cool)}'
    elif c2 == warm:
        c2 = f'(Warm Color) {random.choice(warm)}'

    # group colors in a tuple and return them
    colors = (c1, c2)
    return colors

# picks out challenges and returns a string to report these challenges using f syntax
def roulette():
    theRoll = '```Challenge: '
    tech = random.choice(technique)
    theRoll += f'{tech}\n'
    if tech == 'Technique Feature':
        feat = random.choice(techFeat)
        theRoll += f'Technique Feature: {feat} \n'
    elif tech == 'Theme Challenge':
        chall = random.choice(themeCh)
        theRoll += f'Theme Challenge: {chall}\n'
    # assign colors
    colors = colorSet()
    # make sure colors are not the same color twice
    while colors[0] == colors[1]:
        colors = colorSet()
    theRoll += f'Colors: {colors[0]} and {colors[1]}\n'
    sett = random.choice(setting)
    theRoll += f'Setting: {sett}```'
    return theRoll


# grabs a random bob ross quote
def quote():
    return random.choice(quotes)


# prints to console indicating a successful connection to discord
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# here the discord library listens for commands and responds with challenges, quotes, or quitting the program
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

# initialize and launch discord client
client.run(TOKEN)