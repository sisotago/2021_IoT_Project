import cv2

# xml 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

# gray스케일 이미지로 변경
img = cv2.imread('human.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지에서 얼굴 검출
faces = face_cascade.detectMultiScale(gray)

# 얼굴 위치에 대한 좌표 정보 가져오기
for (x, y, w, h) in faces:
    # 원본 이미지에 얼굴 위치 표시
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2) # 사진, 시작 좌표, 끝나는 좌표, 색(255,0,0)=blue, 선의 두께

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()