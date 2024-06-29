from machine import Pin
import machine, onewire, ds18x20, time
from functions import check_if_connected_wlan, connect_to_mqtt, publish_message

ds_pin = Pin(0) 
button_pin = Pin(5)  


ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
roms = ds_sensor.scan()
print('Found DS devices: ', roms)

# Initialize button
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)


while True:

    ds_sensor.convert_temp()
    time.sleep_ms(750)
    for rom in roms:
        print(rom)

    client.disconnect()
    deep_sleep(1800000)