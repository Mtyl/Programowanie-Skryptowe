import enum
from typing import List
from .lesson import Lesson
from .term import Term, Break
from .day import Day
from math import floor
import re

class Action(enum.Enum):
    DAY_EARLIER = 0
    DAY_LATER = 1
    TIME_EARLIER = 2
    TIME_LATER = 3

class Observer(object):
    @staticmethod
    def update(timetable):
        timetable.findMismatch()

class BasicTimetable(object):
    def __init__(self):
        self.list = []
    
    def findMismatch(self):
        pass

    def get(self, term: Term) -> Lesson:
        for lesson in self.list:
            if(lesson.term == term):
                return lesson
        return None
    
    def put(self, lesson: Lesson) -> bool:
        if not hasattr(self, "can_be_transferred_to"):
            raise Exception("can_be_transferred_to is not defined")
        if(self.can_be_transferred_to(lesson.term, lesson.full_time)):
            self.list.append(lesson)
            return True
        raise ValueError
        #return False
    
    def parse(self, actions: List[str]) -> List[Action]:
        out = []
        for each in actions:
            if each == "d+":
                out.append(Action.DAY_LATER)
            elif each == "d-":
                out.append(Action.DAY_EARLIER)
            elif each == "t+":
                out.append(Action.TIME_LATER)
            elif each == "t-":
                out.append(Action.TIME_EARLIER)
            else:
                raise ValueError("Translation " + each + " is incorrect")    
        return out                

    def perform(self, actions: List[Action]):

        for i in range(len(actions)):
            if(actions[i] == Action.DAY_EARLIER):
                self.list[i%len(self.list)].earlierDay()
            elif(actions[i] == Action.DAY_LATER):
                self.list[i%len(self.list)].laterDay()
            elif(actions[i] == Action.TIME_LATER):
                self.list[i%len(self.list)].laterTime()
            elif(actions[i] == Action.TIME_EARLIER):
                self.list[i%len(self.list)].earlierTime()
    
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
    
    def remove(self, term: Term):
        for i,lesson in enumerate(self.list):
            if(lesson.term == term):
                self.list.pop(i)
                return True
        return False

    def replace(self, lesson: Lesson):
        self.remove(lesson.term)
        return self.put(lesson)
    
    def __add__(self, lesson):
        self.replace(lesson)

    def __sub__(self, lesson):
        if(not self.remove(lesson.term)):
            raise ValueError("ERROR NOTHING TO REMOVE")



class Timetable1(BasicTimetable):
    def __init__(self):
        super().__init__()

    def busy(self, term: Term) -> bool:
        return self.get(term) != None

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        return (not self.busy(term)) and Lesson.isTermValid(term, full_time)

    def __add__(self, lesson):
        self.replace(lesson)

    def __sub__(self, lesson):
        if(not self.remove(lesson.term)):
            print("\nERROR NOTHING TO REMOVE")

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




class Timetable2(BasicTimetable):
    def __init__(self, breaks:List[Break]):
        super().__init__()
        self.breakList = breaks
        self.validTerms = []
        self.dictionary = dict()
        x = 480
        while(x <= 1170):
            break1 = None
            for i in self.breakList:
                if(int(i) == x):
                    break1 = i
            if(break1 != None):
                x += break1.duration
            else:
                self.validTerms.append(Term.fromInt(x))
                x += 90

    def busy(self, term: Term) -> bool:
        termMon = Term.fromInt(int(term) % 1440)
        for i in self.validTerms:
            if termMon == i:
                return self.get(term) != None
        else:
            return True

    def can_be_transferred_to(self, term: Term, full_time: bool) -> bool:
        return (not self.busy(term)) and Lesson.isTermValid(term, full_time)

    def transferrer(self, lesson, pos):
        newIndex = -7
        termMon = Term.fromInt(int(lesson.term) % 1440)
        for index, value in enumerate(self.validTerms):
            if termMon == value:
                newIndex = index + pos
        if newIndex in range(0, len(self.validTerms)):
            lesson.move(int(self.validTerms[newIndex]) - int(termMon))
            return True
        raise ValueError
        #return False
        

    def get(self, term: Term) -> Lesson:
        if int(term) in self.dictionary:
            return self.dictionary[int(term)]
        else:
            None
    
    def remove(self, term):
        if self.get(term) != None:
            self.dictionary.pop(int(term))
            return True
        return False
    
    def put(self, lesson: Lesson) -> bool:
        if(self.can_be_transferred_to(lesson.term, lesson.full_time)):
            self.dictionary[int(lesson.term)] = lesson
            return True
        raise ValueError
        #return False

    def findMismatch(self):
        for key in self.dictionary:
            newKey = int(self.dictionary[key].term)
            if key != newKey:
                lesson = self.dictionary[key]
                self.dictionary.pop(key)
                self.dictionary[newKey] = lesson
                break

    def perform(self, actions: List[Action]):
        lessons = []
        keys = []
        for key in self.dictionary:
            keys.append(key)
        keys.sort()
        for key in keys:
            lessons.append(self.dictionary[key])
        errors = []
        for i in range(len(actions)):
            try:
                if(actions[i] == Action.DAY_EARLIER):
                    lessons[i%len(lessons)].earlierDay()
                elif(actions[i] == Action.DAY_LATER):
                    lessons[i%len(lessons)].laterDay()
                elif(actions[i] == Action.TIME_LATER):
                    lessons[i%len(lessons)].laterTime()
                elif(actions[i] == Action.TIME_EARLIER):
                    lessons[i%len(lessons)].earlierTime()
            except ValueError:
                errors.append((lessons[i%len(lessons)], actions[i]))

    def __str__(self):
        out = " "*20
        for i in range(0,7):
            out += "*" + Timetable1.align(Day(i).readable())
        out += "\n" + "*"*(8*20+7) + "\n"
        start = Term.fromInt(480)
        end = Term.fromInt(570)
        
        for i in range(len(self.validTerms)):
            time = str(start)[:-5] + "-" + str(end)[:-5]
            out += Timetable1.align(time)
            break1 = None
            
            for j in range(0,7):
                lesson = self.get(Term.fromInt(int(start)+1440*j))
                if(lesson == None):
                    out += "*" + " "*20 
                else:
                    out += "*" + Timetable1.align(lesson.name)
            
            for i in self.breakList:
                if(int(i) == int(end)):
                    break1 = i
            if(break1 == None):
                start.reInt(int(start)+90)
                end.reInt(int(end)+90)
            else:
                out += "\n" + "*"*(8*20+7)
                start.reInt(int(start)+90+break1.duration)
                end.reInt(int(end)+90+break1.duration)
                break2 = Break.fromInt(int(break1)+break1.duration, 1)
                out += "\n" + Timetable1.align(break1.bt() + "-" + break2.bt()) + "-" * 147
            out += "\n" + "*"*(8*20+7) + "\n"
        return out

