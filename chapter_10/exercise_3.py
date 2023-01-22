#!/usr/bin/env python3
"""Get the repetitions of the letters in descending order."""

import string

letter_counter = {
	'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0,
	'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0,
	's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
}


def get_letter_counter_ordered(file):
	"""Returns a list with letters and their repetitions in descending order."""
	# Store letters and their repetitions
	for line in file:
		line = line.translate(line.maketrans('', '', string.punctuation)).lower()
		for letter in line:
			if letter not in letter_counter: continue
			letter_counter[letter] += 1
	# Sort
	letter_counter_ordered = list()
	for letter, repetitions in list(letter_counter.items()):
		letter_counter_ordered.append((repetitions, letter))
	letter_counter_ordered.sort(reverse=True)
	return letter_counter_ordered


def main():
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		letter_counter_ordered = get_letter_counter_ordered(file)
		for repetitions, letter in letter_counter_ordered:
			print(letter, repetitions)


if __name__ == '__main__':
	main()