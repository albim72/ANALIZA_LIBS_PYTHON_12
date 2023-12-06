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
