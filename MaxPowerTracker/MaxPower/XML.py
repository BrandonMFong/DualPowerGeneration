
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################


### LIBRARIES ###
from xml.dom import minidom
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
