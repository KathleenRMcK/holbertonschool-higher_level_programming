#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_help = []
    for parse in my_list:
        if parse == search:
            list_help.append(replace)
        else:
            list_help.append(parse)
    return list_help
