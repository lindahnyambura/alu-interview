#!/usr/bin/python3
'''Minimum Operations'''

def min_operations(n: int, result: int = 0) -> int:
    '''
    Returns the minimum number of operations needed to result in exactly n 'H' characters in the file.
    '''
    if n <= 1:
        return 0
    elif n <= 3:
        return n

    common_factor = get_hcf(n)
    return min_operations(common_factor) + (n // common_factor)

def get_hcf(num: int) -> int:
    '''
    Returns the highest common factor (HCF) of a given number.
    '''
    if num % 2 == 0:
        return num // 2
    for i in range(num // 2, 0, -1):
        if num % i == 0:
            return i


