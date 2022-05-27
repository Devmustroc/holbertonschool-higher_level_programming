#!/usr/bin/python3
"""
*****
****
***
**
*
"""
L = int(input("please insert your line number : "))
for i in range(1, L+ 1):
    for j in range(L - i + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
