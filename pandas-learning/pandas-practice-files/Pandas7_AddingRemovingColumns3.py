import pandas as pd

bios = pd.read_csv('bios.csv')
print(bios.head())

#catogorize depending height
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 160 else ('Average' if x < 180 else 'Tall'))
print(bios.head())

#categorize data using a function
def categorize_athlete (row):
    if row['height_cm'] < 160 and row['weight_kg'] < 65:
        return 'Light Weight'
    elif row['height_cm'] < 180 and row['weight_kg'] <= 80:
        return 'Middle Weight'
    else:
        return 'Heavy Weight'

bios['category'] = bios.apply(categorize_athlete, axis=1) #call the function # axis=1 --> horizontal axis
print(bios.head())
