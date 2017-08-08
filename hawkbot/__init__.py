import discord

bot = discord.Client()

@bot.event
async def on_ready():
	print('----------------------')
	print('Logged in as:')
	print('Username:', bot.user.name)
	print('ID:', bot.user.id)
	print('----------------------')


@bot.event
async def on_message(message):
	if 'technically' in message.content.lower():
		await bot.send_message(
			message.channel,
			'***Terminology Hawks, DEPLOY***'
		)

