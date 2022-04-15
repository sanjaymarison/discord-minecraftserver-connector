'''
A primitive bot to connect your minecraft server with discord to execute minecraft commands
@author = sanjay marison
'''


#change to your screen name where the minecraft server us running


import discord
import os

TOKEN = "" #add the token of your server
screen_name = 'mcserver' #replace with screen name of your server
dist = "/home/server/Documents/Universe/logs" #replace with the location of you servers log file

su = 558218797522092054 #replace the id of the user you want to give special priveleges to (can be found by running message.author.id)

def get_output():
	with open(dist+"/latest.log","r") as readfile:
		data = str(readfile.read())
		data = data.splitlines()
		return data[-1]
    
def get_log():
	with open(dist+"/latest.log","r") as readfile:
		data = str(readfile.read())
		return data
    
def shutdown():
	return

def start():
	return

commands = ["/teleport","/tp","/tellraw","/time","/title","/trigger","/weather","/worldborder","/ban-ip","/banlist","/ban","/deop","/op","/pardon","/pardon-ip","/perf","/save-all","/save-off","/save-on","/setidletimeout","/stop","/whitelist","/list"]


client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hello emily'):
		await message.channel.send('Hello There!')

	if message.content.startswith("show log"):
		await message.channel.send(get_log())

	if message.author.id == su:
		if message.content.startswith("shutdown server"):
			await message.channel.send("Shutting Down...")
			shutdown()
            
		elif message.content.startswith("start server"):
			await message.channel.send("Starting server")
			start()
                                       
		elif message.content.startswith("emily"):
			await message.channel.send("Yes, boss...")

	for command in commands:
		if message.content.startswith(command):
			os.system(f"screen -S {screen_name} -X stuff '{message.content}\n'")
			await message.channel.send('Done!')
			await message.channel.send(get_output())
            
#replace token with your token id
client.run(TOKEN)
