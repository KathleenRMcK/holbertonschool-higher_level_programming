#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    numsum = 0
    help = 0

    if not isinstance(romans, str) or romans is None:
        return 0

    while (help < len(roman_string)):
        temp_1 = romans.get(roman_string[help])
        if (help + 1 < len(roman_string)):
            temp_2 = romans.get(roman_string[help + 1])
            if (temp_1 >= temp_2):
                numsum = numsum + temp_1
                help = help + 1
            else:
                numsum = numsum + temp_2 - temp_1
                help = help + 2
        else:
            numsum = numsum + temp_1
            help + help + 1
    return numsum
