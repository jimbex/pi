import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

m1= 13
m2= 19
en= 26

GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(en, GPIO.HIGH)
while True:

    
    GPIO.output(m2, GPIO.HIGH)
    GPIO.output(m1, GPIO.LOW)

GPIO.cleanup()
