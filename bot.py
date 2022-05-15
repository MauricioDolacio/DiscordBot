import asyncio
import discord
from discord.ext import commands, tasks
import os
from itertools import cycle
import random

client = commands.Bot(command_prefix = "&")
status = cycle(['Esqueceu de responder dnvkk', 'Layla Morre', 'Chora fi', 'Olha ele ai'])
songs = ['./source/olhae.mp3', './source/rapaz.mp3', './source/amogus.mp3', './source/atumalaca.mp3', './source/elegosta.mp3', './source/irra.mp3', './source/patrao.mp3', './source/tome.mp3', './source/tururu.mp3']

@client.event
async def on_voice_state_update(member, before, after):
  if not before.channel and after.channel:
    if member != client.user:
        channel = member.voice.channel
        voice = await channel.connect()

        number = random.randint(0, len(songs)-1)
        voice.play(discord.FFmpegPCMAudio(songs[number]))

        while True:
            await asyncio.sleep(2)
            if voice.is_playing() == False:
                await voice.disconnect()
                break

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')



@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

@client.command()
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))



#Open Token
with open("token.0", "r", encoding="utf-8") as configfile:
    token = configfile.read()

client.run(token)
