#!/usr/bin/python3
'''
Function prints Squares
Usage:
    print_square(size_number)
'''


def print_square(size):
    '''
    Function prints a square with # character
    '''

    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
