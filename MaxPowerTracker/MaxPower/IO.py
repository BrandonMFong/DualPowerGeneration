#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
import pynput
from pynput.keyboard import Key, Listener # https://pythonhosted.org/pynput/keyboard.html
import MaxPower_Classes
import System
import threading

# Below is just for simulation purposes
class Keyboard_IO:

    def simulate_rpm(key):
        if System.timer_flag: 
            MaxPower_Classes.total_rpm = 0;
            return exit();
        MaxPower_Classes.Max_Power_Wind.Get_RPM(); # calls this function to increment
        with open("log.txt", 'a') as f:
            f.write("Key was pressed\n");

    def Keyboard_Listener():
        with Listener(on_press=Keyboard_IO.simulate_rpm) as input:
            input.join()