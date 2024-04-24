from gpiozero import Servo
from time import sleep

servo = Servo(7)  # Replace 17 with the GPIO pin number you've connected the servo to

try:
    while True:
        

        # Move the servo to the maximum angle (180 degrees)
        servo.max()
        print("Set to maximum position")
        sleep(1)

except KeyboardInterrupt:
    pass

servo.detach()  # Rel