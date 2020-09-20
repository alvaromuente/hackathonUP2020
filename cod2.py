import pandas as pd

data = pd.read_csv('datachevere.csv')
data = data[data.year != 2020]

data = data.sort_values(by=['country_code', 'year'])
data = data.reset_index(drop=True)

listap = data.country_code
listap = listap.drop_duplicates()
listap = listap.reset_index(drop=True)

dataxp = []
for i in listap:
    temp = data[data.country_code == i]
    dataxp.append(temp)

# for i in range(len(dataxp)):
#     if not dataxp[i].shape == (29, 149):
#         print(data['country_code'][0:1]

listafinal = []
for pais in dataxp:
    for column in pais.columns[3:]:
        listafinal.append(column)
    # print(i[0:1])

    # print(i[5:6])
    # print(i[10:11])
    # print(i[15:16])
    # print(i[20:21])
