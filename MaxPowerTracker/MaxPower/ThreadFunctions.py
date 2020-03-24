
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from MaxPower_Classes import Max_Power_Wind, Max_Power_Solar 
from IO import RPI_Handler
import MaxPower_Classes
import System 
import threading 

# Init
System.init();
MaxPower_Classes.init();

# I do not want this thread to call any IO functions
# I think I have to though because ReadInfrared is an async event
def do():
    ### TIMER ### 
    THREAD_Timer = threading.Thread(target=System.timer);
        
    ### WIND ###
    THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);
    THREAD_Max_Power_Wind_Get_RPM = threading.Thread(target=RPI_Handler.ReadInfrared)

    ### SOLAR ###
    THREAD_Max_Power_Solar_Get_SOLAR_POWER = threading.Thread(target=Max_Power_Solar.Get_Solar_Power);

    # Starts threading the functions
    THREAD_Timer.start();
    THREAD_Max_Power_Wind_Get_TORQUE.start();
    THREAD_Max_Power_Wind_Get_RPM.start();
    THREAD_Max_Power_Solar_Get_SOLAR_POWER.start();

    # This waits until the above threading is finished
    THREAD_Timer.join();
    THREAD_Max_Power_Wind_Get_TORQUE.join();
    THREAD_Max_Power_Wind_Get_RPM.join();
    THREAD_Max_Power_Solar_Get_SOLAR_POWER.join();