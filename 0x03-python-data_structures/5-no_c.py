#!/usr/bin/python3
def no_c(my_string):

    str_help = ""
    for parser in my_string:
        if parser not in "Cc":
            str_help += parser
    return str_help
