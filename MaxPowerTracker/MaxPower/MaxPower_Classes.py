#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

# LIBRARIES
import math
from random import random
import System
import time


# CLASSES
class Max_Power_Wind:
    def Avg_Pwr(Torque, RPM):
        pi = math.pi;
        Max_Power_Objects.Average_POWER_WIND = (Torque * RPM * pi)/30;

    def Avg_Torque(Total_Torque):
        Max_Power_Objects.Average_TORQUE_Wind = Total_Torque/System.Seconds;

    def Avg_RPM(Total_RPM):
        Max_Power_Objects.Average_RPM_Wind = Total_RPM/System.Seconds;

    def Get_RPM():
        total_rpm = 0;
        i = 0;
        # Getting RPM
        while i < System.Seconds: 
            time.sleep(System.delay); # Will execute equation after one second passes
            i = i + 1;

            # Random is temporary, we will read real values
            num = abs(random() % (3600 + 1 - 0) + 0); # Need more information for " ... 1 - 0) + 0"
            total_rpm += num;
            print("Num variable for RPM: ", num);

        Max_Power_Wind.Avg_RPM(total_rpm);

    def Get_Torque():
        total_torque = 0;
        i = 0;
        # Getting Torque
        while i < System.Seconds: 
            time.sleep(System.delay); # Will execute equation after one second passes
            i = i + 1;

            # Random is temporary, we will read real values
            num = abs(random() % (500 + 1 - 0) + 0); # Need more information for " ... 1 - 0) + 0"
            total_torque += num;
            print("Num variable for Torque: ", num);

        Max_Power_Wind.Avg_Torque(total_torque);

#TODO figure out the equations
class Max_Power_Solar:
    def place_holder():
        return 0;

class Max_Power_Objects:
    def init():
        # Wind
        global Average_RPM_Wind;
        global Average_TORQUE_Wind;
        global Average_POWER_WIND;

        # Solar
        global Average_POWER_SOLAR;

        # Initialize
        Average_RPM_Wind = 0;
        Average_TORQUE_Wind = 0;
        Average_POWER_WIND = 0;
        Average_POWER_SOLAR = 0;


