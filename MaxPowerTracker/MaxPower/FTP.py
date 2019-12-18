
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import subprocess, sys

class FTP:
    @staticmethod # Declaring that this method is static 
    def send_using_powershell():
        p = subprocess.Popen(["powershell.exe", 
              "..\\..\\Scripts\\FTP.ps1"], 
              stdout=sys.stdout);
        p.communicate();

    @staticmethod # Declaring that this method is static 
    def send_using_batch():
        subprocess.call([r'..\\..\\Scripts\\FTP.bat'])