#!/usr/local/bin/python3

def next_happy_year(year):

    year+=1
    while 1000 <= year <= 9999:
        int_list = [int(i) for i in str(year)]
        se = set(int_list)
        if len(se) == len(int_list):
            return year

        else:
            year+=1



print(next_happy_year(1001))

