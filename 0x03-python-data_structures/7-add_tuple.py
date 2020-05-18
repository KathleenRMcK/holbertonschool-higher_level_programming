#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuple_1 = (0, 0)
    tuple_2 = ()

    if len(tuple_a) < 2:
        tuple_a = tuple_a + tuple_1
    if len(tuple_b) < 2:
        tuple_b = tuple_b + tuple_1

    tuple_2 = tuple(a + b for a, b in zip(tuple_a[0:2], tuple_b[0:2]))
    return (tuple_2)
