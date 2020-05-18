#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        vals = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        return (keys[vals.index(max(vals))])
