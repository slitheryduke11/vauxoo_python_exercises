#!/usr/bin/env python3
"""Print all the characters line by line of a string in reverse order."""

if __name__ == '__main__':
	fruit = 'banana'
	index = len(fruit) - 1
	while index >= 0:
		print(fruit[index])
		index -= 1