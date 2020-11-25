#!/usr/local/bin/python3


def next_happy_year(year) -> int:
    """
    A function that takes a positive integer between 1000 and 9000
    and returns the next 'Heppy Year' (no duplicate numbers)

    Parameters:
    year : int

    Returns:
    year : int
    """
    year += 1
    while 1000 <= year <= 9999:
        int_list = [int(i) for i in str(year)]
        se = set(int_list)
        if len(se) == len(int_list):
            return year

        else:
            year += 1


print(next_happy_year(1001))
