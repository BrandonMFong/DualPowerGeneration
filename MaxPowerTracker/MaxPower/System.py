#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import time

def init():
    # Delcare
    global Seconds, File, delay, Max_Lines, Log;

    # Initialize
    # This will create Max_Lines, 1 line every Seconds passes
    # Max_Lines * Seconds will pass
    Seconds = 3; 
    File = 0;
    Log = 0;
    delay = 1; 
    Max_Lines = 3;

# Counts to Seconds
def timer():
    i = 0;
    global timer_flag;
    timer_flag = False;
    while i < Seconds:
        time.sleep(delay);
        i = i + 1;
        print("Time: {} seconds\n" .format(i));
    timer_flag = True;

class Client:
    ID = 1000; # Hard coding, TODO figure out a way to figure out client by device.  OS ip address? 