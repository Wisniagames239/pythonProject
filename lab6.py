import pandas as pd
import numpy as np

s = pd.Series([10,12,8,14], index=['a','b','c','d'])
#print(s)
data = {'Kraj':['Belgia','Indie','Brazylia'],'Stolica':['Bruksela','New Delhi','Brasilia'],'Populacja':[11190846,1303171035,207847528]}
df = pd.DataFrame(data)
#print(df)
#print(s['c'])
#print(s.c)
#print(df[0:1])
#print('')

#print(df["Populacja"])
#print('')
#print(df.iloc[0,0])
#print('')
#print(df.loc[0,'Kraj'])
#print('')
#print(df.at[0,'Kraj'])
#print('')
#print(df.loc[0])

#print('kraj: '+ df.Kraj)
#print('')
#print(df.sample())
#print('')
#print(df.sample(2))
#print('')
#print(df.sample(frac=0.5))
#print('')
#print(df.sample(n=10,replace=True))
#print('')
#print(df.head())
#print('')
#print(df.head(2))
#print('')
#print(df.tail(1))
#print('')
#print(df.describe())
#print('')
#print(df.T)

#print(s[s>9])
#print('')
#print(s.where(s>10))
#print('')
#print(s.where(s>10,'za duze'))
#print('')
#seria = s.copy()
#seria.where(seria>10,'za duze', inplace=True)
#print("######")
#print(seria)
#print('')
#print(s[~(s>10)])
#print('')
#print(s[(s<13)& (s>8)])

#print(df[df['Populacja']>12000000000])
#print(df[(df.Populacja>1000000)& (df.index.isin([0,2]))])
#
#s['e'] = 15
#print(s.e)
#s['f']=16
#print(s)
#
#df.loc[3]='dodane'
#print(df)
#
df.loc[4] = ['Polska', 'Warszawa',38675467]
#print(df)
#
#new_df = df.drop([3])
#print(new_df)
#
#df.drop([3], inplace=True)
#print(df)

#df.drop('Kraj', axis=1, inplace=True)
#print(df)
#df['Kontynent']=['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
#
#print(df.sort_values('Kraj'))
#
#grouped = df.groupby(['Kontynent'])
#print(grouped.get_group('Europa'))
#
#print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))

data = pd.read_csv('annual-enterprise-survey-2021-financial-year-provisional-csv.csv')

