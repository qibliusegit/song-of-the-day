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
        if song.text != '{"track":null}':
            real_song = True
            print("i found a real song boss")
            return song.json()


BOT_TOKEN = "YOUR_TOKEN_HERE"
import discord        
import requests
import random
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}') # confirms that you're logged in as the bot you're trying to log in as #

@client.event
async def on_message(message):
    if message.author == client.user: # makes sure the bot isn't responding to itself forever if one of it's messages contains a trigger work
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
        await message.channel.send('give me a second to curate the perfect song of the day!')
        info = daily_song()
        title = info['track'][0]['strTrack']
        artist = info['track'][0]['strArtist']
        album = info['track'][0]['strAlbum']
        await message.channel.send("Your Song of the Day:")
        await message.channel.send(f"Title: {title}")
        await message.channel.send(f"Artist: {artist}")
        await message.channel.send(f"Album: {album}")
        if info['track'][0]['strArtist'].lower == "asian kung-fu generation" or info['track'][0]['strArtist'].lower() == "kessoku band":
            await message.channel.send('omg bocchi the rock reference')  

    if client.user.mentioned_in(message):
        await message.channel.send('hi do you wanna talk about jrock i really like jrock')



# runs code #
client.run(BOT_TOKEN)


