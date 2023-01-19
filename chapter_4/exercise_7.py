#!/usr/bin/env python3
"""Display a grade based on a score."""

def calculate_grade(score):
	"""Return the grade calculated from the score."""
	if score <= 0.0 or score >= 1.0: # Invalid score
		grade = 'Wrong score'
	elif score >= 0.9:
		grade = 'Outstanding'
	elif score >= 0.8:
		grade = 'Remarkable'
	elif score >= 0.7:
		grade = 'Good'
	elif score >= 0.6:
		grade = 'Enough'
	elif score < 0.6:
		grade = 'Insufficient'
	return grade


if __name__ == '__main__':
	try:
		score = float(input('Enter score (0.0 - 1.0): '))
	except ValueError as e: # Manage non-numeric inputs and display a grade to the user
		grade = 'Wrong score'
	else:
		grade = calculate_grade(score)
	finally:
		print(grade)