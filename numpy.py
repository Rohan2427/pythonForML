#Introduction to NumPy

import numpy as np

g = np.array([1,2,3])
print(g)


f = np.array([3,4,5])
print(type(f))
print(f)

d2 = np.array([[5,6,7],[7,8,9]])
print(d2)
print(type(d2))

d3 = np.array([[[1,2,3],[3,4,5],[5,6,7]]])
d34 = np.array([[[2,3,4],[89,3,8],[4,61,5]]])
print(d3)
print(type(d3))
print(d34)
z = d3 + d34
print(z)
print(type(z))

