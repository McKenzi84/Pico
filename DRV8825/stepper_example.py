from machine import Pin
from stepper import StepperMotor
from time import sleep


step_pin = Pin(17, Pin.OUT)
dir_pin = Pin(16, Pin.OUT)
M0 = Pin(20, Pin.OUT)
M1 = Pin(19, Pin.OUT)
M2 = Pin(18, Pin.OUT)
mode_pins = (M0, M1, M2)

# Stepper motor setup
step_type = 'Half'
# fullstep_delay = 0.001

# create object
motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type,)


motor.run(2000, True)     # run motor 6400 steps clowckwise
sleep(0.5)
motor.run(4000, False)    # run motor 6400 steps counterclockwise