# ultra_sonic.py
import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 4
ECHO_PIN = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

try:
    while True:
        # 10us 동안 HIGH 출력
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(0.00001)    #10us (1us -> 0.000001s)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)

        # ECHO_PIN -> HIGH로 되는 시간 (start time)
        while GPIO.input(ECHO_PIN) == 0:
            pass
        start = time.time() # 시작 시간

        while GPIO.input(ECHO_PIN) == 1:
            pass
        stop = time.time()  # 종료 시간

        duration_time = stop - start
        distance = 17160 * duration_time

        print('Distance : %.1fcm' % distance)
        time.sleep(0.1)

finally:
    GPIO.cleanup()
    print('cleanup and exit')