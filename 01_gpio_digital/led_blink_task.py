#import RPi.GPIO as GPIO
#import time

#LED_PIN = 4
#GPIO.setmode(GPIO.BCM)  # GPIO.BCM or GPIO.BOARD
#GPIO.setup(LED_PIN, GPIO.OUT)  # GPIO.OUT or GPIO.IN

#for i in range(10):
#    GPIO.output(LED_PIN, GPIO.HIGH) # 1
#    print("led on") 
#    time.sleep(1)
#    GPIO.output(LED_PIN, GPIO.LOW) # 0
#    print("led off")
#    time.sleep(1)

#GPIO.cleanup()  # GPIO 핀상태 초기화
import RPi.GPIO as GPIO
import time

LEDR = 4
LEDY = 25
LEDG = 24
GPIO.setmode(GPIO.BCM)      # GPIO.BCM or GPIO.BOARD
GPIO.setup(LEDR, GPIO.OUT)
GPIO.setup(LEDY, GPIO.OUT) 
GPIO.setup(LEDG, GPIO.OUT)    # GPIO.OUT or GPIO.IN


GPIO.output(LEDR, GPIO.HIGH) #1
print("led RED on")
time.sleep(2)
GPIO.output(LEDR, GPIO.LOW)  #0
print("led RED off")
GPIO.output(LEDY, GPIO.HIGH) #1
print("led YELLOW on")
time.sleep(2)
GPIO.output(LEDY, GPIO.LOW)  #0
print("led YELLOW off")
GPIO.output(LEDG, GPIO.HIGH) #1
print("led GREEN on")
time.sleep(2)
GPIO.output(LEDG, GPIO.LOW)  #0
print("led GREEN off")

GPIO.cleanup()   