import cv2

cap = cv2.VideoCapture(0) #0 디바이스 번호(카메라 촬영할때)

if not cap.isOpened():
    print('Camera open failed')
    exit()

ret, frame = cap.read()

# xml 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 이미지에서 얼굴 검출
    faces = face_cascade.detectMultiScale(frame)
    
    # 얼굴 위치에 대한 좌표 정보 가져오기
    for (x, y, w, h) in faces:
        # 원본 이미지에 얼굴 위치 표시
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # 사진, 시작 좌표, 끝나는 좌표, 색(255,0,0)=blue, 선의 두께

    cv2.imshow('frame', frame)

    # 1000-> 1초, 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
