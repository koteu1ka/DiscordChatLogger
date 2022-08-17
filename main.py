#Python 3.10
#Coded by koteu1ka / Version: 1.0.0[17.08.22]

import discord;from discord.ext import commands
import datetime 
from colorama import init,Fore,Back,Style;init(autoreset=True)
logger=commands.Bot(command_prefix='.')
time = datetime.datetime.now();time=str(time)
@logger.event
async def on_ready():
	log=open('logs/log.txt','a');log.write('#newlog '+time+'\n');log.close()
	print('  '+Back.GREEN+'|loading|', datetime.datetime.now())
	print('  '+Back.GREEN+'|Coded by koteuika_')
@logger.event
async def on_message(message):
	GCAC=' Message>> [{0.guild},{0.channel}] {0.author}: {0.content}'.format(message) #GCAC[Guild Channel Author Content]
	print('  [',datetime.datetime.now(),']',GCAC)
	log=open('logs/log.txt','a');log.write('['+time+']'+GCAC+'\n');log.close()
logger.run('token') #token
