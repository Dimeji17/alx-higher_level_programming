#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
        add = sum(new_list)
    return add
