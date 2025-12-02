#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

def cupGrab(cupNumber):
    #Move both motors foward, turn 90deg        AHHHHH!!!!!
    #Measure cup location and go to it
    locateCup()
    #Deside color of cup
    #Put cup in correct location, get positioned for next cup

def locateCup():
    #Use pixy cam to find cup!!!!

    dist = 999
    while dist > 10:
        move(1)
        #locate cup with pixy cam
        dist = 000 #placeholder for distance from pixy cam
        cuplocations = []
        cuplocations.append(dist)
        if (len(cuplocations) > 10):
            cuplocations.pop(0)
        #Average cup location
        avgLocation = sum(cuplocations) / len(cuplocations)


def move(speed):
    #Move motor one
    #Move motor twolksdflkjsdlkjflk
    pass

def turn(angle):    # Positive is CW and Negative is CCW
    #Turn robot to angle
    pass