import numpy as np

#Load data from file
filedata =np.genfromtxt('dataset.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)

#Boolean Masking and Advanced Indexing
print(filedata > 50)
print(filedata[filedata > 50])
print((filedata > 50) & (filedata < 100))
print(~((filedata > 50) & (filedata < 100)))

#index with a list
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])

#greater than value check raw wise, column wise
print(np.any(filedata > 50, axis =0)) #any value

print(np.all(filedata > 50, axis =0)) #all value

print(np.any(filedata > 50, axis =1))