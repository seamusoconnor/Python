def open_or_senior(data):
    """
    Function that takes in a list of lists [[age, handicap],[]]
    returns a list of strings depending on age and handicap

    Parameters:

    input: list of lists. the inner list contains two integers,
    age and handicap

    Returns:

    a list of strings
    """
    output = []
    for person in data:
        age = person[0]
        handicap = person[1]

        print(handicap)
        if age >= 55 and handicap > 7:
            output.append("Senior")
        else:
            output.append("Open")
    return output


print(open_or_senior([[56, 6], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

