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

CUP_PLACEMENT = 0.5
CUP_TOLERANCE = 50
ANGLE_CHECK_TOLERANCE = 950
SPEED = 50
TURN_SPEED = 20
LOST_ANGLE_RANGE = 60
ANGLE_RANGE = 80

# Create your objects here.
ev3 = EV3Brick()
USS = UltrasonicSensor(Port.S4)
motorL = Motor(Port.A)
motorR = Motor(Port.D)
motorC = Motor(Port.C)



#           ------Functions------

def cupGrab(cupNumber):
    #Move both motors foward, turn 90deg
    #Measure cup location and go to it
    GoTOCup()
    #Deside color of cup
    #Put cup in correct location, get positioned for next cup


def GoTOCup():
    
    LocateCup(ANGLE_RANGE)

    distance = 9999

    #*
    #while (USS.distance() - CUP_PLACEMENT) > CUP_TOLERANCE:
        #distance = USS.distance()
        #if distance > ANGLE_CHECK_TOLERANCE:
        #    LocateCup(10)
        #move(1)
    dist = USS.distance()
    while dist > CUP_TOLERANCE:
       dist = USS.distance()
       if dist > ANGLE_CHECK_TOLERANCE:
           if not AngleBounce(False, 0):
               LocateCup(LOST_ANGLE_RANGE)

       print("Moving Toward Cup: {}", dist)
       move()

    stop()
    

def LocateCup(angleAmt):
    angleTrack = angleAmt
    angleAtMin = 999
    smallestDist = 9999

    # Set up to start at side
    i = 0
    while i < angleAmt:
        turn(True)
        i = i + 1

    #Sweep from side to side to find smallest distance
    while angleTrack > -angleAmt:
        distance = USS.distance()

        # Check if we've lost the cup
        if distance < smallestDist:
            smallestDist = distance
            angleAtMin = angleTrack
        
        turn(False)
        angleTrack -= 1

        print("Smallest Dist: {}, Angle of Min Dist: {}", smallestDist, angleAtMin)

    # Go to found smallest distance
    while angleTrack < angleAtMin:
        turn(True)
        angleTrack += 1


def AngleBounce(goNoGo, count):
    distance = USS.distance()
    if distance > ANGLE_CHECK_TOLERANCE:
        print ("Bounced!!!!!                    Curr Dist: {}", distance)
        if count < 5:
            AngleBounce(False, count + 1)
            return False
        else:
            return False
    else:
        return True




def move(Forward = True):
    if Forward:
        motorL.dc(SPEED)
        motorR.dc(SPEED)
    else:
        motorL.dc(-SPEED)
        motorR.dc(-SPEED)


def turn(DirCW):    # Positive is CW and Negative is CCW
    i = 0
    angle = 2
    while i < abs(angle):
        if (DirCW):
            motorL.dc(-TURN_SPEED)
            motorR.dc(TURN_SPEED)
        else:
            motorR.dc(-TURN_SPEED)
            motorL.dc(TURN_SPEED)
        i = i + 1
        wait(10)

    motorL.dc(0)
    motorR.dc(0)

def grab(grab):
    if grab:
        motorC.run_angle(500, -50)
    else:
        motorC.run_angle(500, 50)

def stop():
    motorL.dc(0)
    motorR.dc(0)

#           ------Main Function------
#grab(False)
stop()

cupGrab(1)
grab(True)
wait(1500)
#grab(False)
#stop()

i = 0
while i < 100:
    move(False)
    wait(20)
    i = i + 1

stop()
grab(False)
stop()
