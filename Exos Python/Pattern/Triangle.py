#!/usr/bin/python3

"""
*
**
***                '''Ttainlge in python'''
****
*****
"""
L = int(input("Saisir le nombre de ligne: "))
for i in range(1, L + 1):
    for j in range (i):
        print("*", end="")
    print()
