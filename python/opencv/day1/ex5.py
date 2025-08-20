import cv2
import matplotlib.pyplot as plt

gry_img=cv2.imread('./pn/opencv/day1/dog1.jpg',cv2.IMREAD_GRAYSCALE)

print('변환 전')
print(gry_img.shape)
print(gry_img[0,0])
print(gry_img[100,100])
cv2.imshow('m',gry_img)
cv2.waitKey(0)

print('변환 후')
ret,th_img=cv2.threshold(gry_img,127,255,cv2.THRESH_BINARY)
print(gry_img.shape)
print(gry_img[0,0])
print(gry_img[100,100])

print('변환 결과')
print(th_img.shape)
print(th_img[0,0])
print(th_img[100,100])
cv2.imshow('th',th_img)
cv2.waitKey(0)