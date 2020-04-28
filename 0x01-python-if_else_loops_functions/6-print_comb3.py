#!/usr/bin/python3
for combo in range(99):
    if combo / 10 < combo % 10 and combo != 89:
        print("{:02d},".format(combo), end=" ")
    elif combo == 89:
        print(combo)
