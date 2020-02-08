
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

<<<<<<< HEAD

### LIBRARIES ###
from xml.dom import minidom
=======
### LIBRARIES ###
from xml.dom import minidom
import xml.etree.ElementTree as ET # https://docs.python.org/3.3/library/xml.etree.elementtree.html

>>>>>>> dev/Max_Power_Tracker/Feature/BF-ConfigFiles
CLIENT = 'EarthWindFire';
XMLPath = '../../Config/' + CLIENT + '/MaxPower.xml';
reader = minidom.parse(XMLPath);

class xmlreader:
    def int(value):
        return int((reader.getElementsByTagName(value))[0].firstChild.data);

    def string(value):
        return str((reader.getElementsByTagName(value))[0].firstChild.data);

    def double(value):
        return double((reader.getElementsByTagName(value))[0].firstChild.data);
