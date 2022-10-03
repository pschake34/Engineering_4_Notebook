# Engineering_4_Notebook
 
 <br>

## Table of Contents

* [Launch Pad](#launch-pad)
    - [Part 1](#launch-pad-part-1)
    - [Part 2](#launch-pad-part-2)
    - [Part 3](#launch-pad-part-3)
    - [Part 4](#launch-pad-part-4)
* [Crash Avoidance](#crash-avoidance)
    - [Part 1](#crash-avoidance-part-1)
    - [Part 2](#crash-avoidance-part-2)
    - [Part 3](#crash-avoidance-part-3)

<br>

# Launch Pad

You are trapped on Mars. Food is running out. The launch pad you need to launch your rocket is broken. You have limited time to repair your launch pad and get off the planet.

## Launch Pad Part 1

### Assignment Description

The first goal of the assignment was to simply count down from 10 to launch, printing to the serial monitor. 

### Evidence 

<img src="videos/Launch%20Pad/part1.gif" height=300px>

### Wiring

N/A

### Code

[Link to code](/raspberry-pi/launch_pad_pt1.py).

### Reflection

This was the first assignment of the year, and I encoutered no difficulties making it work. A simple while loop counting from 10 to zero was all that was needed. One handy trick I learned to format strings was putting an f before the string: ```f"String to format: {x}"``` Rather than using ```"{}".format(x)``` to put a variable in a string.

<br>

## Launch Pad Part 2

### Assignment Description

The second step in the launch pad was to get LEDs blinking during the countdown. A red LED blinks every second during the countdown, and then a green LED turns on at launch. 

### Evidence

<img src="videos/Launch%20Pad/part2.gif" height=500px>

### Wiring

<img src="images/launch_pad_part2.png" height=300px>

### Code

[Link to code](/raspberry-pi/launch_pad_pt2.py)

### Reflection

Getting the LEDs to blink was a simple task. The only issue that I ran into was forgetting which LED leg went where. The answer is that the long leg goes to positive because bigger is always better.

<br>

## Launch Pad Part 3

### Assignment Description

The goal of the third assignment was to make a button start the countdown. If the button was pressed during the countdown it would be cancelled, and if it was pressed again, the countdown would restart.

### Evidence

<img src="videos/Launch%20Pad/part3.gif" height=500px>

### Wiring

<img src="images/launch_pad_part3.png" height=300px>

### Code

[Link to code](/raspberry-pi/launch_pad_pt3.py)

### Reflection

The hardest part of this assignment was debouncing the button, which I initially forgot to do. I also tried to take the lazy approach to debouncing by using ```time.sleep()```, but I wasn't exactly successful. I eventually had to use another variable to track whether the button had been on so that it wouldn't be triggered multiple times.

<br>

## Launch Pad Part 4

### Assignment Description

The final part of the launchpad assignment was to make a servo actuate at the end of the countdown. The servo had to start moving when there were three seconds left in the countdown, and reach 180 degrees when the countdown reached zero.

### Evidence

<img src="videos/Launch%20Pad/part4.gif" height=500px>

### Wiring

<img src="images/launch_pad_part4.png" height=300px>

### Code

[Link to code](/raspberry-pi/launch_pad_pt4.py)

### Reflection

The hardest part about getting the servo moving in time with the countdown was changing the timing scheme from ```time.sleep()``` to taking readings from ```time.monotonic()```. Although it was much more complicated, it made multitasking possible, so the servo could move while the LED was blinking without causing any troubles.

<br>

# Crash Avoidance

You are in a helicopter, and you have no idea if you're going to crash. You need to not.

## Crash Avoidance Part 1

### Assignment Description

The first part of the assignment was to wire up an accelerometer to read x, y, and z acceleration.

### Evidence

<img src="videos/Crash%20Avoidance/part1.gif" height=500px>

### Wiring

<img src="images/crash_avoidance_part1.png" height=300px>

### Code

[Link to code](/raspberry-pi/crash_avoidance_pt1.py)

### Reflection

I didn't run into any issues, but 

<br>

## Crash Avoidance Part 2

### Assignment Description



### Evidence

<img src="videos/Crash%20Avoidance/part2.gif" height=500px>

### Wiring

<img src="images/crash_avoidance_part2.png" height=300px>

### Code

[Link to code](/raspberry-pi/crash_avoidance_pt1.py)

### Reflection



<br>

## Crash Avoidance Part 3

### Assignment Description



### Evidence

<img src="videos/Crash%20Avoidance/part3.gif" height=300px>

### Wiring

<img src="images/crash_avoidance_part3.png" height=300px>

### Code

[Link to code](/raspberry-pi/crash_avoidance_pt1.py)

### Reflection



<br>