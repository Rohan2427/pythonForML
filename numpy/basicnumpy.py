#basics of numpy

import numpy as np

vec1 = np.array([3,0,6], dtype = bool)
print(vec1)
print()
met1 = np.array([[4,5,7],[0,16,4]])
print(met1)
print()
ten1 = np.array([[[3,22],[0,50]],[[8,0],[0,90]]])
print(ten1)
print()
ten2 = np.array([[[4,65,20],[1,4,0]],[[20,7,0],[3,40,27]]], dtype = bool)
print(ten2)

#np.arange
ten3 = np.arange(6,121,6).reshape(4,5)
print(ten3)

#np.ones and np.zeros (should be used with tupple notation -> () )
met2 = np.ones((2,5))
print(met2)
print()
met3 =np.zeros((2,5))
print(met3)


#np.random
f = np.random.random((2,4))
print(f)
print()

t = np.random.random((2,4))
print(t)
print()
