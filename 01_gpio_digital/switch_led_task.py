import RPi.GPIO as GPIO

LED_R = 7
LED_Y = 6
LED_G = 5
SWITCH_R = 12
SWITCH_Y = 11
SWITCH_G = 10

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_Y, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(SWITCH_R, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #내부풀다운저항
GPIO.setup(SWITCH_Y, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_G, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        valR = GPIO.input(SWITCH_R) #누르지 않은 경우 0, 눌렀을 때는 1
        print(valR)
        GPIO.output(LED_R, valR) #GPIO.HIGH (1), GPIO.LOW (0)

        valY = GPIO.input(SWITCH_Y) #누르지 않은 경우 0, 눌렀을 때는 1
        print(valY)
        GPIO.output(LED_Y, valY) #GPIO.HIGH (1), GPIO.LOW (0)

        valG = GPIO.input(SWITCH_G) #누르지 않은 경우 0, 눌렀을 때는 1
        print(valG)
        GPIO.output(LED_G, valG) #GPIO.HIGH (1), GPIO.LOW (0)

finally:
    GPIO.cleanup()
    print('cleanup and exit')