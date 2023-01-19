#!/usr/bin/env python3
"""Count the number of times a letter is repeated in a string."""

def count(word, letter):
	"""Return the number of occurrences of a letter."""
	counter = 0
	for char in word:
		if char == letter:
			counter += 1
	return counter


if __name__ == '__main__':
	print(count('banana', 'a'))