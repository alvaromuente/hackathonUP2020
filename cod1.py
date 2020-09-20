import pandas as pd

data = pd.read_json('data/hdro_api_all.json')

listapaises = data.country_code
listapaises = listapaises.drop_duplicates()
listapaises = listapaises.reset_index(drop=True)

listavar = data.indicator_name
listavar = listavar.drop_duplicates()
listavar = listavar.reset_index(drop=True)

# table[table.column_name == some_value]
dataper = data[data.country_code == 'PER']
dataper1990 = dataper[dataper.year == 1990]
dataper2018 = dataper[dataper.year == 2018]

datausa = data[data.country_code == 'USA']
datausa2018 = datausa[datausa.year == 2018]

data.to_csv('data/data.csv', index=True, header=True)
# esta data se cargo a power query para convertirse a data chevere
