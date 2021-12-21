import RPi.GPIO as GPIO

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try: #try finally 하면 try에서 오류나도 finally는 무조건 실행
    while True:
        val = input("0:off, 1:on, 9:exit >")
        if val == '0':
            GPIO.output(LED_PIN, GPIO.LOW)
            print('led off')
        elif val == '1':
            GPIO.output(LED_PIN, GPIO.HIGH)
            print('led on')
        elif val == '9':
            break

finally:
    GPIO.cleanup()
    print('clean up and exit')