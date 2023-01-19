#!/usr/bin/env python3
"""Calculate a gross salary based on a number of hours and hourly rate."""

if __name__ == '__main__':
	hours = int(input('Enter hours: '))
	hourly_rate = float(input('Enter hourly rate: '))
	print('Salary:', round(hours * hourly_rate, 2))