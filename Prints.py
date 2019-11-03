from TrainersClass import *
from SpartanClass import *
from BatchesClass import *
from ModuleClass import *

import datetime

time_now = int(datetime.datetime.now().strftime("%H"))

print("Please input your Spartan ID:")
ID = int(input())

if time_now >= 12 and time_now <= 16 and ID == 1:
    print("Good Afternoon, {}!".format(Spartan1.name)
elif time_now <= 11 and ID == 1:
    print("Good Morning, {}!".format(Spartan1.name)
elif time_now >= 17 and ID == 1:
    print("Good Evening, {}!".format(Spartan1.name)
elif time_now >= 12 and time_now <= 16 and ID == 2:
    print("Good Afternoon, {}!".format(Spartan2.name)
elif time_now <= 11 and ID == 2:
    print("Good Morning, {}!".format(Spartan2.name)
elif time_now >= 17 and ID == 2:
    print("Good Evening, {}!".format(Spartan2.name)
elif time_now >= 12 and time_now <= 16 and ID == 3:
    print("Good Afternoon, {}!".format(Spartan3.name)
elif time_now <= 11 and ID == 3:
    print("Good Morning, {}!".format(Spartan3.name)
elif time_now >= 17 and ID == 3:
    print("Good Evening, {}!".format(Spartan3.name)
elif time_now >= 12 and time_now <= 16 and ID == 4:
    print("Good Afternoon, {}!".format(Spartan4.name)
elif time_now <= 11 and ID == 4:
    print("Good Morning, {}!".format(Spartan4.name)
elif time_now >= 17 and ID == 4:
    print("Good Evening, {}!".format(Spartan4.name)
elif time_now >= 12 and time_now <= 16 and ID == 5:
    print("Good Afternoon, {}!".format(Spartan5.name)
elif time_now <= 11 and ID == 5:
    print("Good Morning, {}!".format(Spartan5.name)
elif time_now >= 17 and ID == 5:
    print("Good Evening, {}!".format(Spartan5.name)