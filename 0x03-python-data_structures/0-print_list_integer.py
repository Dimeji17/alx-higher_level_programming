#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
        if type(x) == int:
            print("{}".format(x))
