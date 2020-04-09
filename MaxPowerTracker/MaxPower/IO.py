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

IOXml = xmlreader();

# TODO delete 
class Random_IO:
    def BLADE_FORCE_listener():
        return random();

    def SOLAR_CURR_listener():
        return random();

class RPI_Handler:
    def init(self):

        # Input GPIO pins
        global InfraredInput;
        InfraredInput = IOXml.int('InfraredInputPin');
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(InfraredInput, GPIO.IN, pull_up_down=GPIO.PUD_DOWN);

        # Output GPIO pins
        global AckBitForInfraredRead
        AckBitForInfraredRead = IOXml.int('AckBitForInfraredReadPin');
        GPIO.setmode(GPIO.BCM);
        GPIO.setup(AckBitForInfraredRead, GPIO.OUT, initial=GPIO.LOW);

        # Adding event
        GPIO.add_event_detect(InfraredInput, GPIO.RISING);  
        GPIO.add_event_callback(InfraredInput, self.AckBitTurnOnLED);

        ## ADC INIT (Adafruit source code)
        i2c = busio.I2C(board.SCL, board.SDA);

        # Create the ADC object using the I2C bus
        global ads;
        ads = ADS.ADS1015(i2c);
    
    def CleanupRPi():
        GPIO.cleanup(); 

    # INFRARED
    # Reads infrared device
    def ReadInfrared():
        while True:
            if System.timer_flag:
                MaxPower_Classes.total_rpm = 0;
                return exit();
            if GPIO.input(InfraredInput):
                MaxPower_Classes.Max_Power_Wind.Get_RPM();
            time.sleep(IOXml.float("InfraredReadInterval"));
    
    # This has a terrible latency
    # This does not work, LED might have blown out
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