#!/usr/bin/python3
def print_last_digit(number):

    if number >= 0:
        return "{}".format(number % 10)
    else:
        return "-{}".format(abs(number) % 10)
    print("\n", end='')
