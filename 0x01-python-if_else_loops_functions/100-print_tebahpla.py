#!/usr/bin/python3
for ahpla in reversed(range(97, 123)):
    if ahpla % 2 != 0:
        ahpla = ahpla - 32
    print("{}".format(chr(ahpla)), end="")
