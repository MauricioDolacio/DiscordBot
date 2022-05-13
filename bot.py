import discord
from discord.ext import commands, tasks
import os
from itertools import cycle


client = commands.Bot(command_prefix = "&")
status = cycle(['Esqueceu de responder dnvkk', 'Layla Morre', 'Chora fi', 'Olha ele ai'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is online')

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

# @client.event
# async def on_member_join(member):
#     print(f'{member} Entrou no servidor!')

# @client.event
# async def on_member_remove(member):
#     print(f'{member} Saiu do servidor :(')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


#Open Token
with open("token.0", "r", encoding="utf-8") as configfile:
    token = configfile.read()

client.run(token)
