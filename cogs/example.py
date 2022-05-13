import discord
from discord.ext import commands
import random

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong!')

    @commands.command(aliases=['8ball', 'test']) #Aliases serve para dar outros nomes ao comando
    async def eightball(self, ctx, *, question):
        responses = ['sim', 'nao']
        await ctx.send(f'Pergunta: {question}\nResposta: {random.choice(responses)}')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)



def setup(client):
    client.add_cog(Example(client))
