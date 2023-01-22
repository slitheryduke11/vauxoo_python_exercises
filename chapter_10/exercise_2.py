#!/usr/bin/env python3
"""Get the hours in ascending order and their repetitions."""

def get_hour_counter_ordered(file):
	"""Returns a list with hours and their repetitions in ascending order."""
	hour_counter = dict()
	# Store hours and their repetitions
	for line in file:
		if not line.startswith('From') or line.startswith('From:'): continue
		words = line.split()
		time_chain = words[5]
		hour = time_chain.split(':')[0]
		hour_counter[hour] = hour_counter.get(hour, 0) + 1
	# Sort
	hour_counter_ordered = list()
	for hour, repetitions in list(hour_counter.items()):
		hour_counter_ordered.append((hour, repetitions))
	hour_counter_ordered.sort()
	return hour_counter_ordered


def main():
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		hour_counter_ordered = get_hour_counter_ordered(file)
		for hour, repetitions in hour_counter_ordered:
			print(hour, repetitions)


if __name__ == '__main__':
	main()