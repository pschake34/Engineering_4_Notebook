# Paul Schakel
# Launch Pad

import board
import time
import digitalio

led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT

def countdown(x):
    print("Starting Countdown...")
    while x > 0:
        print(f"{x} seconds left...")
        x -= 1
        led_red.value = True
        time.sleep(.5)
        led_red.value = False
        time.sleep(.5)
    print("Liftoff!")
    led_green.value = True
    time.sleep(10)

countdown(10)