#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from XML import xmlreader
import os
import time

def init():
    # Delcare
    global Seconds, File, delay, MaxLines, Log;

    # Initialize
    # This will create MaxLines, 1 line every Seconds passes
    # MaxLines * Seconds will pass
    Seconds = xmlreader.int('SecondsToCountForEachLine');
    File = 0;
    Log = 0;
    delay = xmlreader.int('delay');
    MaxLines = xmlreader.int('MaxLinesForEachCSVFile');

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
    ID = xmlreader.int('ClientID'); # Hard coding, TODO figure out a way to figure out client by device.  OS ip address? 