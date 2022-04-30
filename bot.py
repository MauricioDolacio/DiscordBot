import discord
from discord.ext import commands

bot = commands.Bot("&")

@bot.event
async def on_ready():
    print("Estou pronto!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "sexo" in message.content:
        await message.channel.send(f"É disso que o povo gosta {message.author.name}")

    await bot.process_commands(message)

@bot.command(name="oi") #|oi
async def send_hi(ctx):
    name = ctx.author.name
    response = "Olá, " + name

    await ctx.send(response)

bot.run("")