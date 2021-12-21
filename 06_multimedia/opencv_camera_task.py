import cv2

cap = cv2.VideoCapture(0) #0 디바이스 번호(카메라 촬영할때)

if not cap.isOpened():
    print('Camera open failed')
    exit()


#동영상 촬영하기
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge1 = cv2.Canny(frame, 50, 100)
    if not ret:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('edge1', edge1)
    cv2.imshow('gray', gray)
    # 1000-> 1초, 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break


cap.release()
cv2.destroyAllWindows()