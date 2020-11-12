#!/usr/bin/python3
import sympy
import sys
for x in sys.argv:
    #x = input()
    #if x == "end":
    #    break
    try:
        x = int(x)
    except:
        continue
    
    if sympy.isprime(x):
        print("{} is a prime!".format(x))

