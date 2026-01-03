import pandas as pd

bios = pd.read_csv('bios.csv')

#use value counts
print(bios['born_city'].value_counts())
#getting only USA regions
print(bios[bios['born_country']=='USA']['born_region'].value_counts())
print(bios[bios['born_country']=='USA']['born_region'].value_counts().tail(20))

cake = pd.read_csv('cupcake2.csv')
print(cake.head())
#use group by for finding sum for cup cake type
print(cake.groupby(['Cupcake Type'])['Units Sold'].sum())
#average per day
print(cake.groupby(['Cupcake Type'])['Units Sold'].mean())
#find different things
print(cake.groupby(['Cupcake Type']).agg({'Units Sold': 'sum', 'revenue': 'mean' }))
#group by different things
print(cake.groupby(['Cupcake Type', 'Day']).agg({'Units Sold': 'sum', 'revenue': 'mean' }))






