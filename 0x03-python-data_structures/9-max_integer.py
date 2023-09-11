#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    l = my_list.copy()
    l.sort()
    return l[-1]
