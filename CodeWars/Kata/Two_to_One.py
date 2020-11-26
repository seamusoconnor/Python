#!/usr/local/bin/python3
def longest(s1, s2):
    """
    Function that takes two strings, and returns a
    string with only unique letters, and sorted

    Parameters:

    s1: str
    s2: str

    Returns

    str
    """
    return ("").join(sorted(set(s1 + s2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

print(longest(a, b))