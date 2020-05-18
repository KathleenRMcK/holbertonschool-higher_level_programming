#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    list_help = list(a_dictionary.items())

    for val in list_help:
        if value == val[1]:
            del a_dictionary[val[0]]
    return (a_dictionary)
