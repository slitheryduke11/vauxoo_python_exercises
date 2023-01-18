#!/usr/bin/env python3
"""Program that prompts the user for the number of hours and
the hourly rate to calculate gross pay."""

if __name__ == '__main__':
	try:
		hours = int(input('Enter hours: '))
		hourly_rate = float(input('Enter hourly rate: '))
	except ValueError as e:
		print('You must enter an integer for hours and an integer/float for the hourly rate.')
	else:
		print('Salary:', round(hours * hourly_rate, 2))