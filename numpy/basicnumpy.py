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

k1 = np.arange(14).reshape(7,2)
k2 = np.arange(64).reshape(4,4,4)

print(k1)
print()
print(k2)
print()
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
print(k1.dtype)
print(k2.dtype)


#Changing datatype

#astype

#Array Operations

#Scalar Operations

#arithmetic

#relational

#Vector Operations

#arithmetic

#numpy array functions
#max/min/sum/prod
#mean/median/std/var

#trignometric functions

#dot product

#log and exponent

#round/floor/ceil

#Indexing and Slicing 

#Iterating numpy arrays

#transpose

#ravel

#Stacking
#horizontal stacking
#vertical stacking

#Spliting
#horizontal split 
#vartical split


