#!/usr/bin/python3
#-*-coding: utf-8-*-

from . import slownik 
import re
from sys import argv as argv

def zapisz(inputstr=""):
    if __name__ == "__main__":
        if(len(argv) < 2):
            return
        string = argv[1]
    else:
        string = inputstr
    arr = re.findall('\d', string)
    for i in arr:
        if (i != ""):
            if i in slownik:
                slownik[i] += 1
            else:
                slownik[i] = 1


def wypisz():
    out = ""
    for i in sorted(slownik):
        out += "{}:{},".format(i, slownik[i])
    print(out)

if __name__ == "__main__":
    zapisz()
    wypisz()