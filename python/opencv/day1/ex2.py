import cv2
import numpy as np

cam=cv2.VideoCapture(0)
if cam.isOpened()==False:
    print('연결불가')
    exit(1)
else:
    # print('카메라 인식됨')
    ret,img=cam.read()
    while True:
        if ret==False:
            print('캡쳐 불가')
            break
        cv2.imshow('cam',img)
        key=cv2.waitKey(1)
        if key==27:
            break
cam.release()
cv2.destroyAllWindows()