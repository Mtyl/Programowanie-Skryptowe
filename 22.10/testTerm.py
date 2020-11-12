#!/usr/bin/python3
import unittest
from DeanerySystem.term import Term
from DeanerySystem.day import Day

class MiniTest(unittest.TestCase):
    
    def test_str(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.FRI, 12, 45)
        self.assertEqual(str(term1),"Wtorek 9:45 [90]")
        self.assertEqual(str(term2),"Środa 10:15 [90]")
        self.assertEqual(str(term3),"Piątek 12:45 [90]")
     
    def test_timeCompare(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term3 = Term(Day.FRI, 12, 45)
        self.assertTrue(term1.earlierThan(term2))
        self.assertTrue(term2.earlierThan(term3))
        self.assertTrue(term1.earlierThan(term3))
        self.assertFalse(term1.laterThan(term2))
        self.assertFalse(term2.laterThan(term3))
        self.assertFalse(term1.laterThan(term3))
        self.assertFalse(term1.equals(term2))
        self.assertTrue(term1.equals(term1))

    def test_int(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term.fromInt(int(term1))
        self.assertTrue(term1.equals(term2))
        self.assertEqual(str(term2),"Wtorek 9:45 [90]")
        term1.reInt(int(term2))
        self.assertEqual(str(term1),"Wtorek 9:45 [90]")
        term1 = Term(Day.WED, 10, 15)
        term2 = Term.fromInt(int(term1))
        self.assertTrue(term1.equals(Term.fromInt(int(term1))))
        self.assertEqual(str(term2),"Środa 10:15 [90]")
        term1.reInt(int(term2))
        self.assertEqual(str(term1),"Środa 10:15 [90]")
    
    def test_new(self):
        term1 = Term(Day.TUE, 9, 45)
        term2 = Term(Day.WED, 10, 15)
        term = term1.minuteDifference(term2)
        self.assertEqual(str(term), "Wtorek 9:45 [30]")
        term = term1.endTime()
        self.assertEqual(str(term), "Wtorek 11:15 [90]")
        term = term2.endTime()
        self.assertEqual(str(term), "Środa 11:45 [90]")

    

if __name__ == '__main__':
    unittest.main()
