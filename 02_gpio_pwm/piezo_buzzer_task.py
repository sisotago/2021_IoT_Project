import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(10)

melody = [262, 294, 330, 349, 392, 440, 494, 523]
school_bell = [4,4,5,5,4,4,2,4,4,2,2,1,4,4,5,5,4,4,2,4,2,1,2,0]
l=0

try:
    for i in school_bell:
        l+=1
        pwm.ChangeFrequency(melody[i])
        if(l==7 or l==19):
            time.sleep(0.5)
        if(l==12 or l==24):
            time.sleep(1.5)
        time.sleep(0.5)

finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')