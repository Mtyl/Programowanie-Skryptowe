import enum
from typing import List
from .lesson import Lesson
from .term import Term
from .day import Day
from math import floor
import re

class Action(enum.Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3

class Timetable1(object):
    def __init__(self):
        self.__list = []

    def get(self, term: Term) -> Lesson:
        for lesson in self.__list:
            if(lesson.term == term):
                return lesson
        return None
    
    def remove(self, term: Term):
        for i,lesson in enumerate(self.__list):
            if(lesson.term == term):
                self.__list.pop(i)
                return True
        return False

    def busy(self, term: Term) -> bool:
        return self.get(term) != None

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        return (not self.busy(term)) and Lesson.isTermValid(term, full_time)

    def put(self, lesson: Lesson) -> bool:
        if(self.can_be_transferred_to(lesson.term, lesson.full_time)):
            self.__list.append(lesson)
            return True
        return False
    
    def replace(self, lesson: Lesson):
        self.remove(lesson.term)
        return self.put(lesson)

    def __add__(self, lesson):
        self.replace(lesson)

    def __sub__(self, lesson):
        if(not self.remove(lesson.term)):
            print("\nERROR NOTHING TO REMOVE")

    def parse(self, actions: List[str]) -> List[Action]:
        reg = re.compile(r'^d\+$|^t\+$|^d-$|^t-$')
        i = 0
        while i < len(actions):
            if reg.match(actions[i]):
                i += 1
            else:
                actions.pop(i)
        i = {"d+":Action.DAY_LATER, 
            "d-":Action.DAY_EARLIER, 
            "t-":Action.TIME_EARLIER, 
            "t+":Action.TIME_LATER}
        out = []
        for each in actions:
            out.append(i[each])
        return out                

    def perform(self, actions: List[Action]):

        for i in range(len(actions)):
            if(actions[i] == Action.DAY_EARLIER):
                self.__list[i%len(self.__list)].earlierDay()
            elif(actions[i] == Action.DAY_LATER):
                self.__list[i%len(self.__list)].laterDay()
            elif(actions[i] == Action.TIME_LATER):
                self.__list[i%len(self.__list)].laterTime()
            elif(actions[i] == Action.TIME_EARLIER):
                self.__list[i%len(self.__list)].earlierTime()

    @staticmethod
    def align(string):
        if(len(string) > 20):
            return string[:20]
        else:
            i = (20-len(string))/2
            if(i % 1):
                i = floor(i)
                return " "*i + string + " "*(i+1)
            else:
                i = int(i)
                return " "*i + string + " "*i

    def __str__(self):
        out = " "*20
        for i in range(0,7):
            out += "*" + Timetable1.align(Day(i).readable())
        out += "\n" + "*"*(8*20+7) + "\n"
        start = Term.fromInt(480)
        end = Term.fromInt(570)
        for i in range(0,8):
            time = str(start)[:-5] + "-" + str(end)[:-5]
            out += Timetable1.align(time)
            for j in range(0,7):
                lesson = self.get(Term.fromInt(int(start)+1440*j))
                if(lesson == None):
                    out += "*" + " "*20 
                else:
                    out += "*" + Timetable1.align(lesson.name)
            start.reInt(int(start)+90)
            end.reInt(int(end)+90)
            out += "\n" + "*"*(8*20+7) + "\n"
        return out
