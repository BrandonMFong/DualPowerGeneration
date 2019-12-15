# Property by Your Engineering Solutions (Y.E.S.)
# Engineers: Lorans Hirmez, Brandon Fong

# LIBRARIES
import math
from random import random

# CLASSES
class Max_Power_Wind:
    def Avg_Pwr(Torque, RPM):
        pi = math.pi; # There is a math lib already imported, more information: https://docs.python.org/3/library/math.html
        return (Torque * RPM * pi)/30;

    def Avg_Torque(Total_Torque, seconds):
        return Total_Torque/seconds;

    def Avg_RPM(Total_RPM, seconds):
        return Total_RPM/seconds;

    def Get_RPM():
        total_rpm = 0;
        # Getting RPM
        for i in range(60): # for i = 0; i < 60; i++
            #TODO put this in the Max_Power_Wind Class
            num = abs(random() % (3600 + 1 - 0) + 0); # Need more information for " ... 1 - 0) + 0
            total_rpm += num;
            print("Num variable for RPM: ", num);
        return total_rpm;

    def Get_Torque():
        total_torque = 0;
        # Getting Torque
        for i in range(60):# for i = 0; i < 60; i++
            #TODO put this in the Max_Power_Wind Class
            num = abs(random() % (500 + 1 - 0) + 0); # Need more information for " ... 1 - 0) + 0
            total_torque += num;
            print("Num variable for Torque: ", num);
        return total_torque;

#TODO figure out the equations
class Max_Power_Solar:
    def place_holder():
        return 0;