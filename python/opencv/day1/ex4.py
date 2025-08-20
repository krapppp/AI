import cv2
import numpy as np

data=cv2.VideoCapture('m_v.avi')
while True:
    ret,img=data.read()
    if data.isOpened()==False:
        print('파일 로드 불가')
        break
    cv2.imshow('m',img)
    key=cv2.waitKey(30)
    if key==27:
        print('동영상 지루해')
        break

data.release()
cv2.destroyAllWindows()