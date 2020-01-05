#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import math
from random import random
import System
import time
import IO


### CLASSES ###
class Max_Power_Wind:
    def Avg_Pwr(Torque, RPM):
        pi = math.pi;
        global Average_POWER_WIND;
        Average_POWER_WIND = (Torque * RPM * pi)/30;

    def Avg_Torque(Total_Torque):
        global Average_TORQUE_Wind;
        Average_TORQUE_Wind = Total_Torque/System.Seconds;

    def Avg_RPM(Total_RPM):
        global Average_RPM_Wind;
        Average_RPM_Wind = Total_RPM/System.Seconds;

    # This is being tracked with the tachometer
    # Task:
    # This functions needs to be on during the duration of the timer from 0 to 60
    # everytime the tachometer sees that piece of metal increment the num variable
    # when timer is up, calculate the average of the count over a minute (60 seconds, hence the timer duration)
    def Get_RPM():# OLD -> num = abs(random() % (3600 + 1 - 0) + 0);
        total_rpm = 0;
        # Getting RPM
        while True:
            if System.timer_flag: break;

            ## this is not being called
            # TODO figure this out
            # At this moment the IO function is detecting the key being pressed and setting the flag true
            # This is supposed to trigger this if statement to increment but it is not
            # Though this is a simulation, it is important to call this function from any external events
            # This is an important step to detecting one revolution of the wind turbine
            if IO.rpm_flag: # if a key was pressed, increment    
                total_rpm = total_rpm + 1;
                IO.rpm_flag = False;

            print("total_rpm = {}" .format(total_rpm));

        Max_Power_Wind.Avg_RPM(total_rpm);

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
            # OLD -> num = abs(random() % (500 + 1 - 0) + 0); # Need more information for " ... 1 - 0) + 0"
            num = radius_of_the_blades * force_of_the_blades * math.sin(angle_of_the_blades);
            total_torque = total_torque + num;
            print("i = {}, total_torque = {} " .format(i, total_torque));

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

    # Solar
    global Average_POWER_SOLAR;

    # Initialize
    Average_RPM_Wind = 0;
    Average_TORQUE_Wind = 0;
    Average_POWER_WIND = 0;
    Average_POWER_SOLAR = 0;
    radius_of_the_blades = 50; # Can be changed
    angle_of_the_blades = 120; # Three blades right?
    force_of_the_blades = random(); # TODO figure this out, we need to dynamically calculate this


