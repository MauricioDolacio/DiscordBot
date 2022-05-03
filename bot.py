from typing_extensions import Required
import discord
from discord.ext import commands
from discord import guild
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
import random

bot = commands.Bot(command_prefix="&") #Prefix
slash = SlashCommand(bot, sync_commands=True)
token = "" #Insira o token do bot aqui



@slash.slash(
    name="hello",
    description="Envia uma mensagem",
    guild_ids=[610609008373399562], #OBS: Encontrar uma forma de pegar o ID do servidor
    options=[
        create_option(
            name="option",
            description="Choose your word!",
            required=True,
            option_type=3,
            choices=[
                create_choice(
                    name="World!",
                    value="world"
                ),
                create_choice(
                    name="You!",
                    value="you"
                )
            ]
        )
    ]
)

async def _hello(ctx:SlashContext, option:str):
    await ctx.send(option)



@slash.slash(
    name="roll",
    description="Rola um d20",
    guild_ids=[610609008373399562]
)

async def _roll(ctx: SlashContext):
    roll = random.randint(1, 20)
    await ctx.send("Roll:", str(roll))



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