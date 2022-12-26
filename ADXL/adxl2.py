from machine import Pin,I2C
import ADXL345
import time

i2c = machine.I2C(0,
                  scl=machine.Pin(9),
                  sda=machine.Pin(8),
                  freq=100000)
adx = ADXL345.ADXL345(i2c)

while True:
    x=adx.xValue
    y=adx.yValue
    z=adx.zValue
    #print('The acceleration info of x, y, z are:%d,%d,%d'%(x,y,z))
    #roll,pitch = adx.RP_calculate(x,y,z)
    #print('roll=',roll)
    #print('pitch=',pitch)
    #time.sleep_ms(1000)
        # Print results
    print("X:", "{:.2f}".format(x), \
          "| Y:", "{:.2f}".format(y), \
          "| Z:", "{:.2f}".format(z))
    time.sleep_ms(50)