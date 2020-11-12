#!/usr/bin/python3
from fractions import Fraction

def sum(a, b):
    x = 0
    y = 0
    try:
        x = Fraction(a)
    except:
        pass
        
    try:
        x = complex(a)
    except:
        pass  
  
    try:
        y = Fraction(b)
    except:
        pass 
            
    try:
        y = complex(b)
    except:
       pass
         
                
    return x + y

if __name__ == '__main__':
    print("Suma = {}".format(sum(2,2)))
    print("Suma = {}".format(sum(2,2.0)))
    #print("Suma = {}".format(sum(2,'2')))
    print("Suma = {}".format(sum('2','2')))
    zmienna = 2
    print(type(zmienna))
    zmienna = '2'
    print(type(zmienna))
   
    print("__name__ =  {}".format(__name__))
