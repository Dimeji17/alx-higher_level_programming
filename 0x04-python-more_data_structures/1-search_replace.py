#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = my_list[:]
    for num in range(len(copy)):
        if copy[num] == search:
            copy[num] = replace
        else:
            copy[num] = copy[num]
    return copy
