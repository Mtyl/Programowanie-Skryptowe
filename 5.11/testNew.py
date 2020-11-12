#!/usr/bin/python3
import unittest
from DeanerySystem.term import Term, BasicTerm, Break
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable2, Action, Observer
timex = None

class Timetable2Test(unittest.TestCase):
    def test_timetable(self):
        exceptCatcher = False
        breaks = [Break(9, 30, 5), Break(11, 5, 10), Break(12, 45, 5), Break(14, 20, 20), Break(16, 10, 5), Break(17, 45, 5), Break(19, 20, 5)]
        self.assertTrue(breaks[0].getTerm().isEq(BasicTerm(9, 30, 5)))
        self.assertTrue(breaks[1].getTerm().isEq(BasicTerm(11, 5, 10)))
        self.assertEqual(str(breaks[0]), "Przerwa")
        global timex 
        timex = Timetable2(breaks)
        lessons = [Lesson(timex, Term(8,0), "Kryptografia", "test", 1), 
        Lesson(timex, Term(8,0,90,Day.TUE), "Sieci", "test", 1), 
        Lesson(timex, Term(9,35,90,Day.FRI), "Fizyka Laby", "test", 1)]
        actList = []
        for i in lessons:
            timex.put(i)
            i.attach(Observer())
        try:
            timex.put(lessons[1])
        except ValueError:
            exceptCatcher = True
        self.assertTrue(exceptCatcher)
        exceptCatcher = False
        try:
            actList = timex.parse(["d-", "dd+", "d+d", "d+"])
        except ValueError as e:
            exceptCatcher = True
            self.assertEqual("Translation " + "dd+" + " is incorrect", str(e) )
        actList = timex.parse(["t+", "d+", "t-", "d+", "t+"])
        timex.perform(actList)
        self.assertTrue(exceptCatcher)
        self.assertEqual(lessons[0].term.day, Day.TUE)
        self.assertEqual(lessons[0].term.hour, 8)
        self.assertEqual(lessons[1].term.hour, 8)
        self.assertEqual(lessons[1].term.day, Day.WED)
        Lesson.skipBreaks = True
        timex.perform(actList)
        self.assertEqual(lessons[0].term.day, Day.WED)
        self.assertEqual(lessons[0].term.hour, 9)
        self.assertEqual(lessons[1].term.hour, 9)
        self.assertEqual(lessons[1].term.day, Day.THU)
        self.assertEqual(lessons[2].term.hour, 8)
    
    def test_exception(self):
        term = Term(12,34)
        buf = 0
        err = 27
        try:
            term.hour = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)
        err = 63
        try:
            term.minute = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)
        err = 1234
        try:
            term.duration = err
        except ValueError as e:
            buf = int(str(e))
        self.assertEqual(buf, err)
 
if __name__ == '__main__':
    unittest.main(exit=False)
    print(timex)
