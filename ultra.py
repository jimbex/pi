from gpiozero import DistanceSensor
from time import sleep
import time



def fr_left():
    u5 = DistanceSensor(echo=0, trigger=11)
    return u5.distance * 100
def front():
    u1 = DistanceSensor(echo=15, trigger=14)
    return u1.distance * 100
def fr_right():
    u4 = DistanceSensor(echo=9, trigger=10)
    return u4.distance * 100
def left():
    u2 = DistanceSensor(echo=25, trigger=8)
    return u2.distance * 100
def right():
    u3 = DistanceSensor(echo=22, trigger=27)
    return u3.distance * 100
def back():
    u6 = DistanceSensor(echo=5, trigger=6)
    return u6.distance * 100

    

try:
    while True:
        # Print distance and speed continuously
        print("Distance1:", back())
        sleep(1)
except KeyboardInterrupt:
    print("Exiting...")

GPIO.cleanup()
