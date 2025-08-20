import cv2
import numpy as np

cam=cv2.VideoCapture(0)
if cam.isOpened()==False:
    print('연결불가')
    exit(1)
ret,img=cam.read()
if ret==False:
    print('캡쳐 불가')
    exit(1)
codec=cv2.VideoWriter_fourcc('M','J','P','G')
fps=30
h,w=img.shape[:2]
m_v=cv2.VideoWriter('m_v.avi',codec,fps,(w,h))
if m_v.isOpened()==False:
    print('동영상 생성 불가')
    exit(1)

while True:
    ret,img=cam.read()
    if ret==False:
        print('캡쳐 불가')
        break
    m_v.write(img)
    cv2.imshow('cam',img)

    key=cv2.waitKey(1)
    print(key)
    if key==27:
        break

cam.release()
m_v.release()
cv2.destroyAllWindows()