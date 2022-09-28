# Paul Schakel
# Crash Avoidance pt 2

import board
import busio
import adafruit_mpu6050
import digitalio
import time

sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(scl_pin, sda_pin)

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:
    x = round(mpu.acceleration[0], 3)
    y = round(mpu.acceleration[1], 3)
    z = round(mpu.acceleration[2], 3)
    time.sleep(0.2)
    print(f"x: {x} y: {y} z: {z}")
    if z > -3 and z < -1:
        led.value = True
    else:
        led.value = False