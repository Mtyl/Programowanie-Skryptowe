#!/usr/bin/python3
import unittest
from DeanerySystem.term import Term
from DeanerySystem.day import Day, nthDayFrom
from DeanerySystem.lesson import Lesson
from DeanerySystem.timetable import Timetable1, Action, Observer
timex = Timetable1()

class DayTest(unittest.TestCase):

    def test_nth(self):
        self.assertEqual(nthDayFrom(1, Day.SAT), Day.SUN)
        self.assertEqual(nthDayFrom(2, Day.SAT), Day.MON)
        self.assertEqual(nthDayFrom(-1, Day.TUE), Day.MON)
        self.assertEqual(nthDayFrom(-2, Day.TUE), Day.SUN)

    def test_difference(self):
        self.assertEqual(Day.MON.difference(Day.TUE), 1)
        self.assertEqual(Day.MON.difference(Day.SUN), -1)
        self.assertEqual(Day.SUN.difference(Day.MON), 1)
        self.assertEqual(Day.SUN.difference(Day.SAT), -1)

class TermTest(unittest.TestCase):
    
    def test_str(self):
        term1 = Term(9, 45, Day.TUE)
        term2 = Term(10, 15, Day.WED)
        term3 = Term(12, 45, Day.FRI)
        self.assertEqual(str(term1),"9:45 [90]")
        self.assertEqual(str(term2),"10:15 [90]")
        self.assertEqual(str(term3),"12:45 [90]")
     
    def test_timeCompare(self):
        term1 = Term(9, 45, Day.TUE)
        term2 = Term(10, 15, Day.WED)
        term3 = Term(12, 45, Day.FRI)
        self.assertTrue(term1.earlierThan(term2))
        self.assertTrue(term2.earlierThan(term3))
        self.assertTrue(term1.earlierThan(term3))
        self.assertFalse(term1.laterThan(term2))
        self.assertFalse(term2.laterThan(term3))
        self.assertFalse(term1.laterThan(term3))
        self.assertFalse(term1.equals(term2))
        self.assertTrue(term1.equals(term1))

    def test_int(self):
        term1 = Term(9, 45, Day.TUE)
        term2 = Term.fromInt(int(term1))
        self.assertTrue(term1.equals(term2))
        self.assertEqual(str(term2),"9:45 [90]")
        term1.reInt(int(term2))
        self.assertEqual(str(term1),"9:45 [90]")
        term1 = Term(10, 15, Day.WED)
        term2 = Term.fromInt(int(term1))
        self.assertTrue(term1.equals(Term.fromInt(int(term1))))
        self.assertEqual(str(term2),"10:15 [90]")
        term1.reInt(int(term2))
        self.assertEqual(str(term1),"10:15 [90]")
    
    def test_new(self):
        term1 = Term(9, 45, Day.TUE)
        term2 = Term(10, 15, Day.WED)
        term = term1.minuteDifference(term2)
        self.assertEqual(str(term), "9:45 [30]")
        term = term1.endTime()
        self.assertEqual(str(term), "11:15 [90]")
        term = term2.endTime()
        self.assertEqual(str(term), "11:45 [90]")

    def test_init(self):
        term1 = Term(9, 45, Day.WED)
        self.assertEqual(str(term1), "9:45 [90]")
        term1 = Term(9, 45, 90)
        self.assertEqual(str(term1), "9:45 [90]")
        term1 = Term(10, 30, 30, Day.TUE)
        self.assertEqual(str(term1), "10:30 [30]")
    
    def test_operator(self):
        term1 = Term(8, 30)
        term2 = Term(9, 45, 30)
        term3 = Term(9, 45, 90)
        self.assertTrue(term1 < term2)
        self.assertTrue(term1 <= term2)
        self.assertFalse(term1 > term2)
        self.assertFalse(term1 >= term2)
        self.assertFalse(term2 == term3)
        self.assertTrue(term2 == term2)
        term2 = term3 - term1
        self.assertEqual(str(term2), "8:30 [165]")

