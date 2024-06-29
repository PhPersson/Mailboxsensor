from mqtt import MQTTClient
import network
from machine import unique_id
from ubinascii import hexlify
from ujson import dumps
import config as CONST


def connect_to_WLAN():

        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)

        if not wlan.isconnected():
            print("Connecting to network...")
            wlan.connect('LANsolo', 'Gefanidetta')
            print("Connected to network")
            while not wlan.isconnected():
                pass


def connect_to_mqtt():
        
        client = MQTTClient(hexlify(unique_id()), CONST.AIO_BROKER, 1883,CONST.AIO_USERNAME, CONST.AIO_ACCESS_KEY)
        if (client):
             print ("Connected to mqtt")
        return client

def publish_message(client, message):
    client.publish(CONST.AIO_TOPIC,dumps(message))
    print("published messaged")


def check_if_connected_wlan():
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        return connect_to_WLAN()
    return wlan