import pandas as pd

#Creating a data frame
df = pd.DataFrame([[7,6,2],[6,7,2],[9,4,3]], columns=['A','B','C'], index=['a','b','c'])

#view data different ways
print(df.head())
print(df.head(2))
print(df.tail(2))

#useful functions
print(df.columns) #see headers
print(df.index) #see index
print(df.index.tolist())

print(df.info()) #see information

print(df.describe()) #describe important information
print(df.nunique()) #see how many unique values
print(df['C'].unique()) #see unique values

print(df.shape) #Get shape of our data frame
print(df.size) #get size