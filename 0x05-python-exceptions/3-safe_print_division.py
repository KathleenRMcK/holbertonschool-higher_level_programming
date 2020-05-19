#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num_res = a / b
    except:
        num_res = None
    finally:
        print("Inside result: {}".format(num_res))
    return num_res
