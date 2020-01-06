#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
from pynput.keyboard import Key, Listener # https://pythonhosted.org/pynput/keyboard.html
import pynput
import MaxPower_Classes
import System
import threading

# Below is just for simulation purposes
class Keyboard_IO:

    def call_rpm(key):
        if System.timer_flag: 
            MaxPower_Classes.total_rpm = 0;
            return exit();
        MaxPower_Classes.Max_Power_Wind.Get_RPM(); # calls this function to increment

    def RPM_Listener():
        with Listener(on_press=Keyboard_IO.call_rpm) as input:
            input.join()