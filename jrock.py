# i have NO IDEA what i'm doing tbh #

BOT_TOKEN = "YOUR_TOKEN_HERE"
import discord
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



client.run(BOT_TOKEN)


