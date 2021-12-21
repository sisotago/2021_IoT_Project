from flask import Flask

# Flask() 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 라우팅(클라이언트로부터 요청받은 URL과 특정한 뷰를 매칭시키는 것)을 위한 뷰 함수, 라우팅에는 동적 라우팅과 정적 라우팅이 있음.
@app.route("/") # @app.route(호출할 URL) /는 정적 라우팅
def hello():    # <p>태그 : p = paragraph = 문단 (문단을 나눌 때), <a>태그 : anker : 다른 URL로 이동 가능, 여는 태그랑 닫는 태그(</태그>) 한 쌍
    return '''
    <p>Hello, Flask!</p> 
    <a href="/first">Go First</a>
    <a href="/second">Go Second</a>
    '''

@app.route("/first")
def first():
    return '''
    <p>First Page</p>
    <a href="/">Go Home</a>
    '''

@app.route("/second")
def second():
    return '''
    <p>Second Page</p>
    <a href="/">Go Home</a>
    '''




# 터미널에서 직접 실행시킨 경우만 app run (앱 실행)
if __name__ == "__main__":  # 터미널에서 직접 실행시킨 경우, 맨 밑에 있어야 함
    app.run(host="0.0.0.0")