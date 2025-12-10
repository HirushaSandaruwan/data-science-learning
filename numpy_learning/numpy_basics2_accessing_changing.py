import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

#Get a specific element [r, c]
print(a[1,5])

#Get a specific row
print(a[0, :])

#Get a specific column
print(a[:, 4])

#Getting a little more fancy [start index:end index:stepsize]
print(a[0, 1:6:2])

#Change elements
a[1, 5] = 20
print(a)

a[:, 3]= 8
print(a)

'''
#for different numbers
a[:, 3] = [8,6]

'''

#3d example
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)

#Get a specific element
print(b[1,1,0])

#Get specific columns
print(b[:,1,:])

#replace
b[:,1 ,:] = [[9,9],[8,8]]
print(b)
