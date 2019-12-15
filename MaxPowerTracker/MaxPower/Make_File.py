# Property by Your Engineering Solutions (Y.E.S.)
# Engineers: Lorans Hirmez, Brandon Fong

# How to test if a file/directory exists https://www.guru99.com/python-check-if-file-exists.html & https://stackabuse.com/creating-and-deleting-directories-with-python/
# How to create a file https://www.guru99.com/reading-and-writing-files-in-python.html
import datetime
import os

class Make_File:

    def Init_File(self, wind_data, solar_data): # function to create a file
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
            f = open(filename,"w+");
        except OSError:
            print("Creation of file %s failed." % filename);
        else:
            print("Successfully created file: %s" % filename);

        # Calls the function to write into the file
        self.Inject_Data(wind_data, solar_data); # error here

    def Inject_Data(wind_data, solar_data):
        f.write("test");
        return 0;

    def Close_File():
        f.close();

    # debugging
    def printtime(Date_and_Time):
        print(Date_and_Time);