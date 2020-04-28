#!/usr/bin/python3
for nums in range(100):
    if nums != 99:
        print("{0:02d}, ".format(nums), end="")
    elif nums == 99:
        print("{0:02d}".format(nums), end="\n")
