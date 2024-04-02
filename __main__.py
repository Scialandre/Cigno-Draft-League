import discord
from discord.ext import commands
import logging
from sys import argv

from private_var import *
from public_var import *
from pythonScripts import *
from pythonScripts import discordBot




def htmlScript():
    infile = open(r'C:\Users\scial\OneDrive\Desktop\progetti_html\Cigno-Draft-League\vediamo\standings\standings.html','r')
    outfile = open(r'C:\Users\scial\OneDrive\Desktop\progetti_html\Cigno-Draft-League\vediamo\standings\standings1.html','w')
    line='<!--generated through python-->\n'
    alternator = True
    i=1

    while  not (line.endswith('<!---->\n')):
        outfile.write(line)
        line=infile.readline()


    for coach in coaches:

        if alternator:
            theme = 'light'
        else:
            theme = 'dark'

        alternator = not alternator

        outfile.write(f'<a href="../team/{coach}.html">\n<div class="player-container-{theme}">\n                    <div class="position-div">\n            <p class="position-p">\n              {i}\n            </p>\n          </div><img src="../images/{coach}.jpg" class="player-logo">\n          <p class="player-name">\n            {coach}\n          </p>\n          <p class="team-name">{coach}</p>\n        </div>\n</a>')

        i+=1


    outfile.write('    </div>\n  </div>\n  <div class="footer"></div>\n</html>')
      
    

  




    infile.close()
    outfile.close()
    



if __name__ == "__main__":
    if argv[1]=='bot':
        discordBot.runBot()
    elif argv[1]=='script':
        htmlScript()
