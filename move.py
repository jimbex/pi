from RPi import GPIO
import time
from enc import pulse, speed, distance


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


out1 = 12
out2 = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(out1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(out1, GPIO.RISING, callback=pulse)

# Set up GPIO pins as outputs
GPIO.setup(IN_11, GPIO.OUT)
GPIO.setup(IN_12, GPIO.OUT)
GPIO.setup(IN_13, GPIO.OUT)
GPIO.setup(IN_14, GPIO.OUT)
GPIO.setup(IN_21, GPIO.OUT)
GPIO.setup(IN_22, GPIO.OUT)
GPIO.setup(IN_23, GPIO.OUT)
GPIO.setup(IN_24, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(en, GPIO.HIGH)


    
def stop():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.LOW)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.LOW)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.LOW)
    GPIO.output(IN_23, GPIO.LOW)
    GPIO.output(IN_24, GPIO.LOW)

def forward():
    GPIO.output(IN_11, GPIO.HIGH)
    GPIO.output(IN_12, GPIO.LOW)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.HIGH)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.HIGH)
    GPIO.output(IN_23, GPIO.LOW)
    GPIO.output(IN_24, GPIO.HIGH)


def backward():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.HIGH)
    GPIO.output(IN_13, GPIO.HIGH)
    GPIO.output(IN_14, GPIO.LOW)
    GPIO.output(IN_21, GPIO.HIGH)
    GPIO.output(IN_22, GPIO.LOW)
    GPIO.output(IN_23, GPIO.HIGH)
    GPIO.output(IN_24, GPIO.LOW)

def left():
    GPIO.output(IN_11, GPIO.HIGH)
    GPIO.output(IN_12, GPIO.LOW)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.HIGH)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.HIGH)
    GPIO.output(IN_23, GPIO.HIGH)
    GPIO.output(IN_24, GPIO.LOW)

def right():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.HIGH)
    GPIO.output(IN_13, GPIO.HIGH)
    GPIO.output(IN_14, GPIO.LOW)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.HIGH)
    GPIO.output(IN_23, GPIO.HIGH)
    GPIO.output(IN_24, GPIO.LOW)

def forward_left():
    GPIO.output(IN_11, GPIO.HIGH)
    GPIO.output(IN_12, GPIO.LOW)
    GPIO.output(IN_13, GPIO.HIGH)
    GPIO.output(IN_14, GPIO.LOW)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.LOW)
    GPIO.output(IN_23, GPIO.LOW)
    GPIO.output(IN_24, GPIO.HIGH)

def forward_right():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.HIGH)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.HIGH)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.LOW)
    GPIO.output(IN_23, GPIO.HIGH)
    GPIO.output(IN_24, GPIO.LOW)

def backward_left():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.HIGH)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.LOW)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.LOW)
    GPIO.output(IN_23, GPIO.LOW)
    GPIO.output(IN_24, GPIO.HIGH)

def backward_right():
    GPIO.output(IN_11, GPIO.LOW)
    GPIO.output(IN_12, GPIO.LOW)
    GPIO.output(IN_13, GPIO.LOW)
    GPIO.output(IN_14, GPIO.HIGH)
    GPIO.output(IN_21, GPIO.LOW)
    GPIO.output(IN_22, GPIO.HIGH)
    GPIO.output(IN_23, GPIO.LOW)
    GPIO.output(IN_24, GPIO.LOW)

# Define other movements and speed control functions similarly


try:
    while True:
        right()
        print(distance())
        print(speed())
        time.sleep(1)
        # Print distance and speed continuously
       
except KeyboardInterrupt:
    print("Exiting...")


GPIO.cleanup()