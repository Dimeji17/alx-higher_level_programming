#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    duplicate = my_list.copy()
    if ((idx < 0) or (idx >= len(my_list))):
        return duplicate
    else:
        duplicate[idx] = element
        return duplicate
