
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from subprocess import call 
#from Files import Log_Handler
from XML import xmlreader
from ftplib import FTP
import Files
import pysftp
import subprocess, sys, os

global file_basename;
file_basename = '..\\..\\Scripts\\FTP';
LocalFTPDir = xmlreader.string('OutboardDir'); # defines where to look to send files out
DestinationDir = xmlreader.string('DestinationDirectory');
Hostname = xmlreader.string('Hostaddress');
Username = xmlreader.string('Username');
Password = xmlreader.string('Password');
PrivateKey = xmlreader.string('PrivateKey')

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
        elif type == 'commandline':
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
        elif type == 'python':
            try:
                cnopts = pysftp.CnOpts();
                #cnopts.hostkeys.load(PublicKey);
                cnopts.hostkeys = None;
                # Establish connection
                with pysftp.Connection(host=Hostname, username=Username, password=Password, cnopts=cnopts, private_key=PrivateKey) as sftp: # temporarily chdir to allcode
                    dest = DestinationDir + Files.filename.replace("\\", "/");
                    sftp.put(Files.fullpath, dest);  	# upload file to allcode/pycode on remote
            except Exception as ex:
                print(ex);
        else:
            print("FTP procedure not defined.  Please check configuration on MaxPower.xml");
