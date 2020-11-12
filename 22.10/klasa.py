#!/usr/bin/python3
class Klasa(object):
    tab = [1,2,3]
    def __init__(self, table, zmienna1=6, zmienna2=9):
        print("Wywołano metodę '__init__()'")
        self.tab = table
        self._zmienna1 = zmienna1
        self.__zmienna2 = zmienna2

    def __del__(self):
        print("Wywołano metodę '__del__()'")

    def __str__(self):
        return "Wywołano metodę '__str__()'"

    def metodaInstancyjna(self):
        print("Wywołano metodę 'metodaInstancyjna()'")

    @classmethod
    def metodaKlasowa(cls):
        print("Wywołano metodę 'metodaKlasowa()'")

    @staticmethod
    def metodaStatyczna():
        print("Wywołano metodę 'metodaStatyczna()'")