#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

#In this section, we need to get IO from tachometer
# TODO figure out how to interface with GPIO RPI with pyhton
from random import random # for the random function
from MaxPower_Classes import Max_Power_Wind # importing the class
from MaxPower_Classes import Max_Power_Solar # importing the class
from MaxPower_Classes import Max_Power_Objects # importing the class
from Files import File_Handler # To create files ready for ftp
import System # Setting globals
from threading import Thread # TODO learn to execute 2 functions at a time

# Init
System.init();
Max_Power_Objects.init();

while True:
    # This creates a file in a directory outside of our git repo named \FTP
    # For debugging please check if the file is created
    # file holds the instance of what was created
    if not File_Handler.Init_File():
        print("File.Init_File() returned 0 (Success)");
    else:
        print("File.Init_File returned 1 (Error)");

    # This is the job to run calculations and inject the data into a file
    while True:
        # WIND 
        Max_Power_Wind.Avg_RPM(Max_Power_Wind.Get_RPM());
        print("\nAverage RPM: ", Max_Power_Objects.Average_RPM_Wind);print("\n");

        Max_Power_Wind.Avg_Torque(Max_Power_Wind.Get_Torque());
        print("\nAverage Torque: ", Max_Power_Objects.Average_TORQUE_Wind);print("\n");

        # Getting Average Power per minute
        Max_Power_Wind.Avg_Pwr(Max_Power_Objects.Average_TORQUE_Wind, Max_Power_Objects.Average_RPM_Wind);
        print("\nAverage Power per minute: ", Max_Power_Objects.Average_POWER_WIND);print("\n");

        # SOLAR
        Max_Power_Objects.Average_POWER_SOLAR = 0; # TODO make solar function

        # Writes data into the file
        File_Handler.Inject_Data(Max_Power_Objects.Average_POWER_WIND, Max_Power_Objects.Average_POWER_SOLAR);

    File_Handler.Close_File();
    # After this you should run the script to send via FTP

    break;

