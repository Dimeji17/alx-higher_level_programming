#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
        elif my_list == []:
            new_list.append(0)
        add = sum(new_list)
    return add
