#!/usr/bin/python3
import unittest
from DeanerySystem.term import Term, Break
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1, Timetable2, Action, Observer

Lesson.skipBreaks = True
x = Timetable2([Break(9, 30, 5), Break(11, 5, 10), Break(12, 45, 5), Break(14, 20, 20), Break(16, 10, 5), Break(17, 45, 5), Break(19, 20, 5)])
#for i in x.validTerms:
#    print(i)
lesson = [Lesson(x, Term(8,0), "Kryptografia", "test", 1), Lesson(x, Term(8,0,90,Day.TUE), "Sieci lokalne", "test", 1), Lesson(x, Term(9,35,90,Day.FRI), "Fizyka lab.", "test", 1)]
for i in lesson:
    x.put(i)
    i.attach(Observer())

while True:
    print(x)
    inp = input()
    inp = inp.split(" ")
    try:
      actions = x.parse(inp)
    except ValueError:
      exit()
    x.perform(actions)
