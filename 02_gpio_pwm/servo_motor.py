import RPi.GPIO as GPIO

SERVO_MOTOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_MOTOR_PIN, GPIO.OUT)

# 서보모터 제어에 필요한 주파수 : 50Hz (20ms)
pwm = GPIO.PWM(SERVO_MOTOR_PIN, 50)
pwm.start(7.5) # 7.5 (0도)  1 period(20ms)
# Duty Cycle 계산 : 1~2ms from datasheet, Max : +-0.5ms
# 1) -90도 : 1ms -> 1Period 당 1ms + (-0.5ms) -> 0.5ms/20ms -> 2.5%
# 2) 0도 : 1.5ms -> 1Period 당 1.5ms -> 1.5ms/20ms -> 7.5%
# 3) +90도 : 1ms -> 1Period 당 2ms + (0.5ms) -> 2.5ms/20ms -> 12.5%

# 1: 0도, 2: -90도, 3: 90도, 9:exit
try:
    while True:
        val = input('1: 0도, 2: -90도, 3: 90도, 9:exit >')
        if val == '1':
            pwm.ChangeDutyCycle(7.5)
        elif val == '2':
            #pwm.ChangeDutyCycle(5)   # -45도
            pwm.ChangeDutyCycle(2.5)  # -90도
        elif val == '3':
            #pwm.ChangeDutyCycle(10)   #45도
            pwm.ChangeDutyCycle(12.5)  #90도
        elif val == '9':
            break
finally:
    pwm.stop()
    GPIO.cleanup()