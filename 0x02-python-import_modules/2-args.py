#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    temp = 1

    if len(argv) - temp > 1:
        print("{:d} arguments:".format(len(argv) - temp))

    elif len(argv) - temp == 1:
        print("1 argument:")

    else:
        print("0 arguments.")

for holder in argv[1:]:
    print("{:d}: {:s}".format(temp, holder))
    temp += 1
