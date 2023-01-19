#!/usr/bin/env python3
"""Decrypt a message."""

if __name__ == '__main__':
	string = 'at7fh64-#-$_)u(fy6AHe-WA3eLrna!at7fh64-#-$_)u(fy6A'
	clean_string = string.strip('at7fh64-#-$_)u(fy6A')
	decrypted_string = clean_string.replace('-WA3e', 'llo, ').replace('r', 'u')
	print(decrypted_string)