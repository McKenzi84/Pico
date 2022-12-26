from time import sleep
from machine import Pin

dir = Pin(16, Pin.OUT)   # Direction GPIO Pin
step = Pin(17, Pin.OUT)  # Step GPIO Pin
M0 = Pin(20, Pin.OUT)
M1 = Pin(19, Pin.OUT)
M2 = Pin(18, Pin.OUT)
step_count = 50
delay = 0.002

def full():
    M0.value(0)
    M1.value(0)
    M2.value(0)

def half():
    M0.value(1)
    M1.value(0)
    M2.value(0)

def four():
    M0.value(0)
    M1.value(1)
    M2.value(0)
def one_16():
    M0.value(0)
    M1.value(0)
    M2.value(1)
def one_32():
    M0.value(1)
    M1.value(1)
    M2.value(1)

def cw():  # stepper turns clockwise
    dir.value(1)    
    step.value(1)
    sleep(delay)
    step.value(0)
    sleep(delay)


def ccw(): # stepper turns counterclockwise
    dir.value(0)    
    step.value(1)
    sleep(delay)
    step.value(0)
    sleep(delay)




def run():
    cw()
    one_16()
    
def run1():
    ccw()
    one_16()
    
while True:
    
    run()
#     sleep(5)
#     run1()
      
     







