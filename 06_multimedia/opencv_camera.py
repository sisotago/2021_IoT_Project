import cv2

cap = cv2.VideoCapture() #0 디바이스 번호(카메라 촬영할때)

if not cap.isOpened():
    print('Camera open failed')
    exit()

# fourcc(four character code)
# DIVX(avi), MP4V(mp4), X264(h264)
#fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 첫번째 방법, ('D','I','V','X') 두번째 방법  파일 저장할 때 필요
#                        파일명    비디오명fps 프레임 사이즈
#out = cv2.VideoWriter('output.avi',fourcc,30,(640,480))    파일 저장할 때 필요

#카메라 사진 찍기
#ret, frame = cap.read() #read : 사진 한 컷
#cv2.imshow('frame', frame)
#cv2.imwrite('output.jpg', frame)
#cv2.waitKey(0)

#동영상 촬영하기
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    #out.write(frame)
    # 1000-> 1초, 10 -> 0.01초
    if cv2.waitKey(10) == 13:
        break


#사용자 자원 해제
cap.release()
#out.release()
cv2.destroyAllWindows()