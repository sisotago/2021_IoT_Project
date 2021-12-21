from flask import Flask
import RPi.GPIO as GPIO

LEDr = 4
LEDb = 5

# Flask() 객체 생성
# __name__은 파일명
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDr, GPIO.OUT)
GPIO.setup(LEDb, GPIO.OUT)

# 라우팅(클라이언트로부터 요청받은 URL과 특정한 뷰를 매칭시키는 것)을 위한 뷰 함수, 라우팅에는 동적 라우팅과 정적 라우팅이 있음.
@app.route("/") # @app.route(호출할 URL) /는 정적 라우팅
def led():    # <p>태그 : p = paragraph = 문단 (화면에 출력), <a>태그 : anker : 다른 URL로 이동 가능, 여는 태그랑 닫는 태그(</태그>) 한 쌍
    return '''
    <p>Hello, Flask!</p> 
    <a href="/led/red/on">LED RED ON</a>
    <a href="/led/red/off">LED RED OFF</a>
    <a href="/led/blue/on">LED BLUE ON</a>
    <a href="/led/blue/off">LED BLUE OFF</a>
    '''

@app.route("/led/<color>/<op>") # 동적 라우팅, led까지는 같고 op자리에는 다른 값이 들어올 수 있음
def led_op(color, op):   # 라우팅의 op는 함수 안의 op와 연결 안 되어있음.
    if color == "red":
        if op == "on":
            GPIO.output(LEDr, 1) # 1 또는 GPIO.HIGH
            return '''
            <p>LED RED ON</p>
            <a href="/">Go Home</a>
            '''
        
        elif op == "off":
            GPIO.output(LEDr, 0) # 0 또는 GPIO.LOW
            return '''
            <p>LED RED OFF</p>
            <a href="/">Go Home</a>
            '''

    if color == "blue":
        if op == "on":
            GPIO.output(LEDb, 1) # 1 또는 GPIO.HIGH
            return '''
            <p>LED BLUE ON</p>
            <a href="/">Go Home</a>
            '''
            
        elif op == "off":
            GPIO.output(LEDb, 0) # 0 또는 GPIO.LOW
            return '''
            <p>LED BLUE OFF</p>
            <a href="/">Go Home</a>
            '''

if __name__ == "__main__":  # 터미널에서 직접 실행시킨 경우, 맨 밑에 있어야 함
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()