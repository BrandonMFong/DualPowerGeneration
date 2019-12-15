# Property by Your Engineering Solutions (Y.E.S.)
# Engineers: Lorans Hirmez, Brandon Fong

# How to test if a file/directory exists https://www.guru99.com/python-check-if-file-exists.html & https://stackabuse.com/creating-and-deleting-directories-with-python/
# How to create a file https://www.guru99.com/reading-and-writing-files-in-python.html

# Current Workflow:
# 1. Creates file
# 2. Calls a function to write into a file
# 3. Calles a function to close the file
# I.E. Init_File() -> Inject_Data() -> Close_File() 

import datetime
import os

class File:

    def Init_File(wind_data, solar_data): # function to create a file
        Date_and_Time = datetime.datetime.now(); # gets current date and time

        # This path below may change depending on where the script is in the raspberry pi
        makepath = "../../../FTP" # defines where the file will be imported

        if(not (os.path.isdir(makepath))): #if that directory doesn't exist, create it
            try:
                os.mkdir(makepath) #mkdir cmd 
            except OSError:
                print ("Creation of the directory %s failed" % makepath) # Unsuccessful
            else:
                print ("Successfully created the directory %s " % makepath) # Successful
        
        # Creates the file to be injected by our power tracker
        # This will be sent through FTP via script to our remote server
        filename = makepath + "/maxpower_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + ".csv"; 
        try:
            file = open(filename,"w+");
        except OSError:
            print("Creation of file %s failed." % filename);
            return 0;
        else:
            print("Successfully created file: %s" % filename);
            return file;

    def Inject_Data(file, wind_data, solar_data):
        file.write("DATETIME, {}, {}" .format(wind_data, solar_data));
        return 0;

    def Close_File(file):
        f.close();

    # debugging
    def printtime(Date_and_Time):
        print(Date_and_Time);