#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
import pynput
from pynput.keyboard import Key, Listener # https://pythonhosted.org/pynput/keyboard.html

# TODO figure out how to only call the rpm function when you press the key
class Keyboard_IO:
    def on_press(key):
        self.increment(True);

    def on_release(key):
        increment(False);
        return False;
        
    def increment(flag):
        if(flag): return 1;
        else: return 0;

    # Collect events until released
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
    