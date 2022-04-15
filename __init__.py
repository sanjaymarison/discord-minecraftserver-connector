'''
A primitive bot to connect your minecraft server with discord to execute minecraft commands
@author = sanjay marison
'''


#change to your screen name where the minecraft server us running
screen_name = 'mcserver'

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


commands = [
	"/teleport",
	"/tp",
	"/tellraw",
	"/time",
	"/title",
	"/trigger",
	"/weather",
	"/worldborder",
	"/ban-ip",
	"/banlist",
	"/ban",
	"/deop",
	"/op",
	"/pardon",
	"/pardon-ip",
	"/perf",
	"/save-all",
	"/save-off",
	"/save-on",
	"/setidletimeout",
	"/stop",
	"/whitelist"
]

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hello emily'):
		await message.channel.send('Hello There!')


	for command in commands:
		if message.content.startswith(command):
			print(message.content)
			os.system(f"screen -S {screen_name} -X stuff '{message.content}\n'")
			await message.channel.send('Done! (Note if there was any error in running the command it will not be displayed here)')


#replace token with your token id
client.run(TOKEN)

