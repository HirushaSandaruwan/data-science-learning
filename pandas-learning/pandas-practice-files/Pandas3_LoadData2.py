import pandas as pd

cake = pd.read_csv('cupcake.csv')

#remove numerical index value
cake.index = cake["Day"]
print(cake.head())

# cant use loc [1:4]
print(cake.loc["Monday"])
print(cake.loc["Monday" : "Wednesday", "Units Sold"])
