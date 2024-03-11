import math
from random import *


def zad1():
    a = {1-x for x in range(1, 11)}
    print(a)
    b = {4**i for i in range(8)}
    print(b)
    c = {x for x in b if x % 2 == 0}
    print(c)


def zad2():
    lista1 = []
    for i in range(10):
        lista1.append(randrange(100))
    print(lista1)
    lista2 = [x for x in lista1 if x % 2 == 0]
    print(lista2)


def zad3():
    produkty = {'jajka': 'sztuki', 'ziemniaki': 'kg', 'mąka': 'kg', 'mleko': 'litr'}
    print(produkty)
    sztuki = [x for x in produkty if produkty[x] == 'sztuki']
    print(sztuki)


def zad4():
    def prostokatny(a, b, c):
        if a**2+b**2 == c**2 or a**2+c**2 == b**2 or b**2+c**2 == a**2:
            return True

        return False

    print(prostokatny(3, 4, 5))
    print(prostokatny(6, 10, 8))
    print(prostokatny(12, 13, 5))
    print(prostokatny(15, 13, 5))


def zad5():
    def pole_trapezu(a=3, b=5, h=1):
        return (a+b)*h/2
    print(pole_trapezu())
    print(pole_trapezu(5))
    print(pole_trapezu(4, 7))
    print(pole_trapezu(4, 7, 8))


def zad6():
    def iloczyn(a=1, b=4, ile=10):
        iloczy = a
        for i in range(ile):
            iloczy *= b
        return iloczy
    print(iloczyn())
    print(iloczyn(2))
    print(iloczyn(2, 10))
    print(iloczyn(2, 10, 50))


def zad7():
    n = float(input('Podaj liczbe'))
    try:
        pierwiastek = math.sqrt(n)
    except ValueError:
        print("Nie możesz obliczyć pierwiastka z l ujemnej")
    else:
        print(pierwiastek)


def main():
    wybor = input('Jakie zadanie mam ci zrobic: ')
    if wybor.isnumeric():
        wybor = int(wybor)
        match wybor:
            case 1:
                zad1()
            case 2:
                zad2()
            case 3:
                zad3()
            case 4:
                zad4()
            case 5:
                zad5()
            case 6:
                zad6()
            case 7:
                zad7()
            case _:
                print('Nie ma takiego zadania')
    else:
        print('To nie jest liczba naturalna')


if __name__ == "__main__":
    main()
    