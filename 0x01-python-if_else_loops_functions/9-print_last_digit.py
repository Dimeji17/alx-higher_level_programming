#!/usr/bin/python3
def print_last_digit(number):
    last_dig = number % 10
    if number < 0:
        neg_last_dig = 10 - last_dig
        print("{}".format(neg_last_dig), end="")
        return ("{}".format(neg_last_dig))
    else:
        print("{}".format(last_dig),end="")
        return ("{}".format(last_dig))
