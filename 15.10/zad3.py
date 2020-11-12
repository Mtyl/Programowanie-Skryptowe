#!/usr/bin/python3
#-*-coding: utf-8-*-
from sys import argv
import getopt

if(len(argv) != 3):
    print("Syntax: ./zad3.py --moduł=[lista,slownik] [data] ")
else:
    opt, arg = getopt.getopt(argv[1:], "", "moduł=")
    if(opt == []):
        print("Syntax: ./zad3.py --moduł=[lista,slownik] [data] ")
        exit()
    if(opt[0][1] ==  "lista"):
        from typy import listy
        listy.zapisz(arg[0])
        listy.wypisz()
    elif(opt[0][1] ==  "slownik"):
        from typy import slowniki
        slowniki.zapisz(arg[0])
        slowniki.wypisz()
    else:
        print("Syntax: ./zad3.py --moduł=[lista,slownik] [data]")