#!/usr/bin/env python3
"""Count the total number of lines beginning with 'Subject:' in a file."""

import sys

if __name__ == '__main__':
	filename = input('Enter filename: ')
	if filename == 'na na boo boo': # Easter Egg
		print('NA NA BOO BOO FOR YOU - I\'ve got you!')
		sys.exit()
	counter = 0
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			if line.startswith('Subject:'):
				counter += 1
		print('There are', counter, 'subject lines in', filename)