#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("0 arguments.")

    if len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, arg))
