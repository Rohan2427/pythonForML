import numpy as np

#1. Create a null vector of size 10 but the fifth value which is 1.
m1 = np.nan * np.empty(10)
print(m1)
m1[4] = 1
print()
print(m1)

#2. Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.
x,y = map(input("Enter two numbers. ").split())
v1 = np.random.random((x,y))
print(v1)
print()
print(np.mean(v1))


