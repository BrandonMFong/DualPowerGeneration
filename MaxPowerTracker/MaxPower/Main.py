# Property by Your Engineering Solutions (Y.E.S.)
# Engineers: Lorans Hirmez, Brandon Fong


#In this section, we need to get IO from tachometer
# TODO figure out how to interface with GPIO RPI with pyhton
from random import random # for the random function
from MaxPower_Classes import Max_Power_Wind # importing the class
from Files import File

#  Variables, no data type declaration needed
n = 60;
total_torque = 0;

# This creates a file in a directory outside of our git repo named \FTP
# For debugging please check if the file is created
# file holds the instance of what was created
if File.Init_File(Average_POWER_WIND, Average_POWER_SOLAR):
    file = File.Init_File(Average_POWER_WIND, Average_POWER_SOLAR);
else:
    print("File.Init_File returned 0 (Error)");

Average_RPM_Wind = Max_Power_Wind.Avg_RPM(Max_Power_Wind.Get_RPM(), n);
print("Average RPM: ", Average_RPM);


Average_TORQUE_Wind = Max_Power_Wind.Avg_Torque(Max_Power_Wind.Get_Torque(), n);
print("Average Torque: ", Average_TORQUE);

# Getting Average Power per minute
Average_POWER_WIND = Max_Power_Wind.Avg_Pwr(Average_TORQUE_Wind, Average_RPM_Wind);
print("Average Power per minute: ", Average_POWER_WIND);

Average_POWER_SOLAR = 0; # TODO make solar function

# Writes data into the file
File.Inject_Data(file, Average_POWER_WIND, Average_POWER_SOLAR);

