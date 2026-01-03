import pandas as pd

#load data
cake = pd.read_csv('cupcake.csv')

#view data different ways
print(cake)
print(cake.head(4))
print(cake.tail(6))

#get a sample data
print(cake.sample(8))
#use random_state = 1 for stop changing
print(cake.sample(4, random_state = 1))

#get specific rows, columns
print(cake.loc[0])
print(cake.loc[[0,1,5]])
print(cake.loc[5:8])
print(cake.loc[5:8, ["Day", "Units Sold"]])
print(cake.loc[:, ["Day", "Units Sold"]]) #all rows
#when using iloc, need only index locations
print(cake.iloc[:, [0,2]])

#Modifying Values
cake.loc[4, "Units Sold"] = 50
print(cake.head())

#Get specific value
print(cake.at[4,"Units Sold"])

#Get specific column data
print(cake.Day) #use for single words without spaces
print(cake["Units Sold"])

#Sort values
print(cake.sort_values("Units Sold"))
print(cake.sort_values("Units Sold", ascending=False)) #decreasing order

'''
["Units Sold", "Cupcake Type"]
The columns used for sorting, in priority order:

First by Units Sold

If there are ties, then by Cupcake Type

ascending=[0, 1]
Specifies the sort order for each column:

0 → descending order for "Units Sold"

1 → ascending order for "Cupcake Type"
'''
print(cake.sort_values(["Units Sold", "Cupcake Type"], ascending=[0,1]))

#iterate row by row through dataframe
for index, row in cake.iterrows():
    print(index)
    print(row)  #for specific row["Unit Sold"]
    print("\n\n")