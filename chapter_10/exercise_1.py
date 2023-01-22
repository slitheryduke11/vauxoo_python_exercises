#!/usr/bin/env python3
"""Get the email address that has sent the most messages."""

def get_email_counter_ordered(file):
	"""Returns a list with emails and messages sent in descending order."""
	email_counter = dict()
	# Store emails and messages sent
	for line in file:
		if not line.startswith('From') or line.startswith('From:'): continue
		words = line.split()
		email_counter[words[1]] = email_counter.get(words[1], 0) + 1
	# Sort
	email_counter_ordered = list()
	for email, messages_sent in list(email_counter.items()):
		email_counter_ordered.append((messages_sent, email))
	email_counter_ordered.sort(reverse=True)
	return email_counter_ordered


if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		email_counter_ordered = get_email_counter_ordered(file)
		print(email_counter_ordered[0][1], email_counter_ordered[0][0])