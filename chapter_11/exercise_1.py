#!/usr/bin/env python3
"""Simulate the operation of the grep command on Unix."""

import re

if __name__ == '__main__':
	regex = input('Enter regular expression: ')
	filename = 'mbox.txt'
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		coincidences = 0
		# Validate regex
		try:
			re.compile(regex)
		except re.error as e:
			print('Invalid expression:', e)
		else:
			for line in file:
				line = line.rstrip()
				if re.search(regex, line):
					coincidences += 1
			print('mbox.txt has', coincidences, 'lines matching', regex)