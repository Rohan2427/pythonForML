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

linmet = np.linspace(1,200,20)
print(linmet)
print()

linmet1 = np.linspace(4,40,8)
print(linmet1)
print(type(linmet1))
print()


idmet1 = np.identity(2)
print(idmet1)
print()

idmet2 = np.identity(4)
print(idmet2)
print()

#numpy array attributes

#ndim/shape/size/itemsize/dtype

k0 = np.arange(81)
k1 = np.arange(14).reshape(7,2)
k2 = np.arange(64).reshape(4,4,4)
k6 = np.array([[[3,8],[98,2],[7,49]],[[51,19],[19,5],[40,72]]])

print(k1)
print()
print(k2)
print()
print(k0.ndim)
print(k1.ndim)
print(k2.ndim)
print()
print(k1.shape)
print(k2.shape)
print()
print(k1.size)
print(k2.size)
print()
print(k1.itemsize)
print(k2.itemsize)
print()
print(k0.dtype)
print(k1.dtype)
print(k2.dtype)


#Changing datatype
#astype
k2.astype(np.int32)

#Array Operations
#Scalar Operations

#arithmetic

r0 = k0 + 2
print(r0)
r0 = k0 * 2
print(r0)
r0 = k0 - 2
print(r0)
r0 = k0 / 2
print(r0)
r0 = k0 % 2
print(r0)
#relational
r1 = k1 < 7
print(r1)


#Vector Operations

#arithmetic
k3 = np.arange(12).reshape(6,2)
k4 = np.random.random(12).reshape(6,2)

print(k3)
print(k4)
print()

s1 = k3 + k4
print(s1)

#numpy array functions
#max/min/sum/prod
np.prod(k0)
np.sum(k1)
np.max(k2)
np.min(k2)


print(k1)
print()
print(np.max(k1, axis=0))
print(np.max(k1, axis=1))
print()
print(np.min(k6, axis=0))
print(np.min(k6, axis=1))


#mean/median/std/var
print(np.mean(k6))
print(np.median(k6))
print(np.std(k6))
print(np.var(k6))

print(k1)
print()

print(np.mean(k1))
print(np.mean(k1, axis=0))
print(np.mean(k1, axis=1))
print(np.median(k1))
print(np.median(k1, axis=0))
print(np.median(k1, axis=1))
print(np.std(k1))
print(np.std(k1, axis=0))
print(np.std(k1, axis=1))
print(np.var(k1))
print(np.var(k1, axis=0))
print(np.var(k1, axis=1))

#trignometric functions

#dot product

k7 = np.array([[2,3],[44,6],[7,38]])
k8 = np.array([[37,1,3],[84,4,0]])
np.dot(k7,k8)

#log and exponent
print(np.log(k0))
print(np.log(k1))
print(np.exp(k0))

#round/floor/ceil

k9 = np.array([[4.938367,1.5927763,1.4927763],[5.3228,4.118,1.5927763],[9.33,4.003,1.5927763]])
print(np.floor(k9))
print()
print(np.ceil(k9))
print()
print(np.round(k9))


#Indexing and Slicing 
print(k1)
print()
k1[5,1]

print(k2)
print()
k2[1,3,0]

print(k0)
print()
k0[3:31:3]


k9 = np.array([[2,95,3,88],[3,94,13,55],[2,836,2,0],[39,74,0,25],[5,3,2,22],[7,3,98,2]])
print(k9)
print()
k9[:,2]

print(k9)
print()
k9[3:5,2:]

print(k9)
print()
k9[2:4,1:3]

print(k9)
print()
k9[::5,::3]

print(k2)
print("----------------------")
print(k2[::5,1:3,1:3])
print("----------------------")
print(k2[1:3:,:1:,::3])

#Iterating numpy arrays

#transpose

#ravel

#Stacking
#horizontal stacking
#vertical stacking

#Spliting
#horizontal split 
#vartical split


