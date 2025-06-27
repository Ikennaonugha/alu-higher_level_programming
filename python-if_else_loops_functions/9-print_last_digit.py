#!/usr/bin/python3
def print_last_digit(number):

    if number >= 0:
        return f"{number % 10}"
    else:
        return f"-{abs(number) % 10}"
    print("\n", end='')
