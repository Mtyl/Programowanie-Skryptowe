#!/usr/bin/python3
#-*-coding: utf-8-*-
import re
import unittest

def skrypt(inp):
    out = ""
    while(inp != ''):
        cur = re.match('^\d+', inp)
        if cur:
            inp = inp[cur.end():]
            out += ("Liczba:" + cur.group(0))
        cur = re.match('^\D+', inp)
        if cur:
            inp = inp[cur.end():]
            out += ("Wyraz:" + cur.group(0))
    return out

class TestStringMethods(unittest.TestCase):

    def test_skrypt(self):
        self.assertEqual(skrypt('50xd'), 'Liczba:50Wyraz:xd')
        self.assertEqual(skrypt('xd'), 'Wyraz:xd')
        self.assertEqual(skrypt('xd50'), 'Wyraz:xdLiczba:50')

if __name__ == '__main__':
    unittest.main()
