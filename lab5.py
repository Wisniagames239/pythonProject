import random

import numpy as np
import math


def zad1():
    a = np.arange(3)
    b = np.arange(0,9,3)
    print(a*b)

def zad2():
    a = np.arange(9).reshape([3,3])
    b = np.arange(16,0,-1).reshape([4,4])
    print("Maksymalne liczby w wierszach a: ",np.max(a,axis=1))
    print("Maksymalne liczby w kolumnach a: ",np.max(a, axis=0))
    print("Maksymalne liczby w wierszach b: ",np.max(b, axis=1))
    print("Maksymalne liczby w kolumnach b: ",np.max(b, axis=0))

def zad3():
    a = np.arange(3)
    b = np.arange(0, 9, 3)
    print(a,b)
    c = a@b
    print(c)

def zad4():
    a = np.array([5.4,3.5,3.2])
    b = np.array([4,3,2])
    print(a, b)
    c = a @ b
    print(c)

def zad5():
    b = np.array([random.randint(1,20) for _ in range(6)])
    b = b.reshape([2,3])
    a = np.sin(b)
    print(a)

def zad6():
    b = np.array([random.randint(1,20) for _ in range(6)])
    b = b.reshape([2, 3])
    a = np.cos(b)
    print(a)

def zad7():
    a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    b = np.array([[4,2,6],[7,3,5],[1,2,3]])
    print(a+b)

def zad8():
    a = np.arange(9).reshape([3,3])
    for i in a:
        print(i)

def zad9():
    a = np.arange(9).reshape([3, 3])
    for i in a.flat:
        print(i)

def zad10():
    a = np.arange(81).reshape([9, 9])
    print(a.reshape([3,27]))
    print(a.reshape([27, 3]))
    print(a.reshape([1, 81]))
    print(a.reshape([81, 1]))

def zad11():
    a = np.arange(12).reshape([3,4])
    b = a.reshape([4,3])
    c = a.reshape([2,6])
    print(np.array([i for i in a.flat]))
    print(np.array([i for i in b.flat]))
    print(np.array([i for i in c.flat]))

def main():
    while True:
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
                case 8:
                    zad8()
                case 9:
                    zad9()
                case 10:
                    zad10()
                case 11:
                    zad11()
                case _:
                    print('Nie ma takiego zadania')
        elif wybor=="end":
            break
        else:
            print('To nie jest liczba naturalna')


if __name__ == "__main__":
    main()