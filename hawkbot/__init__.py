import discord

bot = discord.Client()

@bot.event
async def on_message(message):
	if 'technically' in message.content.lower():
		await bot.send_message(message.channel, '***Terminology Hawks, DEPLOY***')

