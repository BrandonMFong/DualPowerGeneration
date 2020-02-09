
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ### 
from subprocess import call 
from Files import Log_Handler
from XML import xmlreader
import subprocess, sys, os
import ftplib

global file_basename;
file_basename = '..\\..\\Scripts\\FTP';

class FTP:
    @staticmethod
    def send():
        type = xmlreader.string('WhichProcedureToUseForFTP');
        if type == 'powershell':
            try:
                file = file_basename + '.ps1';
                p = subprocess.Popen(["powershell.exe", "{}".format(file)], stdout=sys.stdout);
                p.communicate();
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
            except Exception as ex:
                print(ex);
                print("File not sent through ftp");
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through powershell\n");
        elif type == 'batch':
            file = file_basename + '.bat';
            try:
                os.system('cmd /c {}' .format(file));
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
            except Exception as ex:
                print(ex);
                print("File not sent through ftp");
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through batch\n");
        elif type == 'command line':
            file = file_basename + '.cmd';
            try:
                os.system('cmd /c {}' .format(file));
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
            except Exception as ex:
                print(ex);
                print("File not sent through ftp");
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through cmd\n");
        elif type == 'python':
            print('do something');
            # https://www.pythonforbeginners.com/code-snippets-source-code/how-to-use-ftp-in-python
            # This is going to be for python method.  Doing this will relieve the worry of linux environment on rpi
            # If I can ftp through here then that would be great  
        else:
            print("FTP procedure not defined.  Please check configuration on MaxPower.xml");
