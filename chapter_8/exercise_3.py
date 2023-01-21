#!/usr/bin/env python3
"""Print the third word of each line of a file beginning with 'From'."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			words = line.split()
			if len(words) < 3 or words[0] != 'From': continue
			print(words[2])