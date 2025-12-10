import numpy as np

#creating 1D array
a = np.array([1,2,3,4,5], dtype='int32')
print(a)

#creating 2D array
b = np.array([[4.0,8.0,12.0],[4.0,9.0,2.0]])
print(b)

#number of dimension
print(a.ndim)
print(b.ndim)

#get shape
print(a.shape)
print(b.shape)

#get type
print(a.dtype)

#get size
print(a.itemsize)
print(b.itemsize)

#number of elements
print(a.size)
print(b.size)

#get total size
#method 1
print(a.size * a.itemsize)
#method 2
print(a.nbytes)






