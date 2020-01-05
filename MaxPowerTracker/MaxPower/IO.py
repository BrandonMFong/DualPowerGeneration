#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
import pynput
from pynput.keyboard import Key, Listener # https://pythonhosted.org/pynput/keyboard.html

# Flags to notify that a value was read
# probably can only replicate this with the rpm 
global rpm_flag;
rpm_flag = False;

# Below is just for simulation purposes
class Keyboard_IO:

    def simulate_rpm(key):
        rpm_flag = True;
        with open("log.txt", 'a') as f:
            f.write("Key was pressed\n");
    def Keyboard_Listener():
        with Listener(on_press=Keyboard_IO.simulate_rpm) as input:
            input.join();


    