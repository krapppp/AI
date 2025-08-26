import cv2

img=cv2.imread('./pn/opencv/day3/data1.jpg')
gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # 밝기 파악하여 영역 선정
cv2.imshow('img',img)
cv2.imshow('gry_img',gry_img)

t,tr_img=cv2.threshold(gry_img,119,255,cv2.THRESH_OTSU)
cv2.imshow('tr_img',tr_img)
cv2.waitKey(0)

t1,tr_img=cv2.threshold(gry_img,119,255,cv2.THRESH_BINARY)
cv2.imshow('tr_img',tr_img)
cv2.waitKey(0)

t2,tr_img=cv2.threshold(gry_img,119,255,cv2.THRESH_BINARY_INV)
print(t,t1,t2)

cv2.imshow('tr_img',tr_img)
cv2.waitKey(0)