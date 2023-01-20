#!/usr/bin/env python3
"""Print content of a file in uppercase."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			print(line.rstrip().upper())