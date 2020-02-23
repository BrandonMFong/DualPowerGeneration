
#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
from MaxPower_Classes import Max_Power_Wind, Max_Power_Solar 
import MaxPower_Classes
import System 
import threading 
import IO
#from EmulatorGUI import GPIO # simulates GPIO functions on rpi  

# Init
System.init();
MaxPower_Classes.init();


def do():
    ### TIMER ### 
    THREAD_Timer = threading.Thread(target=System.timer);
        
    ### WIND ###
    THREAD_Max_Power_Wind_Get_TORQUE = threading.Thread(target=Max_Power_Wind.Get_Torque);

    ### SOLAR ###
    THREAD_Max_Power_Solar_Get_SOLAR_POWER = threading.Thread(target=Max_Power_Solar.Get_Solar_Power);

    # Starts threading the functions
    THREAD_Timer.start();
    THREAD_Max_Power_Wind_Get_TORQUE.start();
    THREAD_Max_Power_Solar_Get_SOLAR_POWER.start();

    # This waits until the above threading is finished
    IO.Keyboard_IO.RPM_Listener(); # join thread, TODO 
    THREAD_Timer.join();
    THREAD_Max_Power_Wind_Get_TORQUE.join();
    THREAD_Max_Power_Solar_Get_SOLAR_POWER.join();