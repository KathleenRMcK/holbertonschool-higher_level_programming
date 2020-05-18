#!/usr/bin/python3
def weight_average(my_list=[]):

    score = 0
    weight = 0

    if my_list:
        for listy in my_list:
            score = score + (listy[0] * listy[1])
            weight = weight + listy[1]
        return (score/weight)
    return 0
