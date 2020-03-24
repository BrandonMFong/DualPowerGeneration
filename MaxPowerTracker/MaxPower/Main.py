#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from FTP import FTP
from Files import File_Handler, Log_Handler, Archive_Handler
from random import random 
import MaxPower_Classes
import System 
import threading 
import IO
import os
import ThreadFunctions

Sender = FTP();

# Init
System.init();
MaxPower_Classes.init();
IO.RPI_Handler.init(IO.RPI_Handler);

# Main loop
while True:
    try:
        # .csv 
        if File_Handler.Init_File(): print("Error making file \n");
        else: print("Success created file \n");

        # .log
        if Log_Handler.Init_File(): print("Error making log \n");
        else: print("Success making log \n");

        print("Entering loop\n");
        
        i = 0;
        while i < System.MaxLines:

            ThreadFunctions.do(); # Threads

            MaxPower_Classes.do(i); # Functions for max power
            i = i + 1;

        # Closes and saves file
        File_Handler.Close_File();
        Log_Handler.Close_File();
        
        Sender.send(); # Runs script to send via ftp

        # Move Files to FTP/archive folder
        Archive_Handler.ArchiveFiles();
        
    except KeyboardInterrupt:
        IO.RPI_Handler.CleanupRPi();
        File_Handler.Close_File();
        Log_Handler.Close_File();
        print("Terminating code...");
        break; # Exit code
        