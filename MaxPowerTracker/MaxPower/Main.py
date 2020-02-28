#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# In this section, we need to get IO from tachometer
# TODO figure out how to interface with GPIO RPI with pyhton
from FTP import FTP
from Files import File_Handler, Log_Handler, Archive_Handler
from random import random 
#from MaxPower_Classes import Max_Power_Wind, Max_Power_Solar 
import MaxPower_Classes
import System 
import threading 
import IO
import os
import ThreadFunctions
#from EmulatorGUI import GPIO # simulates GPIO functions on rpi  

# Init
System.init();
MaxPower_Classes.init();
i = 0;
Sender = FTP();
IO.RPI_Handler.init();

# Main loop
while True:
    # This creates a file in a directory inside our git repo named DualPowerGeneration\FTP
    # NOTE: For debugging please check if the file is created
    if File_Handler.Init_File(): print("Error making file \n");
    else: print("Success created file \n");

    # This creates the log file at DualPowerGeneration\logs
    if Log_Handler.Init_File(): print("Error making log \n");
    else: print("Success making log \n");

    print("Entering loop\n");
    
    i = 0;
    while i < System.MaxLines:

        ThreadFunctions.do();

        MaxPower_Classes.do(i);
        i = i + 1;

    # Closes and saves file
    File_Handler.Close_File();
    Log_Handler.Close_File();
    
    Sender.send(); # Runs script to send via ftp

    # Move Files to FTP/archive folder
    Archive_Handler.ArchiveFiles();
    