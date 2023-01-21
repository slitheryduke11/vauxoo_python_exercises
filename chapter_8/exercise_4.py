#!/usr/bin/env python3
"""Print unique words of a file in alphabetical order."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	unique_words = list()
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			words = line.split()
			for word in words:
				if word not in unique_words:
					unique_words.append(word)
		unique_words.sort()
		print(unique_words)