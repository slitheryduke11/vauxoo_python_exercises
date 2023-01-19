#!/usr/bin/env python3
"""Calculate a gross salary based on a number of hours and hourly rate."""

def calculate_salary(hours, hourly_rate):
	"""
    Return the salary calculated from the hours worked and
    the hourly rate.
    """
	return hours * hourly_rate


if __name__ == '__main__':
	try:
		hours = int(input('Enter hours: '))
		hourly_rate = float(input('Enter hourly rate: '))
	except ValueError as e: # Manage non-numeric inputs and display a message to the user
		print('Error, please enter a number')
	else:
		if hours > 40: # Hours worked over 40 are paid 1.5 times the hourly rate
			salary = calculate_salary(40, hourly_rate) + calculate_salary(hours - 40, hourly_rate * 1.5)
		else:
			salary = calculate_salary(hours, hourly_rate)
		print('Salary:', round(salary, 2))