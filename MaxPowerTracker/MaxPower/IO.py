#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
import pynput
from pynput import keyboard
class Input_Output:
    # Thread start
    def start():
        listener = keyboard.Listener(
            on_press=on_press,
            on_release=on_release)
        listener.start()
        
    # Thread Join
    def join():
        # Collect events until released
        with keyboard.Listener(
                on_press=on_press,
                on_release=on_release) as listener:
            listener.join()

    def on_press(key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            return True;
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            return True;

    def on_release(key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False
    