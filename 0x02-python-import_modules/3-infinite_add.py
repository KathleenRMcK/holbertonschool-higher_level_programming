#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_sum = 0

    for holder in argv[1:]:
        num_sum += int(holder)

    print("{:d}".format(num_sum))
