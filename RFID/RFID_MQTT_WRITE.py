#https://www.hivemq.com/blog/iot-reading-sensor-data-raspberry-pi-pico-w-micropython-mqtt-node-red/

import network
import time
from machine import Pin
from umqtt.simple import MQTTClient
from secrets import secrets
import RFID


ssid = secrets['ssid_dom']
password = secrets['password_dom']

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

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


# mqtt_server = '192.168.1.196'
# client_id = 'PicoW'
# user_t = 'mqtt'
# password_t = 'mqtt'
# topic_pub = '/test'

mqtt_server = '192.168.1.196'
client_id = 'PicoW'
user_t = 'mqtt'
password_t = 'mqtt'
topic_sub = '/write_to_card'




def sub_cb(topic, msg):
    print("-------------------------------------")
    print("Nowa wiadomość:  {}".format(topic.decode('utf-8')))
    msg = msg.decode('utf-8')
    print('Przygotuj kartę do zapisu......')
    RFID.write_to_card(msg)
    print(f'Dane zapisane do karty: {msg}')
    

def mqtt_connect():
    #client = MQTTClient(client_id, mqtt_server, keepalive=60)
    client = MQTTClient(client_id, mqtt_server, user=user_t, password=password_t, keepalive=3000)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
    
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    client.subscribe(topic_sub)
    time.sleep(1)