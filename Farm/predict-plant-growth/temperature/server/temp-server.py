import json
import time

import paho.mqtt.client as mqtt

from os import path
import csv
from datetime import datetime

# generate your unique id for mqtt
# then create your telemetry(eg. temperature) with its command and server
id = '9f4189cc-05b2-11ec-9a03-0242ac130003'

client_telemetry_topic = id + '/telemetry'
server_command_topic = id + '/commands'
client_name = id + 'temperature_sensor_server'

mqtt_client = mqtt.Client(client_name) # client name = f4189cc-05b2-11ec-9a03-0242ac130003temperature_sensor_server
mqtt_client.connect('test.mosquitto.org') #connecting to mqtt server with is a public mqtt

mqtt_client.loop_start() # literal that calls start client repeatedly

temperature_file_name = 'temperature.csv' # creating a .csv file where to put output
fieldnames = ['date', 'temperature'] # the data you insert inside the csv file

#this will check if the file already exist if not it will create a file named temperature.csv and write the fieldnames
if not path.exists(temperature_file_name): 
    with open(temperature_file_name, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

def handle_telemetry(client, userdata, message):
    payload = json.loads(message.payload.decode())
    print("Message received:", payload)

    #if file is existed it will just Open for reading and writing.  The file is created if it does not
    #  exist.  The stream is positioned at the end of the file.  Subse-
    #  quent writes to the file will always end up at the then current
    #  end of file, irrespective of any intervening fseek(3) or similar.
    with open(temperature_file_name, mode='a+') as temperature_file:        
        temperature_writer = csv.DictWriter(temperature_file, fieldnames=fieldnames)
        temperature_writer.writerow({'date' : datetime.now().astimezone().replace(microsecond=0).isoformat(), 'temperature' : payload['temperature']})

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(2)