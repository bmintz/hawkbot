from . import bot

from configparser import ConfigParser
import sys

def get_config(filename):
	print(filename)
	config = ConfigParser()
	config.read(filename)
	return config


def main():
	config = get_config(sys.argv[1])

	bot.config = config
	bot.run(config['login']['token'])

if __name__ == '__main__':
	main()