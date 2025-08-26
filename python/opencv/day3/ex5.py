import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('./pn/opencv/day3/data1.jpg')
gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g_h=cv2.calcHist([gry_img],[0],None,[256],[0,256])
cv2.imshow('gr_img',gry_img)
plt.plot(g_h)

e_img=cv2.equalizeHist(gry_img)
e_h=cv2.calcHist([e_img],[0],None,[256],[0,256])
cv2.imshow('e_img',e_img)
plt.plot(e_h)
plt.show()
cv2.waitKey()