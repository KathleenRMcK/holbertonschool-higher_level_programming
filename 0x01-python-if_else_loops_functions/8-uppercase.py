#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) > 96 and ord(upper) < 123:
            temp = ord(upper) - 32
        else:
            temp = ord(upper)
        print("{:c}".format(temp), end="")
    else:
        print()
