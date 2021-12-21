import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 18 #9 -> 18 GPIO 핀 번호 바꿈
ECHO_PIN = 22 #10 -> 22 GPIO 핀 번호 바꿈
BUZZER_PIN = 12
SEGMENT_PINS = [17, 27, 4, 5, 6, 23, 24] #2 -> 17, 3 -> 27, 7 -> 23 , 8 -> 24 GPIO 핀 번호 바꿈
# 7segment의 숫자를 나타내기 위함
zero = [1,1,1,1,1,1,0]
one = [0,1,1,0,0,0,0]
two = [1,1,0,1,1,0,1]
three = [1,1,1,1,0,0,1]
four = [0,1,1,0,0,1,1]
five = [1,0,1,1,0,1,1]
six = [1,0,1,1,1,1,1]
seven = [1,1,1,0,0,0,0]
eight = [1,1,1,1,1,1,1]
nine = [1,1,1,1,0,1,1]


GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
pwm = GPIO.PWM(BUZZER_PIN, 1)
pwm.start(5)
#          도   레   미   파   솔   라   시 높은도 높은레 높은미, 0~100cm까지 10cm 간격으로 다른 음을 나타내기 위함
melody = [262, 294, 330, 349, 392, 440, 494, 523, 587, 659]
for a in SEGMENT_PINS:
    GPIO.setup(a, GPIO.OUT)

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

        if 0 <= distance < 100 : # 거리가 100cm 미만일 때
            if 9 <= distance/10 < 10 :                          # 만약 거리/10이 9 이상이고 10 미만이면 (실제 거리는 90cm~99.몇cm일 때)
                    for i in range(len(SEGMENT_PINS)):          # SEGMENT_PINS의 리스트에 들어있는 숫자만큼 반복 (0~6)
                        GPIO.output(SEGMENT_PINS[i], nine[i])   # 숫자 9를 나타내기 위한 7segment
                        pwm.ChangeFrequency(melody[9])          # melody에서 10번째 값, 즉 높은 미 음을 발생시키기 위한 피에조 부저
            
            # 나머지 거리(0~89.몇cm)도 같은 방법 사용
            elif 8 <= distance/10 < 9 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], eight[i])
                        pwm.ChangeFrequency(melody[8])

            elif 7 <= distance/10 < 8 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], seven[i])
                        pwm.ChangeFrequency(melody[7])

            elif 6 <= distance/10 < 7 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], six[i])
                        pwm.ChangeFrequency(melody[6])

            elif 5 <= distance/10 < 6 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], five[i])
                        pwm.ChangeFrequency(melody[5])

            elif 4 <= distance/10 < 5 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], four[i])
                        pwm.ChangeFrequency(melody[4])

            elif 3 <= distance/10 < 4 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], three[i])
                        pwm.ChangeFrequency(melody[3])

            elif 2 <= distance/10 < 3 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], two[i])
                        pwm.ChangeFrequency(melody[2])

            elif 1 <= distance/10 < 2 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], one[i])
                        pwm.ChangeFrequency(melody[1])

            elif 0 <= distance/10 < 1 :
                    for i in range(len(SEGMENT_PINS)):
                        GPIO.output(SEGMENT_PINS[i], zero[i])
                        pwm.ChangeFrequency(melody[0])
         
                    


finally:
    GPIO.cleanup() 
    print('bye')