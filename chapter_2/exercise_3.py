#!/usr/bin/env python3
"""Calculate a gross salary based on a number of hours and hourly rate."""

if __name__ == '__main__':
	try:
		hours = int(input('Enter hours: '))
		hourly_rate = float(input('Enter hourly rate: '))
	except ValueError as e:
		print('You must enter an integer for hours and an integer/float for the hourly rate.')
	else:
		print('Salary:', round(hours * hourly_rate, 2))