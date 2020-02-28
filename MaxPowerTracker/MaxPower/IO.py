#####################################################
# Property by Your Engineering Solutions (Y.E.S.)   #
# Engineers: Lorans Hirmez, Brandon Fong            #
#####################################################

### LIBRARIES ###
# TODO use the following library to simulate the rotation of the blades to calculate rpm 
# from pynput.keyboard import Key, Listener # https://pythonhosted.org/pynput/keyboard.html
import RPi.GPIO as GPIO
#import pynput
import MaxPower_Classes
import System
import threading
from XML import xmlreader
from random import random

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

class Random_IO:
    def BLADE_FORCE_listener():
        return random();

    def SOLAR_CURR_listener():
        return random();

    def SOLAR_VOLT_listener():
        return random();

#https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api
#https://www.raspberrypi.org/documentation/usage/gpio/
class RPI_Handler:
    def init():
        GPIO.setup(xmlreader.int('InfraredInputPin'), GPIO.IN);

    def ReadInfrared(): # read function
        while True: # while loop to constantly read the gpio pin of the rpi
            if GPIO.input(xmlreader.int('InfraredInputPin')): #if pin is high increment
                #similar to the keyboard listener
                if System.timer_flag: # when timer is up
                    MaxPower_Classes.total_rpm = 0;
                    return exit();
                MaxPower_Classes.Max_Power_Wind.Get_RPM(); # calls this function to increment