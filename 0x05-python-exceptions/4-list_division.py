#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    listy = []

    for help in range(list_length):
        try:
            holder = my_list_1[help] / my_list_2[help]

        except TypeError:
            print("wrong type")
            holder = 0

        except ZeroDivisionError:
            print("division by 0")
            holder = 0

        except IndexError:
            print("out of range")
            holder = 0

        finally:
            listy.append(holder)
    return listy
