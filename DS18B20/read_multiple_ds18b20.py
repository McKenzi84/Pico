import machine
import onewire
import ds18b20
import time
import binascii

gp_pin = machine.Pin(16)

ds18b20_sensor = ds18b20.DS18X20(onewire.OneWire(gp_pin))

sensors = ds18b20_sensor.scan()
sensors_count = len(sensors)
print(f'Found{sensors_count} devices')


sensors_count = len(sensors)
while True:
    ds18b20_sensor.convert_temp()
    time.sleep_ms(750)
    temp_sum = 0
    for device in sensors:
        s = binascii.hexlify(device)
        readable_string = s.decode('ascii')
        temp = ds18b20_sensor.read_temp(device)
        print(f'{readable_string}: Temp: {temp}')
#         print(ds18b20_sensor.read_temp(device))
        temp_sum += temp
        
    avg_temp = temp_sum / sensors_count
    print(f'Avg : {round(avg_temp,1)}')
    time.sleep(60)