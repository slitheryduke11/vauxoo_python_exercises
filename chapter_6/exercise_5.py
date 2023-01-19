#!/usr/bin/env python3
"""Get the float number of a string."""

if __name__ == '__main__':
	string = 'X-DSPAM-Confidence:0.8475'
	colon_index = string.find(':')
	float_number = float(string[colon_index + 1 :])
	print(float_number, type(float_number))