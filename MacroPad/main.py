import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import board
import digitalio
import random


btn1_pin = board.GP2
btn2_pin = board.GP8
btn3_pin = board.GP1
btn4_pin = board.GP4
btn5_pin = board.GP10
btn6_pin = board.GP6

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)
            
def write(text):
    layout.write(text)

def run_let():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.T )
    
    
def run_mizo():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.M )
    
def run_dashboard():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.D )
    

def task_manager():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.LEFT_SHIFT, Keycode.ESCAPE)
    
def generate_password():

    chars = 'abcdefghijklmnoprstuvwxyz1234567890ABCDEFGHIJKLMNOPRSTUVWXYZ!@#$%^&*'
    length = 2000
    password = ''
    for c in range(length):
        password += random.choice(chars)
    write(password)
def change_desktop_1():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.RIGHT_ARROW )	
def change_desktop_2():
    keyboard.send(Keycode.LEFT_CONTROL, Keycode.WINDOWS, Keycode.LEFT_ARROW )	

while True:
    if btn1.value:                    
        generate_password()
    if btn2.value:                    
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.V )       
    if btn3.value:                    
        keyboard.send(Keycode.LEFT_CONTROL, Keycode.S )
    if btn4.value:                    
        keyboard.send(Keycode.WINDOWS, Keycode.NINE )
    if btn5.value:                    
        change_desktop_1()
    if btn6.value:                    
        change_desktop_2()
        

    time.sleep(0.1)

