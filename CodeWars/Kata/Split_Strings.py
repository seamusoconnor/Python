#!/usr/local/bin/python3
def solution(s) -> list:
    """
    splits string into pairs of two characters. If the string contains an odd
    number of characters then it should replace the missing second character
    of the final pair with an underscore ('_').

    Parameters:

    s : str

    Returns:

    lister: list

    """
    lister = []
    if (len(s) % 2) == 0:
        pass
    else:
        s = s + "_"

    for x in range(0, len(s), 2):
        lister.append(s[x] + s[x + 1])
    return lister


print(solution("abdxc"))
