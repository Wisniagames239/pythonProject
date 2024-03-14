import math
from random import *
def zad1():
    print(round(math.pow((math.e**4-math.log2(34)),1/3),2))
    print(round(math.pow((math.exp(20) + math.cos(45) + math.e), 1 / 3), 2))
    print(round(math.pow((math.log(20,3) + math.sin(45)*5/8), 1 / 4), 2))
    print(round((math.log(23,3)+ (math.sin(34)+5)**(1/3)), 2))
    print(round(math.pow((math.log2(32) + math.pi + math.sin(56)), 1 / 4), 2))

def zad2():
    n = int(input('Podaj liczbe: '))
    if n in range(1,11):
        for i in range(1,n+1):
            print('A'*i)
    else:
        print('Liczba nie jest w zbiorze [1,10]')

def zad3():
    n = int(input('Podaj liczbe: '))
    if n in range(1,11):
        for i in range(1,n+1):
            if (n-i)/2 == 0:
                print(' ' * ((n-i)//2)*2,' A'*i)
            else:
                print(' ' * (((n - i)*2 // 2)), ' A' * i)
    else:
        print('Liczba nie jest w zbiorze [1,10]')

def zad5():
    n = int(input("podaj n"))
    def func(n):
        l = []
        for i in range(n):
            lp = []
            for j in range(n):
                lp.append(round(random()*10,4))
            l.append(lp)
        print(l)
        print('')
        return [sum(i) for i in l]
    print(func(n))







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
            case 5:
                zad5()
            case _:
                print('Nie ma takiego zadania')
    else:
        print('To nie jest liczba naturalna')

if __name__ =="__main__":
    main()
