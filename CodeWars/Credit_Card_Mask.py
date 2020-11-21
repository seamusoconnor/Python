# return masked string
def maskify(cc):
    if len(cc) <= 3:
        return cc
    new_string = ''
    last = cc[-4:]
    for x in range(0, len(cc)-4):
        new_string = new_string+'#'
    new_string = new_string + last

    return new_string

print(maskify("dlfjlskdfjlsabcd"))