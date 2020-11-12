from .term import Term
from .day import Day


class Lesson(object):

    @staticmethod
    def isTermValid(term, full_time):
        minutes = int(term)
        if(full_time):
            if(minutes < 4*1440):
                if(minutes % 1440 in range(480,1200-term.duration+1)):
                    return True
                else:
                    return False
            elif(minutes > 4*1440 and minutes < 5 * 1440 ):
                if(minutes % 1440 in range(480,(60*17)-term.duration+1)):
                    return True
                else:
                    return False
        else:
            if(minutes > 5*1440):
                if(minutes % 1440 in range(480,1200-term.duration+1)):
                    return True
                else:
                    return False
            elif(minutes > 4*1440 and minutes < 5 * 1440 ):
                if(minutes % 1440 in range(60*17,(1200)-term.duration+1)):
                    return True
                else:
                    return False

    def __init__(self, timetable, term:Term, name:str, teacherName:str, year:int):
        self.__timetable = timetable
        if(int(term) < 1440*4+17*60-term.duration):
            self.__full_time = True
        else:
            self.__full_time = False
        if(Lesson.isTermValid(term, self.__full_time)):
            self.__term = term
        else:
            self.__term = Term.fromInt(480)
        self.__name = name
        self.__teacherName = teacherName
        self.__year = year
        
    
    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.__name
    
    @property
    def teacherName(self):
        return self.__teacherName

    @property
    def year(self):
        return self.__year

    @property
    def full_time(self):
        return self.__full_time
    
    @term.setter
    def term(self, term):
        if(Lesson.isTermValid(term, self.__full_time)):
            self.__term = term
            return True
        return False
        
    @name.setter
    def name(self, name):
        self.__name=name

    @teacherName.setter
    def teacherName(self, teacherName):
        self.__teacherName=teacherName

    @year.setter
    def year(self, year):
        if year in range(1,5):
            self.__year = year
            return True
        return False

    @full_time.setter
    def full_time(self, full_time):
        if type(full_time) == type(True):
            self.__full_time = full_time
            return True
        return False


    def __str__(self):
        output = self.__name + " (" + self.__term.dayAndHour() + ")\n"
        days = ["Pierwszy", "Drugi", "Trzeci", "Czwarty", "Piąty"]
        output += days[self.__year-1] + " rok studiów "
        if(self.__full_time):
            output += "stacjonarnych\n"
        else:
            output += "niestacjonarnych\n"
        output += "Prowadzący: " + self.__teacherName + "\n"
        return output

    def move(self, dist):
        from .timetable import Timetable1
        newMinutes = int(self.__term)+dist
        if(not newMinutes in range(0,7*1440)):
            return False
        if(self.__timetable.can_be_transferred_to(Term.fromInt(newMinutes), self.__full_time)):
            self.__term.reInt(newMinutes)
            return True
        return False 

    def earlierDay(self):
        return self.move(-1440)

    def laterDay(self):
        return self.move(+1440)

    def earlierTime(self):
        return self.move(-self.__term.duration)

    def laterTime(self):
        return self.move(self.__term.duration)

        
