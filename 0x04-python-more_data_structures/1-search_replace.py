#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """ replaces all occurrences of an element by another in a new list."""
    copy_list = my_list.copy()
    searchIndex = copy_list.index(search)
    copy_list.insert(searchIndex, replace)
    return copy_list