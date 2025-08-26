import cv2

img=cv2.imread('./pn/opencv/day4/data4-1.jpg')
gry_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift=cv2.SIFT_create() # ck=cv2.-> ck.create()
ck=cv2.SIFT()
sift2=ck.create()
print(sift,sift2)

kp,des=sift2.detectAndCompute(gry_img,None)
gry_img_ck=cv2.drawKeypoints(gry_img,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

img2=cv2.imread('./pn/opencv/day4/data4-2.jpg')
gry_img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
sift2_1=cv2.SIFT_create() # ck=cv2.-> ck.create()
kp,des=sift2_1.detectAndCompute(gry_img2,None)
gry_img_ck2=cv2.drawKeypoints(gry_img2,kp,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('kp_img',gry_img_ck)
cv2.imshow('kp_img2',gry_img_ck2)
cv2.waitKey(0)
cv2.destroyAllWindows()