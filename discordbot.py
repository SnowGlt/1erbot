import discord
import os
from dotenv import load_dotenv
import random

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!tirage'):
        gagnant = random.choice(message.guild.members)
        await message.channel.send(gagnant)

client.run(token)
