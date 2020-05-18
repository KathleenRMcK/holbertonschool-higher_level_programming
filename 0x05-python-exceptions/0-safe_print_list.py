#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    put = 0

    for help in range(x):
        try:
            print(my_list[help], end="")
            put += 1
        except:
            None
    print()
    return put
