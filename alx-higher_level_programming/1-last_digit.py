#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    di = number % 10
else:
    di = number % -10
if di == 0:
    print(f"Last digit of {number:d} is {di:d} and is 0")
elif di > 5:
    print(f"Last digit of {number:d} is {di:d} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {di:d} and is less than 6 and not 0")
