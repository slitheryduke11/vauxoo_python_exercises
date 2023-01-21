#!/usr/bin/env python3
"""Count the messages that have arrived from each email domain."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		domain_counter = dict()
		for line in file:
			if not line.startswith('From') or line.startswith('From:'): continue
			words = line.split()
			address_sign_index = words[1].find('@')
			domain = words[1][address_sign_index + 1 :]
			domain_counter[domain] = domain_counter.get(domain, 0) + 1
		print(domain_counter)