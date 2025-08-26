import cv2
oj_img=cv2.imread('./pn/opencv/day2/data1.jpg')#.위로 올라가기 ,/들어가기
img=oj_img.copy()
def cut(event,x,y,f,p):
    global sx,sy,ex,ey,img
    if event==cv2.EVENT_LBUTTONDOWN:
        sx,sy=x,y
    elif event==cv2.EVENT_LBUTTONUP:
        ex,ey=x,y
        img=img[sy:ey,sx:ex]
    cv2.imshow('img',img)

# cv2.namedwindow('img')
cv2.imshow('img',img)
cv2.setMouseCallback('img',cut)
run=True
while True:
    key=cv2.waitKey(1)
    if key==ord('a'):
        run==False
    if key==ord('c'):
        img=oj_img.copy()
        cv2.imshow('img',img)
else:
    cv2.destroyAllWindows()