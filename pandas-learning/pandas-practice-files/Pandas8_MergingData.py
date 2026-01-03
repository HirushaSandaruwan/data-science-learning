import pandas as pd

bios = pd.read_csv('bios.csv')
noc = pd.read_csv('noc_regions.csv')
print(bios.head())
print(noc.head())

#merge two dataframes
'''
___when use left join___

Take all rows from bios

Look at the born_country code of each athlete

Find the same code in noc under NOC

Add country information (region, notes) from noc

If no match is found, put NaN

Save the result as bios2
'''

'''
bios2 → new DataFrame to store the result

pd.merge() → joins two tables together

bios → main (left) table, all rows are kept

noc → second (right) table with country info

left_on='born_country' → use born_country from bios to match

right_on='NOC' → use NOC from noc to match

how='left' → keep every row from bios, even if no match
'''

'''
Simple rule to remember
👉 Use left join when people matter more
👉 Use inner join when only valid matches matter
'''

bios2 = pd.merge(bios,noc,left_on='born_country',right_on='NOC',how= 'left') #in this example we use left join because players matter more
print(bios2.head())

#Rename
bios2.rename(columns={'region':'born_country_full'},inplace=True)
print(bios2.head())

#see mismatching items
print(bios2[bios2['NOC_x'] != bios2['born_country_full']][['name','NOC_x','born_country_full']])

#concatenating data
usa = bios[bios['born_country'] == 'USA'].copy()
print(usa.head())
fra = bios[bios['born_country'] == 'FRA'].copy()
print(fra.head())

usa_fra = pd.concat([usa,fra])
print(usa_fra.head())

#merge using 'on' and using a shared column
results = pd.read_csv('results.csv')
print(results.head())

modified_bios = pd.merge(results,bios,on = 'athlete_id',how='left')
print(modified_bios.head())

'''
modified_bios → the new DataFrame storing the result

pd.merge() → pandas function to join two tables

results → the left table (all its rows will stay)

bios → the right table (columns are added if there’s a match)

on='athlete_id' → match rows using this column from both tables

how='left' → keep all rows from results, even if there’s no match in bios
'''

