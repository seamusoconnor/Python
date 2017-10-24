from sys import argv



def main(a, b):
    a = int(a); b = int(b)

    square = sqr(a,b);print ('the multiplication of {} and {} is: ').format (a,b), square

    plus = plu(a,b);print ('The addition of {} and {} is: ').format (a,b), plus

    division = div(a,b);print ('The division of {} and {} is: ').format (a,b), division

def sqr(a,b):
    square = a*b    
    return square

def plu(a,b):
    plus = a+b
    return plus

def div(a,b):
    division = a/b
    return division

script, a, b = argv

if __name__ == '__main__':
    main(*argv[1:])
