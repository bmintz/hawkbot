#!/usr/bin/env python3
# encoding: utf-8

import setuptools

setuptools.setup(
	name='hawkbot',
	version='0.0.2',
	
	packages=['hawkbot'],
	
	entry_points={
		'console_scripts': 'hawk-bot = hawkbot.__main__:main',
	},
)
