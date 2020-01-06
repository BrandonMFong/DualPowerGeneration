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
    def Avg_Pwr(Torque, RPM):# This gets called from main.py
        global Average_POWER_WIND;
        Average_POWER_WIND = (Torque * RPM * math.pi)/30;
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
        
        Max_Power_Wind.Avg_RPM(total_rpm);

    # Equation: Torque = Radius * Force * sin(Theta)
    def Get_Torque():
        total_torque = 0;
        # Getting Torque
        while True: 
            if System.timer_flag: break;
            time.sleep(System.delay); # Will execute equation after one second passes
            force_of_the_blades = IO.Random_IO.BLADE_FORCE_listener(); # simulating a analog read of the torque
            # Random is temporary, we will read real values
            num = radius_of_the_blades * force_of_the_blades * math.sin(angle_of_the_blades);
            total_torque = total_torque + num;
            print("total_torque = {} " .format(total_torque));
            Log_Handler.Write_Log(os.path.basename(__file__) + "total_torque = {} \n" .format(total_torque));

        Max_Power_Wind.Avg_Torque(total_torque);

#TODO figure out the equations
# Should I separate the read for current and volatage?
class Max_Power_Solar:
    def Avg_Pwr(solar_power):
        global Average_POWER_SOLAR;
        Average_POWER_SOLAR = solar_power/System.Seconds;
        Log_Handler.Write_Log(os.path.basename(__file__) + "Avg Pwr Solar calculated\n");

    def Get_Solar_Power():
        global total_solar_pwr;
        solar_current = 0;
        solar_voltage = 0;
        total_solar_pwr = 0;
        while True:
            if System.timer_flag: break;
            time.sleep(System.delay);
            solar_current = IO.Random_IO.SOLAR_CURR_listener();
            solar_voltage = IO.Random_IO.SOLAR_VOLT_listener();
            total_solar_pwr = (solar_current*solar_voltage) + total_solar_pwr;
            Log_Handler.Write_Log(os.path.basename(__file__) + "solar curr, solar volt, and total solar power calculated\n");

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
    global total_solar_pwr

    # Initialize
    Average_RPM_Wind = 0;
    Average_TORQUE_Wind = 0;
    Average_POWER_WIND = 0;
    Average_POWER_SOLAR = 0;
    radius_of_the_blades = 50; # Can be changed
    angle_of_the_blades = 120; # Three blades right?
    force_of_the_blades = random(); # TODO figure this out, we need to dynamically calculate this
    total_rpm = 0;
    solar_current = 0;
    solar_voltage = 0;
    total_solar_pwr = 0;


