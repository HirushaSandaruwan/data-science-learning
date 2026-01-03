import pandas as pd
import numpy as np

cake = pd.read_csv('cupcake.csv')
#add a new column
cake['price'] = 5.12
print(cake.head())

#specified prices using numpy
cake['new_price'] = np.where(cake['Cupcake Type'] == 'Vanilla',4.12,6.12)
print(cake)

#removing a column
cake = cake.drop(columns = ['price']) # method 2 --> cake.drop(columns = ['price'], inplace = True)
print(cake)

#when creating a new data frame always use ".copy()"
cake_new = cake.copy()
cake_new = cake_new.drop (columns = ['Cupcake Type'])
print(cake_new)
print(cake)

'''
when you only need few columns you can also use this method
cake = cake [['Day' , 'Cupcake Type']]

'''

#calculations
cake ['revenue'] = cake['Units Sold'] * cake['new_price']
print(cake)

#rename columns
cake = cake.rename(columns = {'new_price' : 'price'})
print(cake.head())




