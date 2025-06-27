#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("0")
    elif len(sys.argv) > 1:
        arg_list = []
        for i in sys.argv[1:]:
            num = int(i)
            arg_list.append(num)
        total = sum(arg_list)
        print(total)
