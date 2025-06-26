#!/usr/bin/python3
for i in range(10):
    print(f"0{i}, ",end='')
print(*range(10,100), sep=', ', end='\n')
