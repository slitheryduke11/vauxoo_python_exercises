#!/usr/bin/env python3
"""Generate random numbers from different parameters."""

import random

if __name__ == '__main__':
	t = [1, 2, 3]
	print(random.randint(5, 10)) # From a range
	print(random.choice(t)) # From a list