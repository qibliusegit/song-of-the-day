def daily_song():
    char1 = random.randint(0,25)
    char2 = random.randint(0,25)
    let1 = letter[char1]
    let2 = letter[char2]
    query = let1 + let2
    print(query)
    song_search = f"https://musicbrainz.org/ws/2/work/?query={query}"
    song = requests.get(song_search)
    print(song.text)

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

    if 'natori' in message.content.lower():
        await message.channel.send('natori is my goat i love polargeist wait no thats geometry dash i mean poltergeist')

    if 'jrock' in message.content.lower() or "j-rock" in message.content.lower():
        await message.channel.send('its me, your friendly neighborhood jrock enthusiast!')
    
    if "larp" in message.content.lower():
        await message.channel.send('im always larping, except for jrock, i love jrock')

    if message.content == '?SOOD':
        daily_song()

    if client.user.mentioned_in(message):
        await message.channel.send('hi do you wanna talk about jrock i really like jrock')




client.run(BOT_TOKEN)