class LessonTest(unittest.TestCase):
    def test_str(self):
        time = Timetable1()
        lesson = Lesson(time, Term(9, 35, Day.TUE), "Programowanie skryptowe", "Stanisław Polak", 2)
        self.assertEqual(str(lesson), """Programowanie skryptowe (Wtorek 9:35-11:05)
Drugi rok studiów stacjonarnych
Prowadzący: Stanisław Polak
""")    

    def test_moveDay(self):
        time = Timetable1()
        time1 = Timetable1()
        lesson = Lesson(time, Term(8, 30), "Test", "Tester", 1)
        self.assertFalse(lesson.earlierDay())
        self.assertTrue(lesson.laterDay())
        self.assertEqual(str(lesson), str(Lesson(time1, Term(8, 30, Day.TUE), "Test", "Tester", 1)) )
        self.assertTrue(lesson.earlierDay())
        lesson = Lesson(time, Term(8, 30, Day.SUN), "Test", "Tester", 2)
        self.assertFalse(lesson.laterDay())
        self.assertTrue(lesson.earlierDay())
        self.assertEqual(str(lesson), str(Lesson(time1, Term(8, 30, Day.SAT), "Test", "Tester", 2)) )

    def test_moveTime(self):
        time = Timetable1()
        time1 = Timetable1()
        lesson = Lesson(time, Term(8, 30), "Test", "Tester", 1)
        self.assertFalse(lesson.earlierTime())
        self.assertTrue(lesson.laterTime())
        self.assertEqual(str(lesson), str(Lesson(time1, Term(10, 00, Day.MON), "Test", "Tester", 1)) )
        self.assertTrue(lesson.earlierTime())
        lesson = Lesson(time, Term(18, 30, Day.SUN), "Test", "Tester", 2)
        self.assertFalse(lesson.laterTime())
        self.assertTrue(lesson.earlierTime())
        self.assertEqual(str(lesson), str(Lesson(time1, Term(17, 00, Day.SUN), "Test", "Tester", 2)) )
        lesson = Lesson(time, Term(17, 00, Day.FRI), "Test", "Tester", 2)
        self.assertFalse(lesson.earlierTime())
        self.assertTrue(lesson.laterTime())
        self.assertEqual(str(lesson), str(Lesson(time1, Term(18, 30, Day.FRI), "Test", "Tester", 2)) )

class Timetable1Test(unittest.TestCase):
    def test_timetable(self):
        exceptCatcher = False
        lesson = Lesson(timex, Term(8, 00), "Test", "Tester", 1)
        self.assertTrue(timex.put(lesson))
        try:
            timex.put(lesson)
        except ValueError:
            exceptCatcher = True
        self.assertTrue(exceptCatcher)
        exceptCatcher = False
        self.assertEqual(timex.get(lesson.term), lesson)
        try:
            actList = timex.parse(["d-", "dd+", "d+d", "d+"])
        except ValueError:
            exceptCatcher = True
        actList = timex.parse(["d-", "d+"])
        self.assertTrue(exceptCatcher)
        self.assertEqual(actList, [Action.DAY_EARLIER, Action.DAY_LATER])
        timex.perform(actList)
        self.assertTrue(timex.busy(lesson.term))
        self.assertEqual(lesson.term.day, Day.TUE)
        lesson2 = Lesson(timex, Term(9, 30), "Test2", "Tester2", 1)
        timex.put(lesson2)
        actList = timex.parse(["d-", "d+", "t+", "t-"])
        timex.perform(actList)
        self.assertEqual(int(lesson.term), (9*60+30))
        self.assertEqual(int(lesson2.term), (1440+8*60))
        lesson3 = Lesson(timex, Term(9,30), "Replaced", "Replacer", 1)
        timex - lesson
        try:
            timex - lesson
            
        except ValueError as e:
            self.assertEqual(e, "ERROR NOTHING TO REMOVE")
        
        self.assertEqual(timex.get(lesson3.term), None)
        timex + lesson
        self.assertEqual(timex.get(lesson3.term), lesson)
        timex + lesson3
        self.assertEqual(timex.get(lesson3.term), lesson3)


if __name__ == '__main__':
    unittest.main(exit=False)
    print(timex)
    