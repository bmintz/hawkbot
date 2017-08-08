from . import bot
from configparser import ConfigParser

def get_config(filename):
	config = ConfigParser()
	with open(filename) as config_file:
		config.read(config_file)
	return config


def main():
	config = get_config('config.ini')
	
	bot.config = config
	bot.run(config['login']['token'])
