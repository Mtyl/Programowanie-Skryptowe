#!/usr/bin/python3
from .day import Day
from math import floor

class BasicTerm(object):
    def __init__(self, hour, minute, duration):
        self.__hour = hour
        self.__minute = minute
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration:int):
        if duration in range(0, 600):
            self.__duration = duration
            #return True
        else:
            raise ValueError(duration)
        #return False
    
    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        if minute in range(0, 60):
            self.__minute = minute
            #return True
        else:
            raise ValueError(minute)
        #return False

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        if hour in range(0, 23):
            self.__hour = hour
            #return True
        else:
            raise ValueError(hour)
        #return False

    def __str__(self):
        if(self.minute < 10):
            return "{}:0{} [{}]".format(self.hour, self.minute, self.duration)
        else:
            return "{}:{} [{}]".format(self.hour, self.minute, self.duration)
    
    def isEq(self,term):
        return self.hour == term.hour and self.minute == term.minute and self.duration == term.duration

class Break(BasicTerm):
    def __init__(self, hour, minute, duration):
        super().__init__(hour, minute, duration)

    def __int__(self):
        return (self.hour*60+self.minute)
    
    def reInt(self, minutes):
        self.hour = floor(minutes/60)
        self.minutes = minutes % 60
    
    @classmethod
    def fromInt(cls, minutes:int, duration):
        return Break(floor(minutes/60), minutes % 60, duration)

    def getTerm(self):
        return BasicTerm(self.hour, self.minute, self.duration)

    def __str__(self):
        return "Przerwa"

    def bt(self):
        if(self.minute < 10):
            return "{}:0{}".format(self.hour, self.minute)
        else:
            return "{}:{}".format(self.hour, self.minute)


class Term(BasicTerm):
    
    def __init__(self, hour, minute, duration=90, day=Day.MON):
        if(type(duration) == type(Day.MON)):
            day = duration
            duration = 90
        super().__init__(hour, minute, duration)
        self.__day = day
    
    def strKey(self):
        if(self.minute < 10):
            return "{}:0{} [{}] {}".format(self.hour, self.minute, self.duration, self.day.readable())
        else:
            return "{}:{} [{}] {}".format(self.hour, self.minute, self.duration, self.day.readable)
    
    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day:Day):
        if(type(day) == type(Day.MON)):
            self.__day = day
            return True
        return False
           
    def dayAndHour(self):
        end = self.endTime()
        output = self.__day.readable() + " " + str(self.hour) + ":" 
        if(self.minute < 10):
            output += "0" + str(self.minute) 
        else:
            output += str(self.minute)
        output += "-" + str(end.hour) + ":"
        if(end.minute < 10):
            output += "0" + str(end.minute) 
        else:
            output += str(end.minute)
        return output

    def __int__(self):
        return (self.__day.value*1440+self.hour*60+self.minute)

    @classmethod
    def fromInt(cls, minutes:int):
        return Term(floor(minutes/60) - floor(minutes/1440)*24, minutes % 60, Day(floor(minutes/1440)))
        
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
        newTerm.duration = intSelf + self.duration
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
        return Term.fromInt(int(self)+self.duration)
    

    

