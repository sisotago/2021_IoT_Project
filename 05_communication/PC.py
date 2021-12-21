# import modules
#+--------------------------------------+

import RPi.GPIO as GPIO
from lcd import drivers
import cv2

import time
import multiprocessing as mp

#+--------------------------------------+


# Prepare everything
#+--------------------------------------+



LED_PIN = 4
BUZZER_PIN = 17
PIR_PIN = 9
SWITCH_PIN = 25

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # 내부풀다운저항 사용하기

display = drivers.Lcd()


face_cascade = cv2.CascadeClassifier('./xml/face.xml')

pwm = GPIO.PWM(BUZZER_PIN, 262)


people = 0
total = 0


manager = mp.Manager() # 멀티프로세싱을 대비한 프로세스 간 통신 가능한 변수들 정의하기
people_list = manager.list()
total_list = manager.list()
people_list.append(0)
total_list.append(0)


#+--------------------------------------+

# camera input
#+--------------------------------------+


cap = cv2.VideoCapture(-1)


if not cap.isOpened(): #카메라 오픈되어있는지 확인하기
    print('Camera connection failed')
    exit()


# define functions
#+--------------------------------------+



#+--------------------------------------+


# MultiProcessing
#+--------------------------------------+

def mp_Camera_working(): #카메라 
    print("Camera Worked")
    while 1:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 흑백으로 바꿈으로써 인식이 되도록
        if not ret: # 감지된 프레임이 없으면 꺼지기
            print("false")
            return 0
            break
        faces = face_cascade.detectMultiScale(gray,1.3,5) 
        for (x,y,w,h) in faces: #TODO : x,y,w,h
            cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 0), 2)     # 사진, 시작 좌표, 끝나는 좌표, 색(255,0,0)=blue, 선의 두께
        cv2.imshow('gray', gray)
        people_list[0] = len(faces) # len(faces)를 사용함으로써 현재 카메라 화면에 나와 있는 사람 수를 저장
        print(people_list[0])
        if cv2.waitKey(10) == 13:
            break
            
        


def mp_PIR_working(): #적외선 센서, 사람이 감지되면 LED가 켜지게 설정
    while 1:
        val = GPIO.input(PIR_PIN)
        if val == GPIO.HIGH:
            GPIO.output(LED_PIN,GPIO.HIGH)
        else:
            GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(0.1)

def mp_PeopleLimit_Buzzer():  # people이라는 전역 변수로 사람 수가 3명 이상이라고 측정되면 부저를 울린다.
    while True:
        if people_list[0] >= 3:
            pwm.start(50)
        else :
            pwm.stop()

    
def mp_addpeople_button():   # 버튼이 눌리면 총 사람 수 추가하기
    while True:
        val = GPIO.input(SWITCH_PIN) #누르지 않은 경우 0, 눌렀을 때는 1
        if val == 1:
            total_list[0] += 1
            time.sleep(1)
        
def mp_displaytotal_lcd(): #LCD에 mp_addpeople_button에서 가져온 사람 수 출력하기
    while True:
        display.lcd_display_string("%d" % (total_list[0]), 1)




#+--------------------------------------+

   
        
        
        




# main
#+--------------------------------------+

if __name__ == "__main__":
    try :
        # 멀티프로세싱 설정
        camera_proc = mp.Process(target=mp_Camera_working) 
        PIR_proc = mp.Process(target=mp_PIR_working)
        Buzzer_proc = mp.Process(target = mp_PeopleLimit_Buzzer)
        Button_proc = mp.Process(target = mp_addpeople_button)
        Lcd_proc = mp.Process(target= mp_displaytotal_lcd)

        # 프로세스들 시작
        camera_proc.start()
        PIR_proc.start()
        Buzzer_proc.start()
        Button_proc.start()       
        Lcd_proc.start()
        
        # 프로세스 종료까지 기다리기
        camera_proc.join() 
        PIR_proc.join()
        Buzzer_proc.join()
        Button_proc.join()
        Lcd_proc.join()
        
    finally :
        print("Cleanup Sucessful")
        GPIO.cleanup()
        display.lcd_clear()
        cap.release()
        cv2.destroyAllWindows()
        