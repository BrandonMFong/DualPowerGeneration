
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import subprocess, sys, os
from subprocess import call 

global file_basename;
file_basename = '..\\..\\Scripts\\FTP';
class FTP:
    @staticmethod # Declaring that this method is static 
    def send_using_powershell():
        file = file_basename + '.ps1';
        p = subprocess.Popen(["powershell.exe", "{}".format(file)], stdout=sys.stdout);
        p.communicate();

    @staticmethod
    def send_using_batch():
        file = file_basename + '.bat';
        try:
            os.system('cmd /c {}' .format(file));
        except Exception as ex:
            print(ex);
            print("Something wrong and there is nothing that can solve this at the moment");
            print("File not sent through ftp");
            
    @staticmethod
    def send_using_cmd():
        file = file_basename + '.cmd'; # this only runs batch files, but what is a .cmd file?
        try:
            os.system('cmd /c {}' .format(file));
        except Exception as ex:
            print(ex);
            print("Something wrong and there is nothing that can solve this at the moment");
            print("File not sent through ftp");

    #@staticmethod 
    #def send_using_cmd():
    #    dir = r"{}".format(file_basename);
    #    cmdline = "FTP.bat"
    #    rc = call(cmdline, cwd=dir) # run `cmdline` in `dir`