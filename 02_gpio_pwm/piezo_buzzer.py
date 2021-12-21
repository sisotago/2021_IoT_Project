# 도 음 출력하기
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# PWM 인스턴스 생성
# 주파수 설정 (4옥타브 도 음 : 262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10)   # duty cycle (0~100) -> 소리의 세기(크기)

time.sleep(2)
# 부저음이 나지 않음

pwm.stop()
GPIO.cleanup()
