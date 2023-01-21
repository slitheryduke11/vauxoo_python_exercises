#!/usr/bin/env python3
"""Get the email address that has sent the most messages."""

if __name__ == '__main__':
	filename = input('Enter filename: ')
	try:
		file = open(filename)
	except Exception as e:
		print('Could not open file \'' + filename + '\'')
	else:
		email_counter = dict()
		for line in file:
			if not line.startswith('From') or line.startswith('From:'): continue
			words = line.split()
			email_counter[words[1]] = email_counter.get(words[1], 0) + 1
		most_repeated_email = None
		for email in email_counter:
			if most_repeated_email is None \
			or email_counter[email] > email_counter[most_repeated_email]:
				most_repeated_email = email
		print(most_repeated_email, email_counter[most_repeated_email])