# i have NO IDEA what i'm doing tbh #

letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

BOT_TOKEN = "YOUR_TOKEN_HERE"
import discord
import requests
import random
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('natori'):
        await message.channel.send('natori is my goat i love polargeist wait no thats geometry dash i mean poltergeist')

    if message.content.startswith('j-rock') or message.content.startswith('jrock'):
        await message.channel.send('its me, your friendly neighborhood jrock enthusiast!')
    
    if message.content.startswith('larp'):
        await message.channel.send('im always larping, except for jrock, i love jrock')

    if message.content("?SOOD"):
        daily_song()

    def daily_song():
        char1 = random.randint(0,25)
        char2 = random.randint(0,25)
        let1 = letter[char1]
        let2 = letter[char2]
        query = let1 + let2
        print(query)




client.run(BOT_TOKEN)


