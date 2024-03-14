from random import *
import math as m
def zad1():
    l = []
    while True:
        a = input("Podaj liczbe: ")
        if a.isdigit():
            l.append(a)
            print(l)
        elif a == 'end':
            break
        else:
            print('To nie jest liczba.')
    print(l)

def zad2():
    f = input("podaj funkcje (bez przerw) f(x) = ")
    def func(f):
        fu = f.split('+')
        a = int(fu[0].rstrip('x'))
        if a>0:
            print('F rosnaca')
        elif a<0:
            print('f malejaca')
        elif a==0:
            print('f stala')
    func(f)

def zad3():
    a1=4
    a2=-1/4
    b1=2
    b2=0
    def rownolegle(a1, a2):
        if a1==a2:
            print('rownolegle')
        elif a1*a2==-1:
            print('prostopadle')
        else:
            print('dowolne')
    rownolegle(a1, a2)

def zad4():
    def pitagoras(a=1, b=1):
        print(m.sqrt(a**2+b**2))
    pitagoras(3,4)
    pitagoras(3)
    pitagoras()

def zad5():
    def sumOfAn(a1=1,r=1,ile=10):
        for i in range(ile):
            a1+=r
        return a1
    print(sumOfAn(3,5, 15))
    print(sumOfAn())

def zad6():
    def dodaj_znak(l: list):
        for i in range(len(l)):
            l[i] = l[i].replace(l[i], l[i]+'!')
        return l
    def dodaj_znakv2(l: list):
        lista = []
        for i in l:
            lista.append(i+'!')
        return lista
    print(dodaj_znak(['adaf','dd','fg']))
    print(dodaj_znakv2(['adaf', 'dd', 'fg']))

def zad7():
    def guess_the_number():
        score = 0
        for i in range(5):
            number = m.floor(random()*10)
            quess = int(input("Podaj liczbe:"))
            if number==quess:
                print(f'Wylosowana liczba to {number}. Zdobywasz 10 punktow')
                score+=10
            else:
                print(f'Wylosowana liczba to {number}. Tracisz punkt')
                score-=1
        print(f'Koniec gry. Twoja punktacja to {score} punktow')
    guess_the_number()

def zad8():
    def digital_root(n):
        while len(str(n))!=1:
            suma = 0
            for i in str(n):
                suma+=int(i)
            n=suma
        return n
    n = int(input("Podaj liczbe"))
    print(digital_root(n))

def zad9():
    def multipli_game():
        good_answer = 0
        bad_answer = 0
        for i in range(1,11):
            a = randrange(1,10)
            b = randrange(1, 10)
            print(f"Pytanie {i}. {a}*{b}= ")
            answer = int(input())
            if a*b==answer:
                print('Poprawna odpowiedz')
                good_answer+=1
            else:
                print(f'Błędna odpowiedź, poprawną odpowiedzią jest {a*b}')
                bad_answer+=1
        print('Koniec gry!')
        print(f'Błędne odpowiedzi: {bad_answer}')
        print(f'Poprawne odpowiedzi: {good_answer}')
    multipli_game()

def zad10():
    n = int(input('Podaj liczbe'))
    for i in range(n):
        if i==0:
            print(" " * n + "*")
        elif i == n//2 and n%2==0:
            print(" "*(n-i) + '*'*(n+1))
        elif i==n//2 and n%2==1:
            print(" " * (n - i) + '*' * n)
        else:
            print(" "*(n-i) + '*' + ' '*(i+(i-1)) + '*')

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
            case 8:
                zad8()
            case 9:
                zad9()
            case 10:
                zad10()
            case _:
                print('Nie ma takiego zadania')
    else:
        print('To nie jest liczba naturalna')

if __name__ =="__main__":
    main()