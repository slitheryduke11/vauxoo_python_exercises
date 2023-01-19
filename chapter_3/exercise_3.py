#!/usr/bin/env python3
"""Display a grade based on a score."""

if __name__ == '__main__':
	try:
		score = float(input('Enter score (0.0 - 1.0): '))
	except ValueError as e: # Manage non-numeric inputs and display a message to the user
		message = 'Wrong score'
	else:
		if score <= 0.0 or score >= 1.0: # Invalid score
			message = 'Wrong score'
		elif score >= 0.9:
			message = 'Outstanding'
		elif score >= 0.8:
			message = 'Remarkable'
		elif score >= 0.7:
			message = 'Good'
		elif score >= 0.6:
			message = 'Enough'
		elif score < 0.6:
			message = 'Insufficient'
	finally:
		print(message)
