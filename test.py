from RPi import GPIO
import time


out1 = 12
out2 = 26
IN_11 = 23
IN_12 = 24
IN_13 = 16
IN_14 = 20
IN_21 = 4
IN_22 = 17
IN_23 = 13
IN_24 = 19
en = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN_11, GPIO.OUT)
GPIO.setup(IN_12, GPIO.OUT)
GPIO.setup(IN_13, GPIO.OUT)
GPIO.setup(IN_14, GPIO.OUT)
GPIO.setup(IN_21, GPIO.OUT)
GPIO.setup(IN_22, GPIO.OUT)
GPIO.setup(IN_23, GPIO.OUT)
GPIO.setup(IN_24, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

pwm = GPIO.PWM(en, 100)
pwm.start(90)


try:
    while True:
        
        GPIO.output(IN_11, GPIO.HIGH)
        GPIO.output(IN_12, GPIO.LOW)
        GPIO.output(IN_13, GPIO.LOW)
        GPIO.output(IN_14, GPIO.HIGH)
        GPIO.output(IN_21, GPIO.HIGH)
        GPIO.output(IN_22, GPIO.LOW)
        GPIO.output(IN_23, GPIO.HIGH)
        GPIO.output(IN_24, GPIO.LOW)
        time.sleep(1)
        # Print distance and speed continuously
       
except KeyboardInterrupt:
    print("Exiting...")
    


GPIO.cleanup()

    