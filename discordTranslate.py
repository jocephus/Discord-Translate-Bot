#!/usr/bin/env python3


import discord
from googletrans import Translator

# Replace 'YOUR_TOKEN' with your own Discord bot token
TOKEN = 'YOUR_TOKEN'

# Create a Discord client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Create a Translator object
translator = Translator()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is in Hebrew
    if translator.detect(message.content).lang == 'he':
        # Translate Hebrew to English
        translation = translator.translate(message.content, src='he', dest='en')
        await message.channel.send(f'**Original (Hebrew)**:\n{message.content}\n**Translation (English)**:\n{translation.text}')
    elif translator.detect(message.content).lang == 'en':
        # Translate English to Hebrew
        translation = translator.translate(message.content, src='en', dest='he')
        await message.channel.send(f'**Original (English)**:\n{message.content}\n**Translation (Hebrew)**:\n{translation.text}')

# Start the bot
client.run(TOKEN)
