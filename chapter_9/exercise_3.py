#!/usr/bin/env python3
"""Count the messages that have arrived from each email address."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		email_counter = dict()
		for line in file:
			if not line.startswith('From') or line.startswith('From:'): continue
			words = line.split()
			email_counter[words[1]] = email_counter.get(words[1], 0) + 1
		print(email_counter)