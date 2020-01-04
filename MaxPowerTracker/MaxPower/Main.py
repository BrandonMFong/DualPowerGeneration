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
from Files import File_Handler
import System 
import threading 
from FTP import FTP
import IO
#from EmulatorGUI import GPIO # simulates GPIO functions on rpi  

# Init
System.init();
MaxPower_Classes.init();
i = 0;
Sender = FTP();


while True:
    # This creates a file in a directory outside of our git repo named ..\FTP
    # NOTE: For debugging please check if the file is created
    if not File_Handler.Init_File():
        print("File.Init_File() returned 0 (Success)\n");
    else:
        print("File.Init_File returned 1 (Error)\n");

    print("Entering loop\n");
    
    i = 0;
    # Main loop
    while i < System.Max_Lines:
        ### WIND ###
        # Creates and object to thread the two functions
        # Threading allows us to run these two functions at the same time
        THREAD_Timer = threading.Thread(target=System.timer);
        THREAD_Max_Power_Wind_Get_RPM = threading.Thread(target=Max_Power_Wind.Get_RPM);
        THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);

        # Starts threading the functions
        THREAD_Timer.start();
        THREAD_Max_Power_Wind_Get_RPM.start(); 
        THREAD_Max_Power_Wind_Get_TORQUE.start();

        # This waits until the above threading is finished
        #IO.Keyboard_IO.start_io(); # this thread is taking precedence
        THREAD_Timer.join();
        THREAD_Max_Power_Wind_Get_RPM.join(); 
        THREAD_Max_Power_Wind_Get_TORQUE.join();

        print("\nAverage RPM: ", MaxPower_Classes.Average_RPM_Wind);print("\n");
        print("\nAverage Torque: ", MaxPower_Classes.Average_TORQUE_Wind);print("\n");

        # Getting Average Power per minute
        Max_Power_Wind.Avg_Pwr(MaxPower_Classes.Average_TORQUE_Wind, MaxPower_Classes.Average_RPM_Wind);
        print("\nAverage Power per minute: ", MaxPower_Classes.Average_POWER_WIND);print("\n");

        ### SOLAR ###
        MaxPower_Classes.Average_POWER_SOLAR = 0; # TODO make solar function

        # Writes data into the file
        File_Handler.Inject_Data(MaxPower_Classes.Average_POWER_WIND, MaxPower_Classes.Average_POWER_SOLAR); # doesn't write an extra line
        print("\n Total lines in file: {} \n" .format(i+1));
        i = i + 1;

    File_Handler.Close_File; # Closes and saves file
    
    Sender.send_using_batch(); # Runs script to send via ftp

    

