# dht11.py
import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

try:
    while True:
        #humidity, temperature
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (t, h))
        else:
            print('Read Error')
        time.sleep(0.1)

finally:
    print('bye')