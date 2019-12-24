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
    global Max_Lines;

    # Initialize
    # This will create Max_Lines, 1 line every Seconds passes
    # Max_Lines * Seconds will pass
    Seconds = 60; 
    File = 0;
    delay = 1; 
    Max_Lines = 10;

# Counts to Seconds
def timer():
    i = 0;
    global timer_flag;
    timer_flag = False;
    while i < Seconds:
        time.sleep(delay);
        i = i + 1;
        print("Time: ", i);
    timer_flag = True;

class Client:
    ID = 1000; # Hard coding, TODO figure out a way to figure out client by device.  OS ip address? 

