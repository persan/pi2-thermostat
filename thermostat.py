#!/usr/bin/python3
try:
    import Adafruit_DHT
    import silverpm
except:
    from stubs import silverpm
    from stubs import Adafruit_DHT

import time
import paho.mqtt.client as mqtt

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).

# Un-comment the line below to convert the temperature to Fahrenheit.
# temperature = temperature * 9/5.0 + 32
class thermostat:
    def __init__(self):

        self.mqttc = mqtt.Client()
        self.mqttc.connect("mqtt")
        self.mqttc.loop_start()
        self.manager=silverpm.power_manager()
        self.temperature=0.0
        
        for i in range(1,5):
            self.manager.disable_outlet(i)
            
        for i in range(1,5):
            self.manager.enable_outlet(i)
            time.sleep(1)
            self.manager.disable_outlet(i)
    def run(self):
        while True:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
            if self.humidity is not None and self.temperature is not None:
                # print('Temp={0:0.1f}C  Humidity={1:0.1f}%'.format(temperature, humidity))
                self.mqttc.publish("tele/uterum/temp",     "%f" % (self.temperature))
                self.mqttc.publish("tele/uterum/humidity", "%f" % (self.humidity))
                if self.temperature > 8.0:
                    self.manager.disable_outlet(1)
                    self.manager.disable_outlet(2)
                    self.mqttc.publish("tele/uterum/switch/1", 'False')
                    self.mqttc.publish("tele/uterum/switch/2", 'False')
                elif self.temperature < 7.0:
                    self.manager.enable_outlet(1)
                    self.mqttc.publish("tele/uterum/switch/1", 'True')
                elif self.temperature < 5.0:
                    self.mqttc.publish("tele/uterum/switch/2", 'True')
                    self.manager.enable_outlet(2)
            time.sleep(5)

def main():
    t=thermostat()
    t.run()
if __name__ == "__main__":
    main()
