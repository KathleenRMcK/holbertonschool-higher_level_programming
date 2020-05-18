#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    list_help = []
    if my_list:
        for parse in my_list:
            if parse % 2 == 0:
                list_help.append(True)
            else:
                list_help.append(False)
        return (list_help)
