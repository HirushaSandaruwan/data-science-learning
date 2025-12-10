import numpy as np

#all 0's matrix
print(np.zeros(5))
print(np.zeros((2,3)))
print(np.zeros((2,2,3)))

#all 1's matrix
print(np.ones((4,2,3), dtype='int32'))

#any other number
print(np.full((2,2),99))

#any other number (full_like)
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(np.full_like(a,4))

#Random decimal numbers
print(np.random.rand(2,3))
print(np.random.random_sample(a.shape))

#Random integer values
print(np.random.randint(4,7, size=(2,3)))

#The identity matrix
print(np.identity(5))

#repeat an array
arr = np.array([[1,2,3]])
arr2 = np.repeat(arr,3,)
print(arr2)
arr3 = np.repeat(arr,3,axis= 0) #need to make the 'arr' two dimension first
print(arr3)

#Exercise
output= np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1]= 9
print(z)
output[1:4,1:4]= z
print(output)

#when copying an array use "copy()"
a = np.array([1,2,3])
b=a.copy()
b[0] = 100
print(b)
print(a)


