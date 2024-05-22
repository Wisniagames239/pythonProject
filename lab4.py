import numpy as np


#a = np.arange(2, dtype='int32')
#print(a.dtype)
#b = a.astype('float')
#print(b)
#print(b.dtype)
#print(b.shape)
#print(a.ndim)
#m = np.array([np.arange(2), np.arange(2)])
#print(m.shape)
#m1 = np.array([[5,3,4],[4,8,6]])
#print(m1)
#print(m1.shape)
#print(m1.ndim)
#
#zera = np.zeros((5,5), dtype=int)
#jedynki = np.ones((4,4))
#print(zera)
#print(jedynki)
#print(zera.dtype)
#print(jedynki.dtype)
#
#pusta = np.empty((2,2))
#print(pusta)
#poz_1 = pusta[1, 1]
#poz_2 = pusta[0, 1]
#print(poz_1)
#print(poz_2)
#
#liczby = np.arange(1,2,0.1)
#print(liczby)
#
#liczby_lin = np.linspace(1, 2, 5)
#print(liczby_lin)
#
#z = np.indices((5,3))
#print(z)

#x, y = np.mgrid[0:5, 0:5]
#print(x)
#print(y)
#
#mat_diag_k = np.diag([a for a in range(5)], k=-1)
#print(mat_diag_k)
#
#z = np.fromiter(range(5), dtype='int32')
#print(z)

#znaki = b'abcdef'
#zn1 = np.frombuffer(znaki, dtype='S1')
#print(zn1)
#zn2 = np.frombuffer(znaki, dtype='S2')
#print(zn2)

#znaki= 'abcdef'
#zn3 = np.array(list(znaki))
#zn4 = np.array(list(znaki), dtype='S1')
#zn5 = np.array(list(b'abcdef'))
#zn6 = np.fromiter(znaki, dtype='S1')
#zn7 = np.fromiter(znaki, dtype='U1')
#print(zn3)
#print(zn7)
#print(zn7)
#print(zn7)
#print(zn7)
#
#mat = np.ones((2,2))
#mat_1 = np.ones((2,2))
#mat = mat+mat_1
#print(mat)
#print(mat-mat_1)
#mat_1 = np.array([[4,6],[7,5]])
#print(mat*mat_1)
#print(mat/mat_1)

#a = np.arange(10)
#print(a)
#s = slice(2,7,2)
#print(a[s])
#s = range(2,7,2)
#print(a[s])
#print(a[2:7:2])
#print(a[1:])
#print(a[2:5])
#print('')
#mat = np.arange(25)
#mat = mat.reshape((5, 5))
#print(mat[1:])
#print(mat[:,1])
#print(mat[:, -1:])
#print(mat[2:6, 1:3])
#print(mat[:, range(2,6,2)])
#print('')

#x=np.array([[0,1,2],
#            [3,4,5],
#            [6,7,8],
#            [9,10,11]])
#print(x)
#rows = np.array([[0, 0], [3, 3]])
#cols = np.array([[0, 2], [0, 2]])
#y = x[rows, cols]
#print(y)
#print(rows)
#print(cols)
def zad1():
    numpy = np.arange(3, 3*15+1,3)
    print(numpy)
def zad2():
    lista  = np.array([6.5,3.6,3.2,7.6])
    b = lista.astype('int64')
    print(b)

def zad3():
    def foo(n):
        numpy = np.arange(1, n**2+1)
        numpy = numpy.reshape([n, n])
        return numpy
    print(foo(5))

def zad4():
    def generuj(a, b):
        tab = np.logspace(1, b, num=b, base = a)
        return list(tab)
    print(generuj(2,4))

def zad5():
    def foo(n):
        w = np.arange(n, 0, -1)
        print(w)
        mac = np.diag(w)
        print(mac)
    foo(5)

def zad6():
    numpy = np.diag(np.fromiter('adzi', dtype='U1'))
    numpy[-1,:] = np.fromiter('adai', dtype='U1')
    numpy[:,0] = np.fromiter('adia', dtype='U1')
    print(numpy)

def zad7():
    def gener(n):
        mac = np.diag([2 for _ in range(n)])
        for i in range(2,n+1):
            mac+=np.diag([2*i for _ in range(n-i+1)],k=i-1)
            mac += np.diag([2 * i for _ in range(n - i+1)], k=-i+1)
        print(mac)
    gener(5)

def zad8():
    def foo(tab, kierunek):
        if kierunek=='poziomo' and tab.shape[0]%2==0:
            n = int(tab.shape[0])
            tab1 = tab[:int(n/2),:]
            tab2 = tab[int(n/2):,:]
            print(tab1)
            print(tab2)
        elif kierunek=='pionowo' and tab.shape[1]%2==0:
            n = int(tab.shape[1])
            tab1 = tab[:,:int(n / 2)]
            tab2 = tab[:,int(n / 2):]
            print(tab1)
            print(tab2)
        else:
            print("Nie mozna podzielic na 2")


    mac = np.array([[1,4,2],[5,2,6],[7,4,7],[1,2,3]])
    mac1 = np.array([[1, 4, 2,6], [5, 2, 6,6], [7, 4, 7,6]])
    foo(mac,'poziomo')
    print('')
    foo(mac1, 'pionowo')

def zad9():
    fibonacci = np.ones(25, dtype='int')
    for i in range(2,5**2):
        fibonacci[i] = fibonacci[i-1]+fibonacci[i-2]
    fibonacci = fibonacci.reshape([5,5])
    print(fibonacci)

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
                case _:
                    print('Nie ma takiego zadania')
        elif wybor=="end":
            break
        else:
            print('To nie jest liczba naturalna')


if __name__ == "__main__":
    main()