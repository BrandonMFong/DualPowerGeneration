#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
import RPi.GPIO as GPIO
#import pynput # This is for simulations
import MaxPower_Classes
import System
import time
import threading
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from XML import xmlreader
from random import random
from adafruit_ads1x15.analog_in import AnalogIn

xmlreader = xmlreader();

# Below is just for simulation purposes
#class Keyboard_IO:

#    def call_rpm(key):
#        if System.timer_flag: 
#            MaxPower_Classes.total_rpm = 0;
#            return exit();
#        MaxPower_Classes.Max_Power_Wind.Get_RPM(); # calls this function to increment

#    def RPM_Listener():
#        with Listener(on_press=Keyboard_IO.call_rpm) as input:
#            input.join()


# TODO delete
class Random_IO:
    def BLADE_FORCE_listener():
        return random();

    def SOLAR_CURR_listener():
        return random();

    def SOLAR_VOLT_listener():
        return random();

#https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
#https://www.raspberrypi.org/documentation/usage/gpio/
# Error reading SSH protocol banner[Errno 104] Connection reset by peer

class RPI_Handler:
    def init(self):
        ## INFRARED INIT
        # Input GPIO pins
        global InfraredInput;
        InfraredInput = xmlreader.int('InfraredInputPin');
        # GPIO.setmode(GPIO.BOARD);
        GPIO.setup(InfraredInput, GPIO.IN, pull_up_down=GPIO.PUD_DOWN);

        # Output GPIO pins
        global AckBitForInfraredRead
        AckBitForInfraredRead = xmlreader.int('AckBitForInfraredReadPin');
        # GPIO.setmode(GPIO.BOARD);
        GPIO.setup(AckBitForInfraredRead, GPIO.OUT, initial=GPIO.LOW);

        # Adding event
        GPIO.add_event_detect(InfraredInput, GPIO.RISING);  
        GPIO.add_event_callback(InfraredInput, self.AckBitTurnOnLED);

        ## ADC INIT (Adafruit source code)
        # Create the I2C bus
        i2c = busio.I2C(board.SCL, board.SDA);

        # Create the ADC object using the I2C bus
        ads = ADS.ADS1015(i2c);
    
    def CleanupRPi():
        GPIO.cleanup(); 

    # INFRARED
    def ReadInfrared(): # read function
        while True: # while loop to constantly read the RPi.GPIO pin of the rpi
            if GPIO.input(InfraredInput): #if pin is high then increment
                #similar to the keyboard listener
                if System.timer_flag: # when timer is up
                    MaxPower_Classes.total_rpm = 0;
                    return exit();
                MaxPower_Classes.Max_Power_Wind.Get_RPM(); # calls this function to increment
            time.sleep(0.1);
    
    # This has a terrible latency
    def AckBitTurnOnLED(self):
        GPIO.output(AckBitForInfraredRead, 1);
        time.sleep(0.1);
        GPIO.output(AckBitForInfraredRead, 0);

    # ANALOG TO DIGITAL CONVERTER
    # ***The following is based on Adafruit source code***
    def ReadIO(Port):

        # Create single-ended input on channel 0
        chan = AnalogIn(ads, Port);

        return chan.voltage;

