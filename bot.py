from discord.ext import commands

bot = commands.Bot("&") #Prefixo

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

bot.run("") #Insira o token do bot aqui