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
from XML import xmlreader
import datetime
import os
import System
import shutil

FilesXML = xmlreader();
FTPDir = FilesXML.string('DirectoryForOutboundFTPFiles'); 
LogForMaxPowerDir = FilesXML.string('DirectoryForMaxPowerLogFiles');
FTPArchiveDir = FilesXML.string('ArchiveForOutboundFTPFiles');
LOGArchiveDir = FilesXML.string('ArchiveForMaxPowerLogFiles');
FTPFileType = FilesXML.string('FileTypeForFTP');
LOGFileType = FilesXML.string('FileTypeForLogs');
ZipExtension = FilesXML.string('FileTypeForZippedFolder');
ZippedFTP = FilesXML.string('ZippedFTP');
ZippedLog = FilesXML.string('ZippedLog');

# Makes directory if it does not exist
def MakeDir(makepath):
    if(not (os.path.isdir(makepath))): 
            try:
                os.mkdir(makepath)
            except OSError:
                print("\nCreation of the directory %s failed" % makepath);
            else:
                print("\nSuccessfully created the directory %s " % makepath);
    else:
        print("\nDirectory %s already exits.\n" % makepath);


# .csv files
class File_Handler:

    # Creates .csv file
    def Init_File():

        Date_and_Time = datetime.datetime.now();
        MakeDir(FTPDir);

        global filename;
        global fullpath;
        filename = "/maxpower_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + FTPFileType;
        fullpath = FTPDir + filename; 
        try:
            # Puts file pointer to global var in System.py
            System.File = open(fullpath,"w+"); 
        except OSError:
            print("Creation of file %s failed." % fullpath);
            return 1;
        else:
            print("Successfully created file: %s" % fullpath);
            return 0;

    # Writes into file
    def Inject_Data(wind_data, solar_data):
        Date_and_Time = datetime.datetime.now();
        try:
            System.File.write("{}, {}, {}, {}\n" .format(Client.ID,
                Date_and_Time.strftime("%Y-%m-%d %H:%M:%S"), wind_data, solar_data));
        except OSError:
            print("\nWriting of file failed\n");
            return 1;
        except AttributeError as ex:
            print("in file");
            print(ex);
        else:
            print("\nWriting successful\n");
            return 0;

    def Close_File():
        System.File.close();
        System.File = 0; # clear variable
        print("\n\nSEE IF FILE IS STILL HERE AFTER CLOSE\n\n");
        os.listdir(FTPDir);
        print("\n\nArchive dir\n\n");
        os.listdir(FTPArchiveDir);

# .log files
class Log_Handler:
    
    # Creates .log file
    def Init_File():

        Date_and_Time = datetime.datetime.now();
        MakeDir(LogForMaxPowerDir);

        Logfilename = LogForMaxPowerDir +  "/MaxPowerLog_" + Date_and_Time.strftime("%m%d%Y_%H%M%S") + LOGFileType;
        try:
            # Puts file pointer to global var in System.py
            System.Log = open(Logfilename,"w+");
        except OSError:
            print("\nCreation of file %s failed." % Logfilename);
            return 1;
        else:
            print("\nSuccessfully created file: %s" % Logfilename);
            return 0;

    def Write_Log(string):
        try:
            System.Log.write(string);
        except OSError:
            print("\nWriting log failed\n");
            return 1;
        except AttributeError as ex:
            print("in log");
            print(ex);
        else:
            return 0;

    def Close_File():
        System.Log.close();
        System.Log = 0; # clear variable
        print("\nMaintenance check in \\logs\\MaxPower.  Delete files if space is needed");
        

# Archive files
class Archive_Handler:
    def ArchiveFiles():

        MakeDir(FTPArchiveDir);
        MakeDir(LOGArchiveDir);
        MakeDir(ZippedFTP);
        MakeDir(ZippedLog);

        ## MOVES ##

        # In FTP Folder
        FTPFiles = os.listdir(FTPDir);
        for f in FTPFiles:
            if f.endswith(FTPFileType):
                FilePath = FTPDir + "/" + f;
                shutil.move(FilePath, FTPArchiveDir);
                print("\nMoved %s to archive folder\n" % f);

        # In logs\MaxPower Folder
        LOGFiles = os.listdir(LogForMaxPowerDir);
        for f in LOGFiles:
            if f.endswith(LOGFileType):
                FilePath = LogForMaxPowerDir + "/" + f;
                shutil.move(FilePath, LOGArchiveDir);
                print("\nMoved %s to archive folder\n" % f);
            
        ## ZIPS ##

        # In FTP archive Folder
        FTPArchivedFiles = os.listdir(FTPArchiveDir);
        if (FTPArchivedFiles.__len__()) > 10:
            print("\nBeginning to zip files in %s\n" % FTPArchiveDir)
            filename = ZippedFTP +  "/Archive_" + datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ZipExtension; 
            zipper = ZipFile(filename, 'w');
            for f in FTPArchivedFiles:
                if f.endswith(FTPFileType):
                    FilePath = FTPArchiveDir + "/" + f;
                    zipper.write(FilePath);
                    os.remove(FilePath);
            zipper.close();
            print("\nZipped files in %s\n" % FTPArchiveDir);

        # In logs\MaxPower archive Folder
        LOGArchivedFiles = os.listdir(LOGArchiveDir);
        if (LOGArchivedFiles.__len__()) > 10:
            print("\nBeginning to zip files in %s\n" % LOGArchiveDir)
            filename = ZippedLog +  "/Archive_" + datetime.datetime.now().strftime("%m%d%Y_%H%M%S") + ZipExtension; 
            zipper = ZipFile(filename, 'w');
            for f in LOGArchivedFiles:
                if f.endswith(LOGFileType):
                    FilePath = LOGArchiveDir + "/" + f;
                    zipper.write(FilePath);
                    os.remove(FilePath);
            zipper.close();
            print("\nZipped files in %s\n" % LOGArchiveDir);
        
