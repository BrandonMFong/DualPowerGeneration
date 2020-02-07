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
from zipfile import ZipFile
import datetime
import os
import System
import shutil

FTPDir = "../../FTP"; # defines where the file will be imported
LogForMaxPowerDir = "../../logs/MaxPower"; # defines where the file will be imported
FTPArchiveDir = "../../FTP/archive"; # defines where the file will be imported
LOGArchiveDir = "../../logs/MaxPower/archive";


def MakeDir(makepath):
    if(not (os.path.isdir(makepath))): # if that directory doesn't exist, create it
            try:
                os.mkdir(makepath) # mkdir cmd 
            except OSError:
                print("\nCreation of the directory %s failed" % makepath); # Unsuccessful
            else:
                print("\nSuccessfully created the directory %s " % makepath); # Successful
    else:
        print("\nDirectory %s already exits.\n" % makepath);

class File_Handler:
    def Init_File(): # function to create a file

        Date_and_Time = datetime.datetime.now(); # gets current date and time
        MakeDir(FTPDir);

        # Creates the file to be injected by our power tracker
        # This will be sent through FTP via script to our remote server
        filename = FTPDir + "/maxpower_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + ".csv"; 
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
            print("\nWriting of file failed\n");
            return 1;
        except AttributeError as ex:
            print(ex);
        else:
            print("\nWriting successful\n");
            return 0;

    def Close_File():
        System.File.close();
        System.File = 0; # clear variable

# This is meant for debugging purposes
# When you don't have the terminal up, you can view the logs to check the outputs
class Log_Handler:
    def Init_File(): # function to create a file

        Date_and_Time = datetime.datetime.now(); # gets current date and time
        MakeDir(LogForMaxPowerDir);

        # Creates the file to be injected by our power tracker
        # This will be sent through FTP via script to our remote server
        filename = LogForMaxPowerDir +  "/MaxPowerLog_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + ".log"; 
        try:
            System.Log = open(filename,"w+"); # this file is global
        except OSError:
            print("\nCreation of file %s failed." % filename);
            return 1;
        else:
            print("\nSuccessfully created file: %s" % filename);
            return 0;

    def Write_Log(string):
        try:
            System.Log.write(string);
        except OSError:
            print("\nWriting log failed\n");
            return 1;
        except AttributeError as ex:
            print(ex);
        else:
            return 0;

    def Close_File():
        System.Log.close();
        System.Log = 0; # clear variable
        print("\nMaintenance check in \\logs\\MaxPower.  Delete files if space is needed");
        

class Archive_Handler:
    # https://thispointer.com/python-how-to-create-a-zip-archive-from-multiple-files-or-directory/
    # https://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
    # https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python
    # https://stackoverflow.com/questions/42068699/moving-files-with-shutil-move
    # This is to ensure space on the device does not get backed up
    # I can either archive or delete

    def ArchiveFiles():

        MakeDir(FTPArchiveDir);
        MakeDir(LOGArchiveDir);

        # In FTP Folder
        CSVFiles = os.listdir(FTPDir);
        for f in CSVFiles:
            if f.endswith(".csv"):
                FilePath = FTPDir + "/" + f;
                shutil.move(FilePath, FTPArchiveDir);

        # In logs\MaxPower Folder
        LOGFiles = os.listdir(LogForMaxPowerDir);
        for f in LOGFiles:
            if f.endswith(".log"):
                FilePath = LogForMaxPowerDir + "/" + f;
                shutil.move(FilePath, LOGArchiveDir);

                


