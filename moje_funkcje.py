#przykład 1
import math

n=100

def hx(k):
    return k**0.5 + k
def policz(a,b,c,y):
    global n
    # print(n)
    n=(a+b)*y-c+n+hx(b)
    return n

print(policz(56,3,7,88))
print(policz(5.07,13,4.5,-0.88))
print(n)

#przykład 2

def wx(a,d,b=1,c=8):
    return math.sqrt(a*b*c)+d

print(wx(5,7,9,4))
print(wx(5,7,4))
print(wx(5,5))
print(wx(3,7,c=51))

def rank(*lang,nrrank,**inne):
    print(f'ranking języków programowania nr {nrrank} -> miejsce pierwsze: {lang[0]}, '
          f'drugie: {lang[1]}, trzecie: {lang[2]}')

rank("Python","Java","C++","C#",nrrank=56)
rank("Python","Java","C","C++","JavaScript","C#",nrrank=58)


print((lambda g:g+11.5)(5))
print((lambda g,h:g+11.5-h)(5,3.2))

s = lambda a,b,z:(a*b+a*z)/(z-(a*b))

print(s(3.3,4,2.89))

def multi(n):
    return lambda a:a*n

print(multi(5)(9.9))

num = [56,7,8,-33,52,5,0,-9,-21,45,90,111,-90,8,1,3]
nbparz = list(filter(lambda x:x%2==0,num))
print(nbparz)

cube = list(map(lambda x:x**3,num))
print(cube)

def dodaj(x):
    return x+9
dziewiec = list(map(dodaj,num))
print(dziewiec)

#zbuduj listę która będzie skałdała się z wartości całkowitych z przedziału [1,100000], każda z wartości
#ma być kwadratem wartości z przedziału

kwadraty = [i**2 for i in range(1,100001)] #list comprehension
print(kwadraty)

def generuj_liste(pot,min,max):
    return [i**pot for i in range(min,max+1)]

pt = generuj_liste(5,109,88900)
print(pt)

pt = generuj_liste(2,1,99)
print(pt)

#funkcja wyższego rzędu

def witaj(imie):
    return f'Miło Cię widzieć: {imie}'
def konkurs(imie,punkty,zaliczono):
    return f'Uczestnik konkursu: {imie}, punkty: {punkty}, zaliczono: {zaliczono}'
def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Olga",56,"tak"))
