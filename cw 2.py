import sys
def zad1():
    zdanie = input()
    c = 0
    for i in zdanie.split():
        c+=1
    print(c)

def zad2():
    a, b, c = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
    sys.stdout.write(str(a**b+c))

def zad3():
    napis = input(f'Podaj napis')
    print(f'Napis jest palindromem = {napis==napis[::-1]}')

def zad4():
    a = int(input('Podaj liczbe'))
    for i in range(2,a):
        if a%i == 0:
            lp = False
            print(f'{a} nie jest liczba pierwsza')
            break
        lp = True
    if lp == True:
        print(f'{a} jest liczba pierwsza')

def zad5():
    n = 1000
    doskonale = []
    for i in range(1, n):
        c = 0
        for j in range(1, i):
            if i%j==0:
                c+=j
        if i==c:
            doskonale.append(i)
    print(doskonale)

def zad6():
    lista = [5, 2, 5.34, 6]
    for i in range(len(lista)):
        lista[i]=lista[i]**2
    print(lista)

def zad7():
    lista = []
    while len(lista)<10:
        n = float(input(f'Podaj {len(lista)+1} liczbe'))
        if n%2==0:
            lista.append(n)
        else:
            print('To nie jest l parzysta')
    print(lista)

def zad8():
    l = [-2, 4, 6, 'eje', 'ala', 'ala', 6]
    dir = dict()
    for i in l:
        if i not in dir.keys():
            dir[i] = 1
        else:
            dir[i]+= 1
    print(dir)
    dir1 = {}
    for i in dir:
        if str(i).strip('-').isnumeric():
            dir1[i]=dir[i]
    dir = dir1
    print(dir)
def main():
    #zad1()
    #zad2()
    #zad3()
    #zad4()
    #zad5()
    #zad6()
    #zad7()
    zad8()


if __name__ == '__main__':
    main()