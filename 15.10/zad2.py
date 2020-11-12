#!/usr/bin/python3
#-*-coding: utf-8-*-
import re
pos = 0
reg = re.compile(r'(.)\1{4,}')
reg2 = re.compile(r'([()%])\1*')
s = ""
x = input()
while (x != ""):
    s += x + "\n"
    x = input() 

s = s[:(len(s)-2)]    

x = reg2.search(s)
while(x):
    match = ""
    if(x.group()[0] == '('):
        sub = "%28"
        match = r'\({' + str(x.end() - x.start()) + '}'
    if(x.group()[0] == ')'):
        sub = "%29"
        match = r'\){' + str(x.end() - x.start()) + '}'
    if(x.group()[0] == '%'):
        sub = "%25"
        match = x.group()
    rep = (sub + '(' + (str(x.end() - x.start())) + ')')  
    s = s[:pos] + re.sub(match, rep, s[pos:], 1)
    pos += x.start()+len(rep)
    x = reg2.search(s[pos:])

x = reg.search(s)
while(x):
    rep = (x.group()[0] + '(' + (str(x.end() - x.start())) + ')')
    s = re.sub(x.group(), rep, s)
    x = reg.search(s)

print(s)