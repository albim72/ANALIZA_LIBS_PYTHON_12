#przykład 1
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
