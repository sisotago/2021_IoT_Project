from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 4

# Flask() 객체 생성
# __name__은 파일명
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)


# 라우팅(클라이언트로부터 요청받은 URL과 특정한 뷰를 매칭시키는 것)을 위한 뷰 함수, 라우팅에는 동적 라우팅과 정적 라우팅이 있음.
@app.route("/") # @app.route(호출할 URL) /는 정적 라우팅
def led():    # <p>태그 : p = paragraph = 문단 (화면에 출력), <a>태그 : anker : 다른 URL로 이동 가능, 여는 태그랑 닫는 태그(</태그>) 한 쌍
    return render_template("led.html")

@app.route("/led/<op>") # 동적 라우팅, led까지는 같고 op자리에는 다른 값이 들어올 수 있음
def led_op(op):   # 라우팅의 op는 함수 안의 op와 연결 안 되어있음.
    if op == "on":
        GPIO.output(LED_PIN, 1) # 1 또는 GPIO.HIGH
        return "LED ON"
    
    elif op == "off":
        GPIO.output(LED_PIN, 0) # 0 또는 GPIO.LOW
        return "LED OFF"

    else:
        return "Error"


# 터미널에서 직접 실행시킨 경우만 app run (앱 실행)
if __name__ == "__main__":  # 터미널에서 직접 실행시킨 경우, 맨 밑에 있어야 함
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()