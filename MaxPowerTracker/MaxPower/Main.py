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
import threading # Allows to run two functions at the same time http://blog.acipo.com/python-threading-arguments/
# TODO reading torque and rpm should be timed (https://stackoverflow.com/questions/13293269/how-would-i-stop-a-while-loop-after-n-amount-of-time)

# Init
System.init();
Max_Power_Objects.init();


while True:
    # This creates a file in a directory outside of our git repo named \FTP
    # NOTE: For debugging please check if the file is created
    if not File_Handler.Init_File():
        print("File.Init_File() returned 0 (Success)");
    else:
        print("File.Init_File returned 1 (Error)");

    # This is the job to run calculations and inject the data into a file
    while True:
        ### WIND ###
        # Creates and object to thread the two functions
        # Threading allows us to run these two functions at the same time
        THREAD_Max_Power_Wind_Get_RPM = threading.Thread(target=Max_Power_Wind.Get_RPM);
        THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);

        # Starts threading the functions
        THREAD_Max_Power_Wind_Get_RPM.start(); 
        THREAD_Max_Power_Wind_Get_TORQUE.start();

        # This waits until the above threading is finished
        THREAD_Max_Power_Wind_Get_RPM.join(); 
        THREAD_Max_Power_Wind_Get_TORQUE.join();


        print("\nAverage RPM: ", Max_Power_Objects.Average_RPM_Wind);print("\n");
        print("\nAverage Torque: ", Max_Power_Objects.Average_TORQUE_Wind);print("\n");

        # Getting Average Power per minute
        Max_Power_Wind.Avg_Pwr(Max_Power_Objects.Average_TORQUE_Wind, Max_Power_Objects.Average_RPM_Wind);
        print("\nAverage Power per minute: ", Max_Power_Objects.Average_POWER_WIND);print("\n");

        ### SOLAR ###
        Max_Power_Objects.Average_POWER_SOLAR = 0; # TODO make solar function

        # Writes data into the file
        # Error: not writing into files
        File_Handler.Inject_Data(Max_Power_Objects.Average_POWER_WIND, Max_Power_Objects.Average_POWER_SOLAR);
        File_Handler.Save_File();

    # After this you should run the script to send via FTP

    break;

