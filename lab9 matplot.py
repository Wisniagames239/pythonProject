import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Zad1 i 2
#x = np.arange(1,20)
#y = 1/x
#plt.plot(x,y,'g^:')
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.legend(labels=['f(x)=1/x'])
#plt.axis([0,20,0,1])
#plt.title('Wykres funkcji f(x) dla x[1,20]')
#plt.show()
#Zad 3
#x = np.arange(0.,31.,0.1)
#sinus = np.sin(x)
#cosin = np.cos(x)
#plt.plot(x,sinus,'blue')
#plt.plot(x,cosin, 'green')
#plt.legend(['sin(x)','cos(x)'])
#plt.xlabel('x')
#plt.ylabel('f(x)')
#plt.show()
#Zad 4
#Zad 5
df = pd.read_excel('imiona.xlsx')
grupa1 = df.groupby('Plec').agg({'Liczba':['sum']})
grupa2 = df.groupby('Plec')
grupam=grupa2.get_group('M').groupby('Rok', as_index=None).agg({'Liczba':['sum']})
grupak= grupa2.get_group('K').groupby('Rok',as_index=None).agg({'Liczba':['sum']})
grupka = df.groupby('Rok').agg({'Liczba':['sum']})
fig, axes = plt.subplots(1,3)
ax1 = grupa1.plot(kind='bar', ax = axes[0])
ax1.legend(['urodzenia'])
ax1.set_xlabel('Plec')
ax1.set_ylabel('Liczba')
ax2=plt.plot(df['Rok'].unique(), grupak['Liczba'],'r')
ax2=plt.plot(df['Rok'].unique(), grupam['Liczba'],'g')
ax3 = grupka.plot(kind='barh',ax = axes[1])
plt.tight_layout()
plt.show()