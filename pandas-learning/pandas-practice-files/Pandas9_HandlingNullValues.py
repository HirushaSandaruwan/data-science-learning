import pandas as pd
import numpy as np

cake = pd.read_csv('cupcake2.csv')
cake.loc[[0,1], 'Units Sold'] = np.nan

#data frame with null values
print(cake.head())

#use fillna to fill null values
cake = cake.fillna(50)
print(cake.head())

#fill with much more reasonable values
cake.loc[[0,1], 'Units Sold'] = np.nan
cake = cake.fillna(cake['Units Sold'].mean())
print(cake.head())

# Difference between mean() and interpolate():
# Example data: [10, 20, NaN, 40, 200]
#
# mean(): uses the overall average of known values
# mean = (10 + 20 + 40 + 200) / 4 = 67.5
# Result: [10, 20, 67.5, 40, 200]
#
# interpolate(): estimates missing values using neighboring values (assumes order)
# Result: [10, 20, 30, 40, 200]
#
# Mean ignores data order and is affected by outliers.
# Interpolate preserves local trends in ordered/time-based data.

#use interpolate()
cake.loc[[2,3], 'Units Sold'] = np.nan
print(cake.head())
cake ['Units Sold']= cake['Units Sold'].interpolate()
print(cake.head())

#use dropna to drop null values
cake.loc[[2,3], 'Units Sold'] = np.nan
print(cake.head())
print(cake.dropna())

#limit check for missing values only for 'Unit Sold'
cake.loc[[2,3], 'Units Sold'] = np.nan
print(cake.dropna(subset=['Units Sold']))

#use isna and notna
cake.loc[[2,3], 'Units Sold'] = np.nan
print(cake.head())
#use isna for get colums that contain null values
print(cake[cake['Units Sold'].isna()])
#use notna for gettin columns which has not null values
print(cake[cake['Units Sold'].notna()])








