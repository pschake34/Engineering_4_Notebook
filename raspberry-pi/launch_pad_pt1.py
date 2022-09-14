# Paul Schakel
# Launch Pad part 1

import board
import time

def countdown(x):
    while x > 0:
        print(f"{x} seconds left...")
        x -= 1
        time.sleep(1)
    print("Liftoff!")

print("Starting Countdown...")
countdown(10)