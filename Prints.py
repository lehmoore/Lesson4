from TrainersClass import *
from SpartanClass import *
from BatchesClass import *
from ModuleClass import *

import datetime

time_now = int(datetime.datetime.now().strftime("%H"))

print("Please input your Spartan ID:")
ID = int(input())

if time_now >= 12 and time_now <= 16 and ID == 1:
    print("Good Afternoon, {}!".format(Spartan1.name))
elif time_now <= 11 and ID == 1:
    print("Good Morning, {}!".format(Spartan1.name))
elif time_now >= 17 and ID == 1:
    print("Good Evening, {}!".format(Spartan1.name))
elif time_now >= 12 and time_now <= 16 and ID == 2:
    print("Good Afternoon, {}!".format(Spartan2.name))
elif time_now <= 11 and ID == 2:
    print("Good Morning, {}!".format(Spartan2.name))
elif time_now >= 17 and ID == 2:
    print("Good Evening, {}!".format(Spartan2.name))
elif time_now >= 12 and time_now <= 16 and ID == 3:
    print("Good Afternoon, {}!".format(Spartan3.name))
elif time_now <= 11 and ID == 3:
    print("Good Morning, {}!".format(Spartan3.name))
elif time_now >= 17 and ID == 3:
    print("Good Evening, {}!".format(Spartan3.name))
elif time_now >= 12 and time_now <= 16 and ID == 4:
    print("Good Afternoon, {}!".format(Spartan4.name))
elif time_now <= 11 and ID == 4:
    print("Good Morning, {}!".format(Spartan4.name))
elif time_now >= 17 and ID == 4:
    print("Good Evening, {}!".format(Spartan4.name))
elif time_now >= 12 and time_now <= 16 and ID == 5:
    print("Good Afternoon, {}!".format(Spartan5.name))
elif time_now <= 11 and ID == 5:
    print("Good Morning, {}!".format(Spartan5.name))
elif time_now >= 17 and ID == 5:
    print("Good Evening, {}!".format(Spartan5.name))
elif time_now >= 12 and time_now <= 16 and ID == 6:
    print("Good Afternoon, {}!".format(Spartan6.name))
elif time_now <= 11 and ID == 6:
    print("Good Morning, {}!".format(Spartan6.name))
elif time_now >= 17 and ID == 6:
    print("Good Evening, {}!".format(Spartan6.name))
elif time_now >= 12 and time_now <= 16 and ID == 7:
    print("Good Afternoon, {}!".format(Spartan7.name))
elif time_now <= 11 and ID == 7:
    print("Good Morning, {}!".format(Spartan7.name))
elif time_now >= 17 and ID == 7:
    print("Good Evening, {}!".format(Spartan7.name))
elif time_now >= 12 and time_now <= 16 and ID == 8:
    print("Good Afternoon, {}!".format(Spartan8.name))
elif time_now <= 11 and ID == 8:
    print("Good Morning, {}!".format(Spartan8.name))
elif time_now >= 17 and ID == 8:
    print("Good Evening, {}!".format(Spartan8.name))
elif time_now >= 12 and time_now <= 16 and ID == 9:
    print("Good Afternoon, {}!".format(Spartan9.name))
elif time_now <= 11 and ID == 9:
    print("Good Morning, {}!".format(Spartan9.name))
elif time_now >= 17 and ID == 9:
    print("Good Evening, {}!".format(Spartan9.name))
elif time_now >= 12 and time_now <= 16 and ID == 10:
    print("Good Afternoon, {}!".format(Spartan10.name))
elif time_now <= 11 and ID == 10:
    print("Good Morning, {}!".format(Spartan10.name))
elif time_now >= 17 and ID == 10:
    print("Good Evening, {}!".format(Spartan10.name))
elif time_now >= 12 and time_now <= 16 and ID == 11:
    print("Good Afternoon, {}!".format(Spartan11.name))
elif time_now <= 11 and ID == 11:
    print("Good Morning, {}!".format(Spartan11.name))
elif time_now >= 17 and ID == 11:
    print("Good Evening, {}!".format(Spartan11.name))
elif time_now >= 12 and time_now <= 16 and ID == 12:
    print("Good Afternoon, {}!".format(Spartan12.name))
elif time_now <= 11 and ID == 12:
    print("Good Morning, {}!".format(Spartan12.name))
elif time_now >= 17 and ID == 12:
    print("Good Evening, {}!".format(Spartan12.name))
elif time_now >= 12 and time_now <= 16 and ID == 13:
    print("Good Afternoon, {}!".format(Spartan13.name))
elif time_now <= 11 and ID == 13:
    print("Good Morning, {}!".format(Spartan13.name))
elif time_now >= 17 and ID == 13:
    print("Good Evening, {}!".format(Spartan13.name))
elif time_now >= 12 and time_now <= 16 and ID == 14:
    print("Good Afternoon, {}!".format(Spartan14.name))
elif time_now <= 11 and ID == 14:
    print("Good Morning, {}!".format(Spartan14.name))
else:
    print("Good Evening, {}!".format(Spartan5.name))