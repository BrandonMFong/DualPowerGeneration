#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from Files import Log_Handler
from random import random
import math
import System
import time
import IO
import os


### CLASSES ###
class Max_Power_Wind:
    def Avg_Pwr(Torque, RPM):
        pi = math.pi;
        global Average_POWER_WIND;
        Average_POWER_WIND = (Torque * RPM * pi)/30;
        Log_Handler.Write_Log(os.path.basename(__file__) + "Avg Pwr Wind calculated\n");

    def Avg_Torque(Total_Torque):
        global Average_TORQUE_Wind;
        Average_TORQUE_Wind = Total_Torque/System.Seconds;
        Log_Handler.Write_Log(os.path.basename(__file__) + "Avg Torque Wind calculated\n");

    def Avg_RPM(Total_RPM):
        global Average_RPM_Wind;
        Average_RPM_Wind = Total_RPM/System.Seconds;
        Log_Handler.Write_Log(os.path.basename(__file__) + "Avg RPM Wind calculated\n");

    # Taking out the while loop
    # this function is now going to be called whenever I press the key
    def Get_RPM():
        # Getting RPM
        global total_rpm;
        if System.timer_flag: Max_Power_Wind.Avg_RPM(total_rpm); # If the timer is up, calculate the avg rpm
        else: # if a key was pressed, increment
            total_rpm = total_rpm + 1;
            print("total_rpm = {}" .format(total_rpm));
            Log_Handler.Write_Log(os.path.basename(__file__) + "total_rpm = {}\n" .format(total_rpm));
            

    # Equation: Torque = Radius * Force * sin(Theta)
    def Get_Torque():
        total_torque = 0;
        i = 0;
        # Getting Torque
        while True: 
            if System.timer_flag: break;
            time.sleep(System.delay); # Will execute equation after one second passes
            i = i + 1;
            force_of_the_blades = random(); # simulating a analog read of the torque
            # Random is temporary, we will read real values
            num = radius_of_the_blades * force_of_the_blades * math.sin(angle_of_the_blades);
            total_torque = total_torque + num;
            print("i = {}, total_torque = {} " .format(i, total_torque));
            Log_Handler.Write_Log(os.path.basename(__file__) + "i = {}, total_torque = {} \n" .format(i, total_torque));

        Max_Power_Wind.Avg_Torque(total_torque);

#TODO figure out the equations
class Max_Power_Solar:
    def place_holder():
        return 0;


def init():
    # Wind
    global Average_RPM_Wind;
    global Average_TORQUE_Wind;
    global Average_POWER_WIND;
    global radius_of_the_blades;
    global angle_of_the_blades;
    global force_of_the_blades;
    global total_rpm;

    # Solar
    global Average_POWER_SOLAR;
    global solar_current;
    global solar_voltage;

    # Initialize
    Average_RPM_Wind = 0;
    Average_TORQUE_Wind = 0;
    Average_POWER_WIND = 0;
    Average_POWER_SOLAR = 0;
    radius_of_the_blades = 50; # Can be changed
    angle_of_the_blades = 120; # Three blades right?
    force_of_the_blades = random(); # TODO figure this out, we need to dynamically calculate this
    total_rpm = 0;


