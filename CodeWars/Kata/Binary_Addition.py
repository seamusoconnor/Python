#!/usr/local/bin/python3

def add_binary(a,b):
    """
    Function that adds 2 integers and
    returns the binary representation as
    a string, removing the '0b' tag

    Parameters:

    Two comma separated integers

    Returns:

    str


    """

    return str(bin(a+b))[2:]

print(add_binary(5,6))