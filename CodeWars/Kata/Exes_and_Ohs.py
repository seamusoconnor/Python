#!/usr/local/bin/python3
def xo(s):
    """
    Function that compares 'x' and 'o' from input
    and if number is same, returns True, else False

    Parameters:

    s : str

    Returns:

    Bool
    
    """
    low = s.lower()
    if (low.count('x')) == (low.count('o')):
        return True
    else:
        return False

print(xo("xxoOa"))
