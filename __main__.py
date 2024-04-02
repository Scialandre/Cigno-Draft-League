import discord
from discord.ext import commands
import logging
from sys import argv

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



def htmlScript():
    infile = open(r'C:\Users\scial\OneDrive\Desktop\progetti_html\Cigno-Draft-League\vediamo\standings\standings.html','r')
    outfile = open(r'C:\Users\scial\OneDrive\Desktop\progetti_html\Cigno-Draft-League\vediamo\standings\standings1.html','w')
    line='<!--generated through python-->\n'
    alternator = True

    while  not (line.endswith('<!---->\n')):
        outfile.write(line)
        line=infile.readline()


    for coach in coaches:

        if alternator:
            theme = 'light'
        else:
            theme = 'dark'

        alternator = not alternator

        outfile.write(f'<a href="../team/{coach}.html">\n<div class="player-container-{theme}">\n          <img src="../images/{coach}.jpg" class="player-logo">\n          <p class="player-name">\n            {coach}\n          </p>\n          <p class="team-name">{coach}</p>\n        </div>\n</a>')




    outfile.write('    </div>\n  </div>\n</html>')
      
    

  




    infile.close()
    outfile.close()
    
    #for coach in coaches:




if __name__ == "__main__":
    if argv[1]=='bot':
        client.run(botToken)
    elif argv[1]=='script':
        htmlScript()
