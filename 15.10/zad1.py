#!/usr/bin/python3
#-*-coding: utf-8-*-

lancuch1 = """Litwo! Ojczyzno moja! ty jesteś jak zdrowie:
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.
"""

lancuch2 = """Właśnie dwukonną bryką wjechał młody panek
I obiegłszy dziedziniec zawrócił przed ganek.
Wysiadł z powozu; konie porzucone same,
Szczypiąc trawę ciągnęły powoli pod bramę.
"""

print((lancuch1+lancuch2)*3)

lancuch = "Powrót panicza — Spotkanie się pierwsze w pokoiku, drugie u stołu"
print(lancuch[0])
print(lancuch[:2])
print(lancuch[2:])
print(lancuch[-2])
print(lancuch[-3:])
print(lancuch[1::2])

#lancuch[0] = 'a'
#TypeError: 'str' object does not support item assignment