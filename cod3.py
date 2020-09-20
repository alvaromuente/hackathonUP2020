import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/datachevere2.csv')

percent_missing = data.isnull().sum() * 100 / len(data)
missing_value_df = pd.DataFrame({'column_name': data.columns,
                                 'percent_missing': percent_missing})
missing_value_df = missing_value_df.sort_values(by=['percent_missing'])
# missing_value_df.to_csv('missing.csv')

row_missing = data.isnull().sum(axis=1).rename('new')
temp = data.country_code
missing_value_df2 = pd.concat([data.country_code, row_missing], axis=1).reset_index()
missing_value_df2.drop(['index'], axis=1, inplace=True)
missing_value_df2 = missing_value_df2.groupby(['country_code']).sum()
missing_value_df2 = missing_value_df2.sort_values(by=['new']).reset_index()
# missing_value_df2.to_csv('missing2.csv')

borrarcol = missing_value_df[missing_value_df.percent_missing > 80]['column_name'].to_list()
data2 = data.copy()
data2.drop(borrarcol, axis=1, inplace=True)

borrarfil = missing_value_df2[-25:].country_code.to_list()

for pais in borrarfil:
    data2 = data2[data2.country_code != pais]

# Intento numero 1 de cluster
data3 = data2.copy()
data3 = data3.fillna(0)
data3.to_csv('data/datafinal1.csv')

# Intento numero 2 de cluster
data4 = data2.copy()
data4 = data4.iloc[:, 3:].apply(lambda x: x.fillna(x.mean()))
data4 = pd.concat([data2.iloc[:, 0:3], data4], axis=1).reset_index()
data4.drop(['index'], axis=1, inplace=True)
data4.to_csv('data/datafinal2.csv')

#dataval = data.iloc[:, 3:].values
