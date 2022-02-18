import discord
from discord.ext import commands

TOKEN = "NzQzMTMzODYwMzgwMDE2NzIz.XzQPVw.9YPel_wNMFRKu9rUgXoRiFRttO0"
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot Online")

@client.command(name="join")
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(name="leave")
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

client.run(TOKEN)