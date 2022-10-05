# Paul Schakel
# Crash Avoidance pt 1

import board
import busio
import adafruit_mpu6050
import time

# Initialize Accelerometer
sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    time.sleep(0.2)
    print(f"x: {round(mpu.acceleration[0], 3)} y: {round(mpu.acceleration[1], 3)} z: {round(mpu.acceleration[2], 3)}")