from counterfit_connection import CounterFitConnection
CounterFitConnection.init('127.0.0.1',5000)

import time 
from counterfit_shims_grove.grove_light_sensor_v1_2 import GroveLightSensor
from counterfit_shims_grove.grove_led import GroveLed

light_sensor = GroveLightSensor(0) # this is the light sensor 0
led = GroveLed(2) #this is the led pin which is #2

while True:
    light = light_sensor.light
    print('Light Level: ', light)

    if(light <500):
        led.on()
    else:
        led.off()

    time.sleep(1)



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
