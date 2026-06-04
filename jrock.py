def daily_song():
    real_song = False
    while not real_song: # generates an 8 digit code, the length of AudioDB's IDs. Then checks if that matches up with an actual song on the database, and tries again if it doesn't #
        char1 = random.randint(0,4)
        char2 = random.randint(0,9)
        char3 = random.randint(0,9)
        char4 = random.randint(0,9)
        char5 = random.randint(0,9)
        char6 = random.randint(0,9)
        char7 = random.randint(0,9)
        char8 = random.randint(0,9)
        query = str(char1) + str(char2) + str(char3) + str(char4) + str(char5) + str(char6) + str(char7) + str(char8)
        print(query)
        song_search = f"https://www.theaudiodb.com/api/v1/json/123/track.php?m={query}"
        song = requests.get(song_search)
        print(song.text)
        if song.text != '{"track":null}' and query not in songlist:
            real_song = True
            print("i found a real song boss")
            songlist.append(query)
            return song.json()


BOT_TOKEN = "YOUR_TOKEN_HERE"
thedate = ""
songlist = [] # keeps track of IDs that have already been used so you don't get duplicate songs #
import discord        
import requests
import random
from datetime import date
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}') # confirms that you're logged in as the bot you're trying to log in as #

@client.event
async def on_message(message):
    if message.author == client.user: # makes sure the bot isn't responding to itself forever if one of it's messages contains a trigger word #
        return

# various words that trigger the bot to says certain things #
    if 'natori' in message.content.lower():
        await message.channel.send('natori is my goat i love polargeist wait no thats geometry dash i mean poltergeist')

    if 'jrock' in message.content.lower() or "j-rock" in message.content.lower():
        await message.channel.send('its me, your friendly neighborhood jrock enthusiast!')
    
    if "larp" in message.content.lower():
        await message.channel.send('im always larping, except for jrock, i love jrock')

# runs the daily song function and prints out the song's info. also reacts if song of the day is by two specific j-rock artists #
    if message.content == '?SOOD':
        global thedate
        global info
        global title
        global artist
        global album
        if thedate == "" or thedate != str(date.today()): # if a song has already been generated for the day it just prints the same one again #
            thedate = str(date.today())
            await message.channel.send('give me a second to curate the perfect song of the day!')
            info = daily_song()
            title = info['track'][0]['strTrack']
            artist = info['track'][0]['strArtist']
            album = info['track'][0]['strAlbum']
            await message.channel.send('ive selected a song!')
        await message.channel.send(f"Song of the Day for {thedate}:")
        await message.channel.send(f"Title: {title}")
        await message.channel.send(f"Artist: {artist}")
        await message.channel.send(f"Album: {album}")
        if info['track'][0]['strArtist'].lower == "asian kung-fu generation" or info['track'][0]['strArtist'].lower() == "kessoku band":
            await message.channel.send('omg bocchi the rock reference') 

    # explains what the command is in case users need help #
    if message.content == '?help':
        await message.channel.send('send the command "?SOOD" to get the song of the day!')


    # sends a message if the bot is pinged #
    if client.user.mentioned_in(message):
        await message.channel.send('hi do you wanna talk about jrock i really like jrock')



# runs code #
client.run(BOT_TOKEN)


