import discord
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get

bot_token = ['NzE1NjI5NTc5NDk4MjkxMjAy.XtKlVA.P-fQEaQIyAtGmkQ0Tzqp3uPywLY','NzQzNDc4NzY1NjgxNjM5NTA1.XzVQjg.HMVC3GSgVmu4QlmXJigaNEId_i0','NzQzNDc5NTk2MDYxNjg3ODE5.XzVRVA.pxpwdeXJB036vyYdBK6pPvBTzZM',
             'NzQzNDc5Nzk5ODQxODE2NjE4.XzVRhQ.GYAAFE1bdAnrk9EKUDIYZvpU4fU','NzQzNDgzMTExNDU4OTk2MjM0.XzVUmw.a-tvdr8E1bf-VYYUKPoMvTWK3Uo','NzQzNDgzMzQ1MTkwNTE4ODE1.XzVU0g.lF5wLdI2h6qBIUd4N57vjfQ9jBc']

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("bot online")

@client.command(pass_context=True)
async def hi(message):
    member = message.author
    var = discord.utils.get(message.guild.roles, name = "Mafia King")
    member.add_role(var)

@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
        print("Joined channel: ", channel)


@client.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.voice:
        # channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client.command(pass_context=True, aliases=['p,','pla'])
async def play(ctx, url: str):

    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("Music is already playing")
        return

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio \n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.08

    nname = name.rsplit("-", 2)
    await ctx.send(f"Playing: {nname[0]}")
    print("playing\n")

client.run(bot_token[1])
