#!/usr/bin/env python3
"""Store found words from a file."""

if __name__ == '__main__':
	filename = 'words.txt'
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		word_counter = dict()
		for line in file:
			words = line.split()
			for word in words:
				word_counter[word] = word_counter.get(word, 0) + 1
		print(word_counter)