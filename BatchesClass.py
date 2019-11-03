from SpartanClass import *

list_of_students = [Spartan1.name, Spartan2.name, Spartan3.name, Spartan4.name, Spartan5.name, Spartan6.name,
                    Spartan7.name, Spartan8.name, Spartan9.name, Spartan10.name, Spartan11.name, Spartan12.name,
                    Spartan13.name, Spartan14.name]

class Batches():

    def __init__(self, stream, start_date, list_of_students):
        self.stream = stream
        self.start_date = start_date
        self.list_of_students = list_of_students

D5 = Batches("Data", "2019-09-30", list_of_students)

