import RFID
import network
import time
import machine
from umqtt.simple import MQTTClient
from secrets import secrets

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
 

mqtt_server = '192.168.1.196'
client_id = 'PicoW'
user_t = 'mqtt'
password_t = 'mqtt'
topic_pub = '/test'

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

client = mqtt_connect()    
while True:
        
        
        try:
            message = RFID.read_card()
            client.publish(topic_pub, msg=str(message))
            time.sleep(5)
        except:
            print('Error')
            time.sleep(60)
            reconnect()
            #pass
            #client.disconnect()
