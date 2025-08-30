import numpy as np

#1. Create a null vector of size 10 but the fifth value which is 1.
m1 = np.nan * np.empty(10)
print(m1)
m1[4] = 1
print()
print(m1)

#2. Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.
x,y = map(int, input("Enter two numbers. ").split())
v1 = np.random.random((x,y))
print(v1)
print()
print(np.mean(v1))

#3. Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array shape as (a,b) as parameter to function.
def midzero(a,b):
    v2 = np.ones((a,b))
    v2[1:-1,1:-1] = 0
    return(v2)

midzero(4,6)

#4. Create a vector of size 10 with values ranging from 0 to 1, both excluded.
np.linspace(0, 1, 12)[1:-1]


#5. Can you create a identity mattrix of shape (3,4). If yes write code for it.
# No we can't create such mattrix. but we can create identity mattrix with following methods:
mat1 = np.eye(4)
mat2 = np.identity(5)
print(mat1)
print(mat2)

#6. Create a 5x5 matrix with row values ranging from 0 to 4.

#7. Consider a random integer (in range 1 to 100) vector with shape (10,2) representing coordinates, and coordinates of a point as array is given.
#  Create an array of distance of each point in the random vectros from the given point. Distance array should be interger type.

#8. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?

#9. Arrays
#You are given a space separated list of numbers. Your task is to print a reversed NumPy array with the element type float.
#Input Format:
#A single line of input containing space separated numbers.
#Output Format:
#Print the reverse NumPy array with type float.

#10. Elements count
#Count the number of elements of a numpy array.

#11.

#12.

#13.
