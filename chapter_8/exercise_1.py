#!/usr/bin/env python3
"""Remove items from a list and create a new list."""

def cut(t):
	del t[0]
	del t[-1]


def medium(t):
	return t[1:-1]


if __name__ == '__main__':
	elements = [1, 2, 3, 4, 5]
	print('Original list:', elements)
	print('Call to function \'cut\':', cut(elements))
	print('Call to function \'medium\':', medium(elements))