from machine import Pin
from time import sleep

class StepperMotor:
    def __init__(self,  step_pin, dir_pin, mode_pins, step_type,):
        """docstring for ."""
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        resolution = {'Full':(0, 0, 0),
                    'Half':(1, 0, 0),
                    '1/4':(0, 1, 0),
                    '1/8':(1, 1, 0),
                    '1/16':(0, 0, 1),
                    '1/32':(1, 0, 1)}
        microsteps =  {'Full':1,
                    'Half':2,
                    '1/4':4,
                    '1/8':8,
                    '1/16':16,
                    '1/32':32}
        
        #self.delay = .005/microsteps[step_type]
        self.delay = .001
        mode_pins[0].value(resolution[step_type][0])
        mode_pins[1].value(resolution[step_type][1])
        mode_pins[2].value(resolution[step_type][2])

    def run(self, steps, clockwise):
        self.dir_pin.value(clockwise)
        for i in range(steps):
            self.step_pin.value(1)
            sleep(self.delay)
            self.step_pin.value(0)
            sleep(self.delay)


###################
# step_pin = Pin(17, Pin.OUT)
# dir_pin = Pin(16, Pin.OUT)
# M0 = Pin(20, Pin.OUT)
# M1 = Pin(19, Pin.OUT)
# M2 = Pin(18, Pin.OUT)
# mode_pins = (M0, M1, M2)
# 
# # Stepper motor setup
# step_type = 'Half'
# # fullstep_delay = 0.001
# 
# # create object
# motor = StepperMotor(step_pin, dir_pin, mode_pins, step_type,)
# 
# 
# motor.run(2000, True)     # run motor 6400 steps clowckwise
# sleep(0.5)
# motor.run(4000, False)    # run motor 6400 steps counterclockwise
