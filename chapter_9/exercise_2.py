#!/usr/bin/env python3
"""Counts the occurrences of days in lines beginning with the word 'From'."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		day_counter = dict()
		for line in file:
			if not line.startswith('From') or line.startswith('From:'): continue
			words = line.split()
			day_counter[words[2]] = day_counter.get(words[2], 0) + 1
		print(day_counter)