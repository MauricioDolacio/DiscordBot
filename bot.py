import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "&")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('Babigi'))
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

with open("token.0", "r", encoding="utf-8") as configfile:
    token = configfile.read()

client.run(token)
