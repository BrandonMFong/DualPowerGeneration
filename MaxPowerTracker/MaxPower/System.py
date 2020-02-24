#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from XML import xmlreader
import os
import time


SystemXML = xmlreader();
def init():
    # Delcare
    global Seconds, File, delay, MaxLines, Log;

    # Initialize
    # This will create MaxLines, 1 line every Seconds passes
    # MaxLines * Seconds will pass
    Seconds = SystemXML.int('SecondsToCountForEachLine');
    File = 0;
    Log = 0;
    delay = SystemXML.int('delay'); # using in torque and solar
    MaxLines = SystemXML.int('MaxLinesForEachCSVFile');

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
    ID = SystemXML.int('ClientID'); 

