from machine import Pin,I2C
import ADXL345
import time
import network
import machine
from umqtt.simple import MQTTClient
from secrets import secrets
import json

#ssid = secrets['ssid']
#password = secrets['password']

ssid = secrets['ssid_dom']
password = secrets['password_dom']

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

led = machine.Pin("LED", machine.Pin.OUT)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
mqtt_server = secrets['broker_dom']
client_id = 'PicoW'
user_t = ''
password_t = ''
topic_pub = '/adxl'

last_message = 0
message_interval = 5
counter = 0

def mqtt_connect():
    #global client
    client = MQTTClient(client_id, mqtt_server, user=user_t, password=password_t, keepalive=3000)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connected to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()



i2c = machine.I2C(0,
                  scl=machine.Pin(9),
                  sda=machine.Pin(8),
                  freq=100000)

adx = ADXL345.ADXL345(i2c)

client = mqtt_connect()    

while True:
        x=adx.xValue
        y=adx.yValue
        z=adx.zValue
    #print('The acceleration info of x, y, z are:%d,%d,%d'%(x,y,z))
        roll,pitch = adx.RP_calculate(x,y,z)
        
        try:
            
#            client.publish(topic_pub, msg=json.dumps({
#                                            "x": x,
#                                            "y": y,
#                                            "z" : z,
#}))
            client.publish(topic_pub, msg=json.dumps({
                                            "pitch": pitch,
                                            "roll": roll,
                                            
}))
            #blink_onboard_led(2, 0.1)
            print(x)
            time.sleep(0.1)
        except:
            print('Error')
            time.sleep(60)
            reconnect()
            #pass
            #client.disconnect()





