#!/usr/bin/python3
from .day import Day
from math import floor

class Term(object):
    
    def __init__(self, day:Day, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day

    def __str__(self):
        return "{} {}:{} [{}]".format(self.__day.readable(), self.hour, self.minute, self.duration)

    def __int__(self):
        return (self.__day.value*1440+self.hour*60+self.minute)

    @classmethod
    def fromInt(cls, minutes:int):
        return Term(Day(floor(minutes/1440)), floor(minutes/60) - floor(minutes/1440)*24, minutes % 60)
        
    def reInt(self, minutes:int):
        self.hour = floor(minutes/60) - floor(minutes/1440)*24
        self.minute = minutes % 60
        self.__day = Day(floor(minutes/1440))
        return self

    def earlierThan(self, term):
        if(int(self) < int(term)):
            return True
        else:
            return False

    def laterThan(self, term):
        if(int(self) > int(term)):
            return True
        else:
            return False

    def equals(self, term):
        if(int(self) == int(term)):
            return True
        else:
            return False

    def minuteDifference(self, term):
        minutes1 = int(self) % 1440
        minutes2 = int(term) % 1440
        diff = 0
        if(minutes1 < minutes2):
            diff = Term.fromInt(int(self))
            diff.duration = minutes2 - minutes1
        else:
            diff = Term.fromInt(int(term))
            diff.duration = minutes1 - minutes2
        return diff

    def endTime(self):
        return Term.fromInt(int(self)+self.duration)

