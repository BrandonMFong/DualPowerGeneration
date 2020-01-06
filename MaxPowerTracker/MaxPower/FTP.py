
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from subprocess import call 
from Files import Log_Handler
import subprocess, sys, os

global file_basename;
file_basename = '..\\..\\Scripts\\FTP';
class FTP:
    @staticmethod # Declaring that this method is static 
    def send_using_powershell():
        try:
            file = file_basename + '.ps1';
            p = subprocess.Popen(["powershell.exe", "{}".format(file)], stdout=sys.stdout);
            p.communicate();
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
        except Exception as ex:
            print(ex);
            print("File not sent through ftp");
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through powershell\n");
            
    @staticmethod
    def send_using_batch():
        file = file_basename + '.bat';
        try:
            os.system('cmd /c {}' .format(file));
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
        except Exception as ex:
            print(ex);
            print("File not sent through ftp");
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through batch\n");
            
    @staticmethod
    def send_using_cmd():
        file = file_basename + '.cmd';
        try:
            os.system('cmd /c {}' .format(file));
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
        except Exception as ex:
            print(ex);
            print("File not sent through ftp");
            Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through cmd\n");
            