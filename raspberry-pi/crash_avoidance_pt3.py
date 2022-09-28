# Paul Schakel
# Crash Avoidance pt 3

import board
import busio
import adafruit_mpu6050
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import time

displayio.release_displays()

sda_pin = board.GP10
scl_pin = board.GP11
i2c = busio.I2C(scl_pin, sda_pin)

led = digitalio.DigitalInOut(board.GP16)
led.direction = digitalio.Direction.OUTPUT

mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP6)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

# create the display group
splash = displayio.Group()

# add title block to display group
title = "ANGULAR VELOCITY"
# the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

# you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
# Don't forget to round the angular velocity values to three decimal places

# send display group to screen
display.show(splash)

while True:
    x = round(mpu.acceleration[0], 3)
    y = round(mpu.acceleration[1], 3)
    z = round(mpu.acceleration[2], 3)
    time.sleep(0.2)

    # create the display group
    splash = displayio.Group()

    # add title block to display group
    content = f"ANGULAR VELOCITY\nx: {x}\ny: {y}\nz: {z}"
    # the order of this command is (font, text, text color, and location)
    text_area = label.Label(terminalio.FONT, text=content, color=0xFFFF00, x=5, y=5)
    splash.append(text_area)

    # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
    # Don't forget to round the angular velocity values to three decimal places

    # send display group to screen
    display.show(splash)

    print(f"x: {x} y: {y} z: {z}")
    if z > -3 and z < -1:
        led.value = True
    else:
        led.value = False