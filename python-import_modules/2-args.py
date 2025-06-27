#!/usr/bin/python3
import sys

if __name__ == "__main__":
    
    if len(sys.argv) == 0:
        print("{} arguments.".format(len(sys.argv)))
    elif len(sys.argv) == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[0]))
    else:
        print("{} arguments:".format(len(sys.argv)))
        for i, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(i + 1, arg))
