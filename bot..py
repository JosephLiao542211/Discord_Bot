import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NzE1NjI5NTc5NDk4MjkxMjAy.XtAAvQ.5pGj49OdgXkFWpDFD4XLg0lGb2o'
GUILD = 'Elite'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)