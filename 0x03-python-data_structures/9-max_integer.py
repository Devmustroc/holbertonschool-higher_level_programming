#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        val_max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > val_max:
                val_max = my_list[i]
        return val_max
    return None
