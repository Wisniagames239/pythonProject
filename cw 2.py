import sys


def zad1():
    zdanie = input()
    i = 0
    while i < len(zdanie.split()):
        i += 1
    print(i)


def zad2():
    a, b, c = int(sys.stdin.readline()), int(sys.stdin.readline()), int(sys.stdin.readline())
    sys.stdout.write(str(a**b+c))


def zad3():
    napis = input(f'Podaj napis')
    print(f'Napis jest palindromem = {napis == napis[::-1]}')


def zad4():
    a = int(input('Podaj liczbe'))
    lp = True
    for i in range(2, a):
        if a % i == 0:
            lp = False
            print(f'{a} nie jest liczba pierwsza')
            break
        lp = True
    if lp:
        print(f'{a} jest liczba pierwsza')


def zad5():
    n = 1000
    doskonale = []
    for i in range(1, n):
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += j
        if i == c:
            doskonale.append(i)
    print(doskonale)


def zad6():
    lista = [5, 2, 5.34, 6]
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    print(lista)


def zad7():
    lista = []
    while len(lista) < 10:
        n = float(input(f'Podaj {len(lista)+1} liczbe'))
        if n % 2 == 0:
            lista.append(n)
        else:
            print('To nie jest l parzysta')
    print(lista)


def zad8():
    lis = [-2, 4, 6, 'eje', 'ala', 'ala', 6]
    dirk = dict()
    for i in lis:
        if i not in dirk.keys():
            dirk[i] = 1
        else:
            dirk[i] += 1
    print(dirk)
    dirk1 = {}
    for i in dirk:
        if str(i).strip('-').isnumeric():
            dirk1[i] = dirk[i]

    dirk = dirk1
    print(dirk)


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
            case _:
                print('Nie ma takiego zadania')
    else:
        print('To nie jest liczba naturalna')


if __name__ == '__main__':
    main()
