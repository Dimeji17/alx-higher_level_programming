#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in range(len(my_list)):
        if type(x) == int:
            print("{}".format(len(my_list[x])))
