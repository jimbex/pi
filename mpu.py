import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mp = adafruit_mpu6050.MPU6050(i2c)

def acc():
	return mp.acceleration

def gyr():
	return mp.gyro
	
def temp():
	return mp.temperature
	
while True:
	print(gyr())
	time.sleep(1)
