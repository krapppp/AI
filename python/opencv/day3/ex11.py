import cv2
img=cv2.imread('./pn/opencv/day3data1.jpg')
gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

eg=cv2.Canny(gry_img,100,100)
cv2.imshow('w',eg)
cv2.waitKey()