#!/usr/bin/python3
#-*-coding: utf-8-*-
import re

while True:
    inp = input()
    while(inp != ''):
        cur = re.match('^\d+', inp)
        if cur:
            inp = inp[cur.end():]
            print("Liczba:" + cur.group(0))
        cur = re.match('^\D+', inp)
        if cur:
            inp = inp[cur.end():]
            print("Wyraz:" + cur.group(0))
