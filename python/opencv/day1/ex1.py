import cv2
import matplotlib.pyplot as plt
# import sys
# print(sys.executable)

data=cv2.imread('./pn/opencv/day1/dog1.jpg',cv2.IMREAD_COLOR)
data1=cv2.imread('./pn/opencv/day1/dog1.jpg',cv2.IMREAD_COLOR)
cv2.namedWindow('m')
cv2.imshow('m',data)
rgb_img=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
print(type(data))
print(type(data1))
cv2.waitKey(0)
plt.imshow(data)
plt.show()
