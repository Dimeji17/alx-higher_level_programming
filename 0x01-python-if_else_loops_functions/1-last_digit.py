#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new_num = number % 10
if number < 0:
    if new_num == 0:
        print(f"Last digit of {number} is {new_num} and is 0")
    else:
        neg_num = 10 - new_num
        print(f"Last digit of {number} is {-neg_num}", end=" ")
        print("and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {new_num}", end=" ")
    if new_num > 5:
        print("and is greater than 5")
    elif new_num == 0:
        print("and is 0")
    elif new_num < 6:
        print("and is less than 6 and not 0")
