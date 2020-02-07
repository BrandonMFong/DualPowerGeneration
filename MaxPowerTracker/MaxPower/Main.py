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
from MaxPower_Classes import Max_Power_Wind, Max_Power_Solar 
import MaxPower_Classes
import System 
import threading 
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
    if File_Handler.Init_File(): print("File.File_Handler.Init_File returned 1 \n");
    else: print("File.File_Handler.Init_File() returned 0 \n");

    # This creates the log file at DualPowerGeneration\logs
    if Log_Handler.Init_File(): print("File.Log_Handler.Init_File returned 1 \n");
    else: print("File.Log_Handler.Init_File() returned 0 \n");

    print("Entering loop\n");
    
    i = 0;
    # Main loop
    while i < System.Max_Lines:
        ### TIMER ### 
        THREAD_Timer = threading.Thread(target=System.timer);
        
        ### WIND ###
        THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);

        ### SOLAR ###
        THREAD_Max_Power_Solar_Get_SOLAR_POWER = threading.Thread(target=Max_Power_Solar.Get_Solar_Power);

        # Starts threading the functions
        THREAD_Timer.start();
        THREAD_Max_Power_Wind_Get_TORQUE.start();
        THREAD_Max_Power_Solar_Get_SOLAR_POWER.start();

        # This waits until the above threading is finished
        IO.Keyboard_IO.RPM_Listener(); # join thread, TODO 
        THREAD_Timer.join();
        THREAD_Max_Power_Wind_Get_TORQUE.join();
        THREAD_Max_Power_Solar_Get_SOLAR_POWER.join();

        # Sub calculations for Wind Power
        print("\nAverage RPM: ", MaxPower_Classes.Average_RPM_Wind);print("\n"); 
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage RPM: {} \n" .format(MaxPower_Classes.Average_RPM_Wind));
        print("\nAverage Torque: ", MaxPower_Classes.Average_TORQUE_Wind);print("\n");
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage Torque: {} \n" .format(MaxPower_Classes.Average_TORQUE_Wind));

        # Getting Average Power per minute
        Max_Power_Wind.Avg_Pwr(MaxPower_Classes.Average_TORQUE_Wind, MaxPower_Classes.Average_RPM_Wind); # This needs to be called from the main
        print("\nAverage Power per minute for WIND: ", MaxPower_Classes.Average_POWER_WIND);print("\n");
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage Power per minute for WIND: {} \n" .format(MaxPower_Classes.Average_POWER_WIND));
        Max_Power_Solar.Avg_Pwr(MaxPower_Classes.total_solar_pwr); # Get's the total solar power and gets its average across a minute
        print("\nAverage Power per minute for SOLAR: ", MaxPower_Classes.Average_POWER_SOLAR);print("\n");
        Log_Handler.Write_Log(os.path.basename(__file__) + "\nAverage Power per minute for SOLAR: \n" .format(MaxPower_Classes.Average_POWER_SOLAR));

        # Writes data into the file
        File_Handler.Inject_Data(MaxPower_Classes.Average_POWER_WIND, MaxPower_Classes.Average_POWER_SOLAR); # doesn't write an extra line
        print("\n Total lines in file: {} \n" .format(i+1));
        Log_Handler.Write_Log(os.path.basename(__file__) + "\n Total lines in file: {} \n" .format(i+1));
        i = i + 1;

    # Closes and saves file
    File_Handler.Close_File();
    Log_Handler.Close_File();

    # Move Files to FTP/archive folder
    Archive_Handler.ArchiveFiles();
    
    Sender.send_using_batch(); # Runs script to send via ftp

    

