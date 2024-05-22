#Zad 1
import pandas as pd
import numpy as np
data = pd.read_excel('imiona.xlsx')
#Zad 2
#print(data[data['Liczba']>1000])

#print(data.Imie[data.Imie =='DOMINIK'])

#print(sum(data.Liczba))

#print(data[data.Rok.isin(np.arange(2000,2006))].agg({"Liczba":['sum']}))

#print(f'Suma chłopców = {data[data.Plec == 'M'].agg({"Liczba":['sum']})}\nSuma dziewczynek = {data[data.Plec == 'K'].agg({"Liczba":['sum']})}')

#grouped = data.groupby(['Rok', 'Plec']).max('Liczba')
#print(data[data['Liczba'].isin(grouped['Liczba'])])

grupa = data.groupby('Plec', group_keys=False, as_index=True).max('Liczba')
print(data[data['Liczba'].isin(grupa['Liczba'])])

#Zad 3
df = pd.read_csv('zamowienia.csv', delimiter=';')

#print(df['Sprzedawca'].unique())

#print(df.sort_values(by='Utarg', ascending=False).head(5))

#print(df.groupby(['Sprzedawca'])['Sprzedawca'].count())

#print(df.groupby('Kraj')['Kraj'].count())

#polski = df.groupby('Kraj').get_group('Polska')
#print(polski[(polski['Data zamowienia']>='2005-01-01')&(polski['Data zamowienia']<='2005-12-31')].value_counts('Kraj'))

#print(round(df.Utarg[(df['Data zamowienia']>='2004-01-01')&(df['Data zamowienia']<='2004-12-31')].mean(),2))

#dane2004 = df[(df['Data zamowienia']>='2004-01-01')&(df['Data zamowienia']<='2004-12-31')]
#dane2005 = df[(df['Data zamowienia']>='2005-01-01')&(df['Data zamowienia']<='2005-12-31')]
#dane2004.to_csv('zamówienia_2004.csv')
#dane2005.to_csv('zamówienia_2005.csv')