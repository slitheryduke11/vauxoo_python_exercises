#!/usr/bin/env python3
"""Program that executes assignment statements and prints
their value and type."""

if __name__ == '__main__':
	width, height = 17, 12.0
	op_1 = width / 2 
	op_2 = width / 2.0
	op_3 = height / 3
	op_4 = 1 + 2 * 5
	print(op_1, type(op_1))
	print(op_2, type(op_2))
	print(op_3, type(op_3))
	print(op_4, type(op_4))