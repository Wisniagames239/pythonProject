import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from betterprint import Printing
printf = Printing.printf

#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#print(ts)
#ts.plot()
#plt.show()

#data = {'Kraj':['Belgia','Indie','Brazylia','Polska'],'Stolica':['Bruksela','New Delhi','Brasilia', 'Warszawa'],'Kontynent':['Europa','Azja','Ameryka Południowa','Europa'],'Populacja':[11190846,1303171035,207847528, 38675467]}
#df = pd.DataFrame(data)
#print(df)
#grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
#print(grupa)
#grupa.plot(kind='bar', xlabel='Kontynent', ylabel='Mld', rot=0, legend=True, title='Populacja z podziałem na kontynenty')
#plt.xticks(rotation=0)
##plt.savefig('wykres.png')
#plt.show()

#df = pd.read_csv('dane.csv', header=0, sep=';', decimal=".")
#print(df)
#grupa=(df.groupby(['Imię i nazwisko']).agg({"Wartość zamówienia":["sum"]}))
#grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red','green'])
#plt.legend(loc='lower right')
#plt.title('Suma zamówienia dla sprzedawcy')
#plt.show()
#ts = pd.Series(np.random.randn(1000))
#ts = ts.cumsum()
#
#df = pd.DataFrame(ts, columns=['wartości'])
#printf(df)
#
#df['Średnia krocząca'] = df.rolling(window=50).mean()
#df.plot()
#plt.legend()
#plt.show()

df = pd.read_excel("imiona.xlsx")
#Zad 1

#grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
#grupa.plot()
#plt.legend()
#plt.xlabel("Rok")
#plt.xticks(df['Rok'].unique(),rotation=90)
#plt.ylabel('Liczba Urodzeń')
#plt.title("Wykres liczby urodzeń ")
#plt.show()
#Zad2

#grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
#grupa.plot(kind='bar', xlabel='Płeć', ylabel='Liczba Urodzeń (Mln)', title='Wykres liczby urodzeń względem płci' )
#plt.legend()
#plt.show()
#Zad3
#grupa= df[df['Rok']>2012].groupby(['Plec']).agg({'Liczba':['sum']})
#grupa.plot(kind='pie', subplots = True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red','green'])
#plt.legend(['Chłopacy', 'Dziewczyny'])
#plt.title('Wykres % urodzonych według płci')
#plt.show()
#Zad4
data = pd.read_csv('zamowienia.csv', delimiter=';')
grupa = data.groupby('Sprzedawca')['Sprzedawca'].count()
grupa.plot(kind='bar', xlabel='Sprzedawca', ylabel='Ilosc zamowien', title='Wykres ilości zamowień u kazdego sprzedawcy')
plt.legend(['Ilosc zamowien'])
plt.show()
print(grupa)