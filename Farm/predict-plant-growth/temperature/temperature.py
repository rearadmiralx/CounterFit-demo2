# importing the counterfit connection
from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1', 5000)

# import tme, dht or digital temperature and humidity sensor
# paho client for mqtt(server) and json string
import time
from counterfit_shims_seeed_python_dht import DHT
import paho.mqtt.client as mqtt
import json

#this is a virtual sensor we used DHT11 and connected to pin5
sensor = DHT("11", 5)

id = '9f4189cc-05b2-11ec-9a03-0242ac130003'

client_telemetry_topic = id + '/telemetry'
client_name = id + 'temperature_sensor_client'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

print("MQTT connected!")

while True:
    _, temp = sensor.read()
    telemetry = json.dumps({'temperature' : temp})

    print("Sending telemetry ", telemetry)

    mqtt_client.publish(client_telemetry_topic, telemetry)

    time.sleep(10)
    

# from counterfit_connection import CounterFitConnection
# CounterFitConnection.init('127.0.0.1', 5000)

# import time
# from counterfit_shims_seeed_python_dht import DHT
# # You need to import this counterfit_shims_seeed_python_dht


# sensor = DHT("11", 5)

# while True:
#     _, temp = sensor.read()
#     print(f'Temperature {temp}°C')

#     time.sleep(10)
