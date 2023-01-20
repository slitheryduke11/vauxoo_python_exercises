#!/usr/bin/env python3
"""Print the spam confidence average in a file."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	total, counter = 0, 0
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		for line in file:
			if line.startswith('X-DSPAM-Confidence:'):
				colon_index = line.find(':')
				float_number = float(line[colon_index + 1 :])
				total += float_number
				counter += 1
		print('Spam confidence average:', total / counter)