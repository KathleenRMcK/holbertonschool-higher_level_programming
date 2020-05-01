#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    for holder in dir(hidden_4):
        if holder[:2] != "__":
            print(holder)

