#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    """ adds all unique integers in a list (only once for each integer)

    Keyword arguments:
    argument -- list
    Return: sum of the list
    """
    uniq_list = [*{el for el in my_list}]
    sum = reduce((lambda x, y: x + y), uniq_list)
    return sum
