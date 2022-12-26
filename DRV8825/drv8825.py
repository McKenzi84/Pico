# Stepper control w/o stepping

from time import sleep
from machine import Pin

DIR = Pin(16, Pin.OUT)   # Direction GPIO Pin
STEP = Pin(17, Pin.OUT)  # Step GPIO Pin
led_red = Pin(15, Pin.OUT)
led_green = Pin(14, Pin.OUT)

step_count = 1000
delay = .005

while True:
    sleep(1)

    for x in range(step_count):
        DIR.value(1)
        led_red.value(1)
        led_green.value(0)
        STEP.value(1)
        sleep(delay)
        STEP.value(0)
        sleep(delay)
        led_red.value(0)
    
    sleep(1)

    for x in range(step_count):
        led_red.value(0)
        led_green.value(1)
        DIR.value(0)
        STEP.value(1)
        sleep(delay)
        STEP.value(0)
        sleep(delay)
        led_green.value(0)