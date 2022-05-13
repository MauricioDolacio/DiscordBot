import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = "&")

@client.event
async def on_ready():
    print("Bot is ready for use")


# @client.event
# async def on_member_join(member):
#     print(f'{member} Entrou no servidor!')


# @client.event
# async def on_member_remove(member):
#     print(f'{member} Saiu do servidor :(')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {client.latency * 1000}ms')


@client.command(aliases=['8ball', 'test']) #Aliases serve para dar outros nomes ao comando
async def eightball(ctx, *, question):
    responses = ['sim', 'nao']
    await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


client.run('ODc2OTQwMzQ3MTMxOTgxODk1.GSrcdm.jMWuOJjOEIuNHsh6QoG1Ttes905MOPIrL5BwfA')
