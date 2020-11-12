#!/usr/bin/python3
from inspect import signature
import unittest

def argumenty(*args, **kwargs):
        def wynik(funkcja):
            decList = []
            decList += args[0]
            parLen = len(signature(funkcja).parameters) - 1
            def wrapper(self, *args, **kwargs):
                remaining = 0
                finalArgs = []
                finalArgs += args
                if([len(args) < parLen]):
                    remaining = parLen - len(args)
                if remaining > 0:
                    finalArgs += decList[:remaining]
                string = funkcja(self, *finalArgs)
                if type(string) == tuple:
                    if(len(string) > 1):
                        return string[1]
                out = 0
                if len(decList) > remaining:
                    out = decList[remaining]
                else:
                    out = decList[-1]
                return (string, out)
            return wrapper
        return wynik 


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]  

    def __setitem__(self, key, value):
        if(key == "suma"):
            self.argumentySuma = value
        elif(key == "roznica"):
            self.argumentyRoznica = value
    @argumenty(argumentySuma)
    def suma(self,a,b,c):
        return( "%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(self,x,y):
        return("%d-%d=%d" % (x,y,x-y))

class extest(unittest.TestCase):
    def test_decorate(self):
        op=Operacje()
        x = op.suma(1,2,3)
        self.assertEqual(x[0], "1+2+3=6")
        self.assertEqual(x[1], 4)
        x = op.suma(1,2) 
        self.assertEqual(x[0], "1+2+4=7")
        self.assertEqual(x[1], 5)
        x = op.suma(1) 
        self.assertEqual(x[0], "1+4+5=10")
        self.assertEqual(x[1], 5)
        try:
            op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
        except TypeError:
            x = True
        self.assertTrue(x)
        x = op.roznica(2,1) 
        self.assertEqual(x[0], "2-1=1")
        self.assertEqual(x[1], 4)
        x = op.roznica(2)
        self.assertEqual(x[0], "2-4=-2")
        self.assertEqual(x[1], 5)
        x = op.roznica() #Wypisze: 4-5=-1
        self.assertEqual(x[0], "4-5=-1")
        self.assertEqual(x[1], 6)
        op['suma']=[1,2]
        op['roznica']=[1,2,3]
        self.assertEqual(op.argumentySuma, [1,2])
        self.assertEqual(op.argumentyRoznica, [1,2,3])

if __name__ == '__main__':
    unittest.main(exit=False)