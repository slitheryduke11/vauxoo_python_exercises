#!/usr/bin/env python3
"""Get total, quantity and mean of a set of numbers."""

if __name__ == '__main__':
	total, quantity = 0, 0
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
	print('Total: ', total, ', quantity: ', quantity, ', mean: ', total / quantity, sep='')