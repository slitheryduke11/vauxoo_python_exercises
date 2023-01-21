#!/usr/bin/env python3
"""Print and count the lines in a file that start with the word 'From'."""

if __name__ == '__main__':
	# filename = input('Enter filename: ')
	filename = 'mbox-short.txt'
	counter = 0
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			if not line.startswith('From') or line.startswith('From:'): continue
			words = line.split()
			print(words[1])
			counter += 1
		print('There are', counter, 'lines in the file with the word \'From\' at the beginning')
