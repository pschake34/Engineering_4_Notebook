# Paul Schakel
# Launch Pad

import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

led_red = digitalio.DigitalInOut(board.GP13)
led_green = digitalio.DigitalInOut(board.GP18)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP16)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_prev = button.value
pwm_servo = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)
servo1.angle = 0

blink_duration = 0.5

def countdown(x):
    print("Starting Countdown...")
    while x > 0:
        now = time.monotonic()
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
        if x <= 3:
    led_green.value = True
    print("Liftoff!")

def servo_thread():
    for a in range(180):
        servo1.angle = a
        time.sleep(0.1)

while True:
    if button.value:
        button_prev = button.value
    if not button.value and button_prev:
        led_green.value = False
        button_prev = button.value
        countdown(10)
