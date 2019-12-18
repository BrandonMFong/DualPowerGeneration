#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import time

def init():
    # Delcare
    global Seconds;
    global File;
    global delay;

    # Initialize
    Seconds = 60;
    File = 0;
    delay = 1; # 1 second

# Counts to Seconds
def timer():
    i = 0;
    global timer_flag;
    timer_flag = False;
    while i < Seconds:
        time.sleep(1);
        i = i + 1;
    timer_flag = True;


