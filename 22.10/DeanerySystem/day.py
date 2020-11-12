import enum

class Day(enum.Enum):
    MON = 0
    TUE = 1
    WED = 2
    THU = 3
    FRI = 4
    SAT = 5
    SUN = 6

    def difference(self, day):
        x = day.value - self.value
        if(x > 4):
            x -= 7
        elif(x < -4):
            x += 7
        return x
    
    def readable(self):
        return {
        Day.MON : "Poniedziałek",
        Day.TUE : "Wtorek",
        Day.WED : "Środa",
        Day.THU : "Czwartek",
        Day.FRI : "Piątek",
        Day.SAT : "Sobota",
        Day.SUN : "Niedziela"
        }[self]
        


def nthDayFrom(n:int, day:Day):
    return Day((day.value + n)%7)