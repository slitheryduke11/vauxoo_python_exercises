#!/usr/bin/env python3
"""Convert degrees Celsius to degrees Fahrenheit."""

if __name__ == '__main__':
	try:
		temperature_c = float(input('Enter temperature (°C): '))
	except ValueError as e:
		print('You must enter an integer/float for the temperature')
	else:
		temperature_f = temperature_c * (9 / 5) + 32
		print('Temperature (°F):', round(temperature_f, 2))