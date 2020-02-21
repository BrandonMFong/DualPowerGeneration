
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from subprocess import call 
from Files import Log_Handler
from XML import xmlreader
from ftplib import FTP
import subprocess, sys, os

global file_basename;
file_basename = '..\\..\\Scripts\\FTP';

class FTP:
    @staticmethod
    def send():
        type = xmlreader.string('WhichProcedureToUseForFTP');

        # POWERSHELL
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
        
        # BATCH
        elif type == 'batch':
            file = file_basename + '.bat';
            try:
                os.system('cmd /c {}' .format(file));
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
            except Exception as ex:
                print(ex);
                print("File not sent through ftp");
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through batch\n");
        
        # COMMAND PROMPT
        elif type == 'command line':
            file = file_basename + '.cmd';
            try:
                os.system('cmd /c {}' .format(file));
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n Sent file\n");
            except Exception as ex:
                print(ex);
                print("File not sent through ftp");
                Log_Handler.Write_Log(os.path.basename(__file__) + "\n\n" + ex + "\n\n File not sent through cmd\n");
        
        # PYTHON
        # refer https://stackoverflow.com/questions/68335/how-to-copy-a-file-to-a-remote-server-in-python-using-scp-or-ssh
        elif type == 'Python':
            # Establish connection
            PythonFTPHandler = FTP(xmlreader.string('Hostaddress'), 
                                   xmlreader.string('Username'), 
                                   xmlreader.string('Password')); # Reading from config

            Path = xmlreader.string('Username') + '@' + xmlreader.string('Hostaddress')
            subprocess.run(["scp", "foo.bar", "joe@srvr.net:/path/to/foo.bar"])

        else:
            print("FTP procedure not defined.  Please check configuration on MaxPower.xml");
