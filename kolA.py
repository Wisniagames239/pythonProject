# Zadanie 1
import math
"""
suma = 0
for i in range(14,33):
    suma+=math.pow((i**math.e + math.cos(i)),1/5)
print(round(suma,2))
"""
#Zadanie 2
"""
import random
def generuj(min, max, ile):
    lista = []
    try:
        if ile>0:
            for i in range(ile):
                lista.append(random.randint(min, max))
            print(lista)
            for i in range(len(lista)):
                lista[i]*= -1

            return lista
        else:
            print('Parametr ile nie jest naturalny')
    except TypeError:
        print('Podane argumenty nie sa liczbami')
    except ValueError:
        print('Min nie jest mniejszy od max')

print(generuj(2,5,10))
print(generuj(2,5,0))
print(generuj(5,2,3))
print(generuj('b',5,10))
"""
#Zadanie 3

def foo(nazwa_pliku):
    mak = []
    with open(nazwa_pliku) as f:
        k = f.readlines()
        for j in range(len(k)):
            c = k[j].split(' ')
            wiersz = {}
            for i in c:
                if i not in wiersz:
                    wiersz[i] = 1
                else:
                    wiersz[i] += 1
            maksi = 0
            for i in wiersz:
                if i>maksi:
                    maksi=i
            print(wiersz[maksi])

    print(mak)
foo('liczby.txt')
# Zadanie 4



