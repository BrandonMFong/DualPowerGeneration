#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

# How to test if a file/directory exists https://www.guru99.com/python-check-if-file-exists.html & https://stackabuse.com/creating-and-deleting-directories-with-python/
# How to create a file https://www.guru99.com/reading-and-writing-files-in-python.html

# Current Workflow:
# 1. Creates file
# 2. Calls a function to write into a file
# 3. Calles a function to close the file
# I.E. Init_File() -> Inject_Data() -> Close_File() 

### LIBRARIES ###
from System import Client
import datetime
import os
import System

class File_Handler:
    def Init_File(): # function to create a file

        Date_and_Time = datetime.datetime.now(); # gets current date and time

        # This path below may change depending on where the script is in the raspberry pi
        # This ignored in git repo
        makepath = "../../FTP" # defines where the file will be imported

        if(not (os.path.isdir(makepath))): # if that directory doesn't exist, create it
            try:
                os.mkdir(makepath) #mkdir cmd 
            except OSError:
                print("Creation of the directory %s failed" % makepath) # Unsuccessful
            else:
                print("Successfully created the directory %s " % makepath) # Successful
        else:
            print("FTP already exits.");
        # Creates the file to be injected by our power tracker
        # This will be sent through FTP via script to our remote server
        filename = makepath + "/maxpower_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + ".csv"; 
        try:
            System.File = open(filename,"w+"); # this file is global
        except OSError:
            print("Creation of file %s failed." % filename);
            return 1;
        else:
            print("Successfully created file: %s" % filename);
            return 0;

    def Inject_Data(wind_data, solar_data):
        Date_and_Time = datetime.datetime.now(); # gets current date and time
        try:
            System.File.write("{}, {}, {}, {}\n" .format(Client.ID,
                Date_and_Time.strftime("%Y-%m-%d %H:%M:%S"), wind_data, solar_data));
        except OSError:
            print("Writing of file failed\n");
            return 1;
        else:
            print("Writing successful\n");
            return 0;

    def Close_File():
        System.File.close();
        System.File = 0; # clear variable

# This is meant for debugging purposes
# When you don't have the terminal up, you can view the logs to check the outputs
class Log_Handler:
    def Init_File(): # function to create a file

        Date_and_Time = datetime.datetime.now(); # gets current date and time

        # This path below may change depending on where the script is in the raspberry pi
        # This ignored in git repo
        makepath = "../../logs/MaxPower" # defines where the file will be imported

        if(not (os.path.isdir(makepath))): # if that directory doesn't exist, create it
            try:
                os.mkdir(makepath) #mkdir cmd 
            except OSError:
                print("Creation of the directory %s failed" % makepath) # Unsuccessful
            else:
                print("Successfully created the directory %s " % makepath) # Successful
        else:
            print("logs already exits.");
        # Creates the file to be injected by our power tracker
        # This will be sent through FTP via script to our remote server
        filename = makepath +  "/MaxPowerLog_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + ".log"; 
        try:
            System.Log = open(filename,"w+"); # this file is global
        except OSError:
            print("Creation of file %s failed." % filename);
            return 1;
        else:
            print("Successfully created file: %s" % filename);
            return 0;

    def Write_Log(string):
        try:
            System.Log.write(string);
        except OSError:
            print("Writing log failed\n");
            return 1;
        else:
            return 0;

    def Close_File():
        System.Log.close();
        System.Log = 0; # clear variable
        print("\nMaintenance check in \\logs\\MaxPower.  Delete files if space is needed");
        # TODO zip folders or delete to save space

