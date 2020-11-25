#!/usr/local/bin/python3


import math


def strong_num(number) -> str:
    """
    A Function that determines whether the input is a 'Strong' number.
    i.e. is the number that the sum of the factorial of its digits is
    equal to number itself.

    Parameters:

    number: int

    Returns:

    str

    """

    inter = []

    int_list = [int(i) for i in str(number)]
    for element in int_list:
        inter.append(math.factorial(element))
        print(sum(inter))

    if (sum(inter)) == number:
        return "STRONG!!!!"
    else:
        return "Not Strong !!"


print(strong_num(145))