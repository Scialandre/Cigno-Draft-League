import discord
from discord.ext import commands
# py  C:\Users\Giovanni\PycharmProjects\discordBot\main.py
botToken='discord developer portal'
botPrefix='-'

client = commands.Bot(command_prefix=botPrefix,intents=discord.Intents.all())



@client.event
async def on_ready():
    print('---------------------')
    print('Piton Ciliegia Online')
    print('---------------------')
    channel= client.get_channel(1061583591315869737)
    await channel.send('---------------------')
    await channel.send('Piton Ciliegia Online')
    await channel.send('---------------------')

@client.event
async def on_member_join(member):
    channel= client.get_channel(1061583591315869737)
    await channel.send('Benvenuto nella Sciala Draft League!')

@client.event
async def on_member_remove(member):
    channel= client.get_channel(1061583591315869737)
    await channel.send(f'{member} non verrai dimenticato.')

@client.command()
async def hello(ctx):
    await ctx.send(f'hello {ctx.message.author}')

@client.command()
async def goodbye(ctx):
    await ctx.send('buona giornata')

@client.command()
async def siopera(ctx):
    await ctx.send('who can? kapkan :joy:')

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel= ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send(f'Non sei in alcun Voice Channel {ctx.message.author}')




client.run(botToken)
