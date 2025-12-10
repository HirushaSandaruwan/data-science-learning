import numpy as np
from numpy.ma.extras import hstack, vstack

#EXERCISE 1
#create 1D array
arr = np.arange(1, 10)
print(arr)

arr2 = np.arange(11, 20)
print(arr2)

#mathematical operations with two arrays
print(arr + arr2)
print(arr2 - arr)
print(arr2 / arr)
print(arr * arr2)

print(np.sin(arr))
print(np.cos(arr))

#EXERCISE 2
#Create 2d array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

#Access specific rows and columns
print(a[0])
print(a[:, 2])

#modify elements
a[1,2] = 100
print(a)

#EXERCISE 3
#reshape 1D array into 2D array
b = np.arange(1,21)
print(b)
print(b.reshape((5,4)))

#stack 2d arrays vertically and horizontally
a1 = np.ones((5,4))
a2 = np.zeros((5,4))

print(hstack((a1, a2)))
print(vstack((a1, a2)))

#EXERCISE 4
#Create a random 2d array
arr3 = np.random.randint(1,20,(4,5))
print(arr3)

#find element greater than 10
print(arr3[arr3 > 10])
#fancy indexing
print(arr3[[0,2,3]])
print(arr3[:, [1,3]])

#Mini Project
#Analyzing Random Data
#Create a random dataset for 100 students with 3 subjects
data = np.random.randint(50,100,(100,3))
print(data)

#Calculate mean,median, standard deviation for each subject
mean = np.mean(data, axis=0)
median = np.median(data, axis=0)
Standard_deviation = np.std(data, axis=0)
print(f"Mean scores per subject: {mean}")
print(f"Median scores per subject: {median}")
print(f"Standard deviations per subject: {Standard_deviation}")

#Reshape data to explore differently
reshaped_data = np.reshape(data, (2,150))
print(reshaped_data)
