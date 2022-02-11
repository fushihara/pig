#!usr/bin/env python

from setuptools import setup, find_packages

raise ValueError("error!")
setup(name="pig2",
	version="0.1",
	description="descです",
	url="https://github.com/fushihara/pig",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	pig = pig.pig:main
	""",
	)
