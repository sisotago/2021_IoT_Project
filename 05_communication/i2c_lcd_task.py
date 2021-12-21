from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4
display = drivers.Lcd()

try:
    while True:
        now = datetime.datetime.now()
        print(now.strftime("%x %X"))
        display.lcd_display_string(now.strftime("%x%X"),1)
        h, t = Adafruit_DHT.read_retry(sensor, DHT_PIN)
        if h is not None and t is not None:
            print('Temperature=%.1f*, Humidity=%.1f%%' % (t, h))
            display.lcd_display_string(f"{t:.1f}*C, {h:.1f}%",2)
        else:
            print('Read Error')
        
        time.sleep(0.5)
        
finally:
    print("Cleaning up!")
    display.lcd_clear()
