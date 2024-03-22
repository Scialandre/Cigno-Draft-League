import discord
from discord.ext import commands
import logging

from var import *


client = commands.Bot(command_prefix=botPrefix,intents=discord.Intents.all())

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

logging.basicConfig(level=loggerLevel, format="%(asctime)s - %(levelname)s - %(message)s")

client = commands.Bot(
    command_prefix=botPrefix,
    intents=discord.Intents.all(),
    help_command=help_command
)




@client.event
async def on_ready():
    print('---------------------')
    print('Piton Ciliegia Online')
    print('---------------------')
    channel= client.get_channel(masterChannel)
    await channel.send('---------------------')
    await channel.send('Piton Ciliegia Online')
    await channel.send('---------------------')

###
@client.command()
async def hello(ctx):
    await ctx.send(f'hello {ctx.message.author}')

@client.command()
async def goodbye(ctx):
    await ctx.send('Buona giornata')

@client.command()
async def siopera(ctx):
    await ctx.send('who can? kapkan :joy:')
###

@client.command(aliases=['sd'])    
async def shutdown(ctx):
    if ctx.message.author.id in admins:
        
        print('----------------------\nPiton Ciliegia Offline\n----------------------')

    
        channel= client.get_channel(masterChannel)
        logging.info(f'Bot shutdown by {ctx.message.author}')        
        await channel.send('----------------------\nPiton Ciliegia Offline <@232466674299699211>\n----------------------')

        await client.close()

    else:
        await ctx.send('Non puoi farlo tu.')
        logging.info(f'{ctx.message.author} tried to shutdown the bot')

@client.command(hidden=True, aliases=['msd'])
async def master_shutdown(ctx):
    logging.warning(f'Master Shutdown by {ctx.message.author}')
    await client.close()

@client.command()
async def link(ctx):
    global botInviteLink
    await ctx.send(botInviteLink)



if __name__ == "__main__":
    client.run(botToken)
