#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list."""
    new_list = my_list.copy()
    for i, el in enumerate(new_list):
        if el == search:
            new_list[i] = replace 
    return new_list