#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# In this section, we need to get IO from tachometer
# TODO figure out how to interface with GPIO RPI with pyhton
from random import random 
from MaxPower_Classes import Max_Power_Wind, Max_Power_Solar 
import MaxPower_Classes
from Files import File_Handler, Log_Handler
import System 
import threading 
from FTP import FTP
import IO
import os
#from EmulatorGUI import GPIO # simulates GPIO functions on rpi  

# Init
System.init();
MaxPower_Classes.init();
i = 0;
Sender = FTP();

while True:
    # This creates a file in a directory inside our git repo named DualPowerGeneration\FTP
    # NOTE: For debugging please check if the file is created
    if File_Handler.Init_File():
        print("File.File_Handler.Init_File returned 1 \n");
    else:
        print("File.File_Handler.Init_File() returned 0 \n");

    # This creates the log file at DualPowerGeneration\logs
    if Log_Handler.Init_File():
        print("File.Log_Handler.Init_File returned 1 \n");
    else:
        print("File.Log_Handler.Init_File() returned 0 \n");

    print("Entering loop\n");
    
    i = 0;
    # Main loop
    while i < System.Max_Lines:
        # Creates and object to thread the two functions
        # Threading allows us to run these two functions at the same time
        ### WIND ###
        THREAD_Timer = threading.Thread(target=System.timer);
        THREAD_Max_Power_Wind_Get_RPM = threading.Thread(target=Max_Power_Wind.Get_RPM);
        THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);
        #THREAD_IO_Keyboard_Listener = threading.Thread(target=IO.Keyboard_IO.Keyboard_Listener);

        # Starts threading the functions
        THREAD_Timer.start();
        THREAD_Max_Power_Wind_Get_RPM.start(); 
        THREAD_Max_Power_Wind_Get_TORQUE.start();
        #THREAD_IO_Keyboard_Listener.start();

        # This waits until the above threading is finished
        IO.Keyboard_IO.Keyboard_Listener(); # join thread
        THREAD_Timer.join();
        THREAD_Max_Power_Wind_Get_RPM.join(); 
        THREAD_Max_Power_Wind_Get_TORQUE.join();
        #THREAD_IO_Keyboard_Listener.join();

        print("\nAverage RPM: ", MaxPower_Classes.Average_RPM_Wind);print("\n"); 
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage RPM: {} \n" .format(MaxPower_Classes.Average_RPM_Wind));
        print("\nAverage Torque: ", MaxPower_Classes.Average_TORQUE_Wind);print("\n");
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage Torque: {} \n" .format(MaxPower_Classes.Average_TORQUE_Wind));

        # Getting Average Power per minute
        Max_Power_Wind.Avg_Pwr(MaxPower_Classes.Average_TORQUE_Wind, MaxPower_Classes.Average_RPM_Wind);
        print("\nAverage Power per minute: ", MaxPower_Classes.Average_POWER_WIND);print("\n");
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage Power per minute: {} \n" .format(MaxPower_Classes.Average_POWER_WIND));

        ### SOLAR ###
        MaxPower_Classes.Average_POWER_SOLAR = 0; # TODO make solar function

        # Writes data into the file
        File_Handler.Inject_Data(MaxPower_Classes.Average_POWER_WIND, MaxPower_Classes.Average_POWER_SOLAR); # doesn't write an extra line
        print("\n Total lines in file: {} \n" .format(i+1));
        Log_Handler.Write_Log(os.path.basename(__file__) + "\n Total lines in file: {} \n" .format(i+1));
        i = i + 1;

    File_Handler.Close_File; # Closes and saves file
    
    Sender.send_using_batch(); # Runs script to send via ftp

    

