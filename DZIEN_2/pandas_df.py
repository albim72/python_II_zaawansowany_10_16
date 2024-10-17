import pandas as pd

#tworzenie obiektu dataframe
data = {
    'Imię':['Jan','Piotr','Inga','Lila'],
    'Wiek':[34,21,39,18],
    'Miasto':['Warszawa','Gdańsk','Lublin','Kraków']
}

df = pd.DataFrame(data)


print(df)
print("_"*60)
filtered_df = df[df['Wiek']>30]
print(filtered_df)

mean_age = df['Wiek'].mean()
print(f'średni wiek: {mean_age} lat')

print('pobieranie danych....')
ultradata = pd.read_csv('zawody.csv')
print("_"*60)
print(ultradata)
npultra = ultradata.to_numpy()
print(npultra)

l1 = list(npultra[0])
print(l1)
