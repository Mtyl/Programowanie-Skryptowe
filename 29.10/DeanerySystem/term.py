#!/usr/bin/python3
from .day import Day
from math import floor

class Term:
    
    def __init__(self, hour, minute, duration=90, day=Day.MON):
        self.__hour = hour
        self.__minute = minute
        if(type(duration) == type(Day.MON)):
            day = duration
            duration = 90
        self.__duration = duration
        self.__day = day

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration:int):
        if duration in range(0, 600):
            self.__duration = duration
            return True
        return False

    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day:Day):
        if(type(day) == type(Day.MON)):
            self.__day = day
            return True
        return False

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if minute in range(0, 60):
            self.__minute = minute
            return True
        return False

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if hour in range(0, 23):
            self.__hour = hour
            return True
        return False

    def __str__(self):
        if(self.__minute < 10):
            return "{}:0{} [{}]".format(self.__hour, self.__minute, self.__duration)
        else:
            return "{}:{} [{}]".format(self.__hour, self.__minute, self.__duration)
         
    
    def dayAndHour(self):
        end = self.endTime()
        output = self.__day.readable() + " " + str(self.__hour) + ":" 
        if(self.__minute < 10):
            output += "0" + str(self.__minute) 
        else:
            output += str(self.__minute)
        output += "-" + str(end.__hour) + ":"
        if(end.__minute < 10):
            output += "0" + str(end.__minute) 
        else:
            output += str(end.__minute)
        return output

    def __int__(self):
        return (self.__day.value*1440+self.__hour*60+self.__minute)

    @classmethod
    def fromInt(cls, minutes:int):
        return Term(floor(minutes/60) - floor(minutes/1440)*24, minutes % 60, Day(floor(minutes/1440)))
        
    def reInt(self, minutes:int):
        self.__hour = floor(minutes/60) - floor(minutes/1440)*24
        self.__minute = minutes % 60
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

    def __lt__(self,term):
        return int(self) < int(term)
    
    def __le__(self, term):
        return int(self) <= int(term)

    def __ge__(self, term):
        return int(self) >= int(term)
    
    def __gt__(self,term):
        return int(self) > int(term)
    
    def __eq__(self,term):
        return int(self) == int(term) and self.duration == term.duration

    def __sub__(self,term):
        intSelf = int(self) % 1440
        intTerm = int(term) % 1440
        newTerm = Term.fromInt(int(term))
        intSelf -= intTerm
        if(intTerm < 0):
            intTerm *= -1
        newTerm.duration = intSelf + self.__duration
        return newTerm

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
        return Term.fromInt(int(self)+self.__duration)

    

