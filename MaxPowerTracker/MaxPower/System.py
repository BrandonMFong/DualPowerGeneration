#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
<<<<<<< HEAD
from xml.dom import minidom
from XML import xmlreader
=======
from XML import xmlreader
import os
>>>>>>> dev/Max_Power_Tracker/Feature/BF-ConfigFiles
import time

#xmlreader = minidom.parse('../../Config/EarthWindFire/MaxPower.xml');

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
<<<<<<< HEAD
    ID = xmlreader.int('ID'); # Hard coding, TODO figure out a way to figure out client by device.  OS ip address? 
=======
    ID = xmlreader.int('ClientID'); # Hard coding, TODO figure out a way to figure out client by device.  OS ip address? 
>>>>>>> dev/Max_Power_Tracker/Feature/BF-ConfigFiles
