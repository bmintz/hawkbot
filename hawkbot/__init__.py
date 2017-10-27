
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
    if (bot.config['bot']['reply_to'].lower() in message.content.lower()
    		and not is_me(message)):
        await message.channel.send(bot.config['bot']['reply_with'])

def is_me(message):
    return message.author == bot.user
