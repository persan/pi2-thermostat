#!/usr/bin/python3
import Adafruit_DHT
import time
import silverpm
# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32

manager=silverpm.power_manager()
for i in range(1,5):
    manager.disable_outlet(i)
    
for i in range(1,5):
    manager.enable_outlet(i)
    time.sleep(1)
    manager.disable_outlet(i)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    if humidity is not None and temperature is not None:
        # print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
        if temperature > 8.0:
            manager.disable_outlet(1)
            manager.disable_outlet(2)
        elif temperature < 7.0:
            manager.enable_outlet(1)
        elif temperature < 5.0:
            manager.enable_outlet(1)
    time.sleep(5)
