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
        humains = []
        for member in message.guild.members:
            if not member.bot:
                humains.append(member)
        gagnant = random.choice(humains)
        await message.channel.send(gagnant.mention)

client.run(token)
