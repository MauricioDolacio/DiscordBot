import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option


bot = commands.Bot(command_prefix="&") #Prefix
slash = SlashCommand(bot, sync_commands=True)
token = "ODc2OTQwMzQ3MTMxOTgxODk1.YRrYVw.4djeMZ5Xjwf9rAOBCbe4f0qY_co" #Insira o token do bot aqui

@slash.slash( #Comandos com /
    name="hello",
    description="Envia uma mensagem",
    guild_ids=[610609008373399562]
)

async def _hello(ctx:SlashContext):
    await ctx.send("Fala fi")


@bot.event
async def on_ready():
    print('Estamos logados com {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if "bom dia bot" in message.content:
        await message.channel.send(f"Bom dia {message.author.name}")

    await bot.process_commands(message)

@bot.command(name="oi") #&oi
async def send_hi(ctx):
    name = ctx.author.name
    response = "Olá, " + name

    await ctx.send(response)

bot.run(token)