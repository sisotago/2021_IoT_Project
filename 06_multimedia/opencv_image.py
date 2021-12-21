import cv2

img = cv2.imread('a.jpg')
img2 = cv2.resize(img, (1080,720)) #이미지 사이즈 조정해서 img2에 저장
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #컬러 이미지를 흑백 변환

#Edge 선 추출
edge1 = cv2.Canny(img, 50, 100) #min max
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

#cv2.imshow('a',img)
#cv2.imshow('a2',img2) #img2 보이기
#cv2.imshow('GRAY', gray)
cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)
# cv2.waitKey(0) #키보드가 입력될 때까지 기다리기 예:10000 : 10초 기다리기, 0 : 무한대로 기다리기
# A:65, a:97, ENTER: 13, ESC:27
while True:
    if cv2.waitKey() == 13:
        break

#파일 저장하기
cv2.imwrite('a_GRAY.jpg', gray)

cv2.destroyAllWindows()
