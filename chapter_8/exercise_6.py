#!/usr/bin/env python3
"""Get minimum and maximum of a set of numbers."""

if __name__ == '__main__':
	numbers = list()
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
			numbers.append(number)
	print('Max: ', max(numbers))
	print('Min: ', min(numbers))