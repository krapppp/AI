import cv2
import numpy as np
import matplotlib.pyplot as plt

data=np.array([[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,1,0,0,0,0,0,0,0],
               [0,0,1,1,0,0,0,0,0,0],
               [0,0,1,1,1,0,0,0,0,0],
               [0,0,1,1,1,1,0,0,0,0],
               [0,0,1,1,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],],dtype=np.float32)

ux=np.array([[-1,0,1]])
uy=np.array([[-1,0,1]]).T
k=cv2.getGaussianKernel(3,1)
g=np.outer(k,k.T)
dx=cv2.filter2D(data,cv2.CV_32F,ux)
dy=cv2.filter2D(data,cv2.CV_32F,uy)

dyy=dy*dy
dxx=dx*dx
dyx=dy*dx

gdyy=cv2.filter2D(dyy,cv2.CV_32F,g)
gdxx=cv2.filter2D(dxx,cv2.CV_32F,g)
gdyx=cv2.filter2D(dyx,cv2.CV_32F,g)

C=(gdyy*gdxx-gdyx**2)-0.04*(gdyy+gdxx)**2

# for y in range(1, C.shape[0]-1):      # 행
#     for x in range(1, C.shape[1]-1):  # 열
#         if C[y, x] > 0.1:
#             # 3x3 이웃 중 자기 자신이 가장 큰 값인지 확인
#             if C[y, x] == np.max(C[y-1:y+2, x-1:x+2]):
#                 data[y, x] = 9

for i in range(1,C.shape[0]-1):
    for j in range(1,C.shape[1]-1):
        if C[i,j]>0.1 and sum(sum(C[j,i]>C[j-1:i+2,i-1:j+2]))==8:
            data[i,j]=9
np.set_printoptions(precision=2)

dd = [
    (dy, 'dy'),
    (dx, 'dx'),
    (dyy, 'dyy'),
    (dxx, 'dxx'),
    (dyx, 'dyx'),
    (gdxx, 'gdxx'),
    (gdyy, 'gdyy'),
    (gdyx, 'gdyx'),
    (C, 'C')
]

for x, (mat, name) in enumerate(dd):
    print(mat)
    plt.subplot(3,3,x+1)
    plt.title(name)
    plt.imshow(mat)
    plt.axis('off')

plt.show()