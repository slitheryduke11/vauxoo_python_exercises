#!/usr/bin/env python3
"""Get average of the numbers after the string 'New Revision: '."""

import re

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		total, counter = 0, 0
		for line in file:
			line = line.rstrip()
			numbers = re.findall('New Revision: ([0-9]+)', line)
			for number in numbers:
				total += float(number)
				counter += 1
		print(total / counter)