# Paul Schakel
# Launch Pad part 3

import board
import time
import digitalio

led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_prev = button.value

def countdown(x):
    print("Starting Countdown...")
    while x > 0:
        print(f"{x} seconds left...")
        x -= 1
        led_red.value = True
        time.sleep(.5)
        led_red.value = False
        time.sleep(.5)
        if button.value:
            button_prev = button.value
        if not button.value and button_prev:
            print("Aborting...")
            led_red.value = False
            led_green.value = False
            button_prev = button.value
            return
    led_green.value = True
    print("Liftoff!")

while True:
    if button.value:
        button_prev = button.value
    if not button.value and button_prev:
        led_green.value = False
        button_prev = button.value
        countdown(10)