# pir_led.py
import RPi.GPIO as GPIO
import time

PIR_PIN = 9
LED_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

time.sleep(5)
print('PIR Ready...')

try:
    while True:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:    # 1, True, HIGH
            print('움직임 감지')
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print('움직임 없음')
            GPIO.output(LED_PIN, GPIO.LOW)
            
        time.sleep(0.1)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
