import cv2
#이미지 준비
img=cv2.imread('data1.jpg')
r=(0,0,255)
g=(0,255,0)
b=(255,0,0)
ck=[r,g]
#이벤트 함수 정의
def draw(event,x,y,f,p):
    global ix,iy
    if event == cv2.EVENT_MOUSEMOVE and f==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),5,ck[0],-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        ck.reverse()
    cv2.imshow('img',img)
    
cv2.imshow('img',img)#화면 생성(윈도우 생성으로 변환 가능)
cv2.setMouseCallback('img',draw)#콜백함수 정의
run=True
while run:#반복동작 정의
    key=cv2.waitKey(1)
    if key==ord('a'):
        run=False
else:
    #자원 정리
    cv2.destroyAllWindows()