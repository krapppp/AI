import pn.numpy1 as np
np.__version__

ar1=np.array([1,2,3,4,5])
print(ar1,type(ar1))

ar2=np.array([[10,20,30],[40,50,60]])
print(ar2,type(ar2))

ar3=np.arange(1,11,2)
print(ar3,type(ar3))

ar4=np.array([1,2,3,4,5,6]).reshape((3,2))
print(ar4,type(ar4))

ar5=np.zeros((2,3))
print(ar5,type(ar5))

ar6=ar2[0:2,0:2]
print(ar6,type(ar6))

ar7=ar2[0,:]
print(ar7,type(ar7))

ar8=ar1+10
print(ar8,type(ar8))