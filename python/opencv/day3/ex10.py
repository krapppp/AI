import cv2

img=cv2.imread('./pn/opencv/day3/data1.jpg')
gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gr_dx=cv2.Sobel(gry_img,cv2.CV_32F,1,0,ksize=3)
gr_dy=cv2.Sobel(gry_img,cv2.CV_32F,0,1,ksize=3)

s_x=cv2.convertScaleAbs(gr_dx)
s_y=cv2.convertScaleAbs(gr_dy)
eg_d=cv2.addWeighted(s_x,0.5,s_y,0.5,0)

cv2.imshow('img',img)
cv2.imshow('gry_img',gry_img)
cv2.imshow('dx_img',gr_dx)
cv2.imshow('dy_img',gr_dy)
cv2.imshow('eg_img',eg_d)

cv2.waitKey()