#!/usr/bin/env python3
"""Call an undefined function to raise an error."""

if __name__ == '__main__':
	repeat_chorus()


def show_chorus():
	"""Print a fun chorus."""
	print('I am a lumberjack, what a joy.')
	print('I sleep all night and work all day.')


def repeat_chorus():
	"""Call the show_chorus function twice."""
	show_chorus()
	show_chorus()