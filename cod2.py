import pandas as pd

data = pd.read_csv('datachevere.csv')
data = data[data.year != 2020]

data = data.sort_values(by=['country_code', 'year'])
data = data.reset_index(drop=True)

listap = data.country_code
listap = listap.drop_duplicates()
listap = listap.reset_index(drop=True)

listay = data.year
listay = listay.drop_duplicates()
listay = listay.reset_index(drop=True)

data2 = data

for i in range(0, 6):
    for j in range(0, 4):
        data2['year'].replace(1991 + j + i * 5, 1990 + i * 5, inplace=True)

data2 = data2.groupby(['country_code', 'country_name', 'year']).first()

data2.to_csv('datachevere2.csv', index=True, header=True)
