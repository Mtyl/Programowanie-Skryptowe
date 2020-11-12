#!/usr/bin/python3
#-*-coding: utf-8-*-
from . import lista
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
    for d in arr:
        if d != "":
            d = int(d)
            for i in range(len(lista)):
                if(d == lista[i][0]):
                    lista[i][1] += 1
                    break
                elif(d < lista[i][0]):
                    lista.insert(i, [d, 1])
                    break
            else:
                lista.append([d, 1])

def wypisz():
    out = ""
    for i in lista:
        out += "{}:{},".format(i[0], i[1])
    print(out)

if __name__ == "__main__":
    zapisz()
    wypisz()