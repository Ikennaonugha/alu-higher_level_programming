#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string_number = str(number)
last_digit = string_number[-1]
int_last_digit = int(last_digit)
if number < 0 :
    int_last_digit *= -1

def checker(num):
    if num > 5 :
        return "and is greater than 5"
    elif num == 0:
        return "and is 0"
    elif num < 6 and num != 0 :
        return "and is less than 6 and not 0"

message = checker(int_last_digit)
print(f"Last digit of {number} is {int_last_digit} {message}")
