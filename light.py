from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1',5000)

# importing paho for mqtt to connect to server and json to dump datas
import paho.mqtt.client as mqtt
import json

import time 
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

# this id is generated so to make sure the uniqueness 
id = '9f4189cc-05b2-11ec-9a03-0242ac130003'

client_name = id + 'nightlight_client'
client_telemetry_topic = id + '/telemetry'
server_command_topic = id +'/commands'

# trying to connect to mostquitto.org with is used for mqtt
mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')


def handle_command(cliend, userdate, message):
    payload = json.loads(message.payload.decode())
    print("Message received: ", payload)

    if payload['led_on']:
        led.on()
    else:
        led.off()


mqtt_client.subscribe(server_command_topic)
mqtt_client.on_message = handle_command

mqtt_client.loop_start()

print("MQTT connected!")


light_sensor = GroveLightSensor(0) # this is the light sensor 0
led = GroveLed(2) #this is the led pin which is #2

#change the while loop and make it json type this won't 
# work if you don't do codes for server side
while True:
    light = light_sensor.light
    telemetry = json.dumps({'light': light})
    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(5)







##########################################################
# For RASPI
# import time 
# from grove.grove_light_sensor_v1_2 import GroveLightSensor

# light_sensor = GroveLightSensor(0)

# while True:
#     light = light_sensor.light
#     print('Light Level: ', light)

#     if(light <500):
#         led.on()
#     else:
#         led.off()

#     time.sleep(1)
