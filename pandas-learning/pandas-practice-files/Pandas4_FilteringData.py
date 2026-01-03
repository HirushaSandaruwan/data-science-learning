import pandas as pd

#loading data
bios = pd.read_csv("bios.csv")
print(bios.head(5))
print(bios.tail(5))

#filter data differently

print(bios.loc[bios['height_cm'] > 215]) #players with whose height greater than 215
#reduce columns
print(bios.loc[bios['height_cm'] > 215,['name', 'height_cm']])
#Method 2
print(bios[bios['height_cm'] > 215][['name', 'height_cm']])
#use more conditions
print(bios[(bios['height_cm']> 215) & (bios['born_country']== 'USA')][['name', 'born_country']])
#get specific name
print(bios[bios['name'].str.contains("Johnny | Williamson", case= False)])
#filter by country using 'isin'
print(bios[bios['born_country'].isin(["USA","FRA","GBR"])][['name', 'born_country']])
#add more conditions
print(bios[bios['born_country'].isin(["USA","FRA","GBR"]) & (bios['name'].str.startswith("Johnny"))][['name', 'born_country']])
#use 'query' to filter
print(bios.query('born_country=="USA" and born_region == "Washington"')[['name','born_citys' ,'born_region']])



