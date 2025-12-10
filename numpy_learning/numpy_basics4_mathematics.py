import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

#basic maths
print(a+2)
print(a-2)
print(a*2)
print(a/2)

#add two arrays
b = np.array([1, 0, 1, 0])
print(a+b)

#get power
print(a ** 2)

#Take sin,cos value
print(np.sin(a))
print(np.cos(a))

#linear algebra
c = np.ones((2,3))
print(c)
d = np.full((3,2),2)
print(d)
print(np.matmul(c,d))

#find the determinant
c = np.identity(3)
print(np.linalg.det(c))

#statistics
stats = np.array([[1,2,3],[4,5,6]])
print(stats)

#find min
print(np.min(stats))
print(np.min(stats, axis=0))
print(np.min(stats, axis=1))

#find max
print(np.max(stats))
print(np.max(stats, axis=0))
print(np.max(stats, axis=1))

#find sum
print(np.sum(stats))
print(np.sum(stats, axis=0))
print(np.sum(stats, axis=1))