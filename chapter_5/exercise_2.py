#!/usr/bin/env python3
"""Get total, quantity, minimum and maximum of a set of numbers."""

if __name__ == '__main__':
	total, quantity = 0, 0
	min_n, max_n = None, None
	while True:
		user_input = input('Enter a number (\'end\' to finish): ')
		if user_input == 'end':
			break
		try:
			number = int(user_input)
		except ValueError as e: # Manage non-numeric inputs and display a message to the user
			print('Wrong data')
			continue
		else:
			total += number
			quantity += 1
			if min_n is None or number < min_n:
				min_n = number
			if max_n is None or number > max_n:
				max_n = number
	print('Total: ', total, ', quantity: ', quantity, ', min: ', min_n, ', max: ', max_n, sep='')