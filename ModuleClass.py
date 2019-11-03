from BatchesClass import *

class Module(Batches):

    def __init__(self, stream, duration):
        self.stream = stream
        self.duration = duration

Module1 = Module("Data", "8 Weeks")
Module2 = Module("Business", "6 Weeks")
Module3 = Module("Java", "10 Weeks")