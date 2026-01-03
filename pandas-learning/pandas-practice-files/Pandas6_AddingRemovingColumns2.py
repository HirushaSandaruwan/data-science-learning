import pandas as pd

bios = pd.read_csv('bios.csv')
print(bios.head())

#get a copy
bios_new = bios.copy()

#get the first name
'''
str. = tells pandas you want to apply string operations
split(' ')  = this splits each name where there is a space and each name become a list of words
str[0] = grab the first element of the list
'''
bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]
print(bios_new)

#filter data using new column
print(bios_new.query('first_name == "John"'))

#convert born date to a datetime object
bios_new['born_datetime'] = pd.to_datetime(bios_new['born_date'])
print(bios_new.info())
print(bios_new.head())

#use of date time object
bios_new['born_year'] = bios_new['born_datetime'].dt.year #dt. = use pandas date time properties
print(bios_new[['name','born_year']])

#save bios_new to a new csv file
bios_new.to_csv('bios_new.csv',index = False)