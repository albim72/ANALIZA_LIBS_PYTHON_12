# -*- coding: utf-8 -*-

# -- Sheet --

# To jest pierwszy notebook w temacie: <span style="color:red;font-size:16pt;font-weight:bold;">biblioteka Pandas</span>
# <p><img src="supernova.jpg" width=300></p>


import numpy as np

np.zeros(7)

print(np.ones(10))

np.empty(10)

u = np.arange(1,77,3)
u

zlista = [4,7,5,8,64,25,6,8,5,78,5545,6]
print(zlista)
print(type(zlista))

k=np.linspace(0,10,num=5)
k

mlista = np.array(zlista)
print(mlista)
print(type(mlista))

kl = (4,323,5,2,787,64,3)
knum = np.array(kl)
print(knum)
print(type(knum))

zl = {56,3,4,58,90,21,38,36,8,3,3}
znum = np.array(zl)
print(znum)
print(type(znum))

knum.sort()
print(knum)

# znum.sort()
# print(znum)

l1 = [2,4,6,9]
l2 = [5,6,78,9,13]
l3 = [112,89,12]

l1 = l1+l2+l3

l1

a = np.array(l1)
b = np.array(l2)
c = np.array(l3)

# a = a+b+c
a  = np.concatenate((a,b,c))
a

z1 = [[56,2],[64,2]]
z1

a1 = np.array([[2,9],[7,15]])
a1

z1[0][1]

a1[0][1]

a1[0,1]

x = np.array([[3,4],[6,8]])
y = np.array([[7,11],[19,3]])

p = np.concatenate((x,y),axis=1)
p

prosta = np.arange(12)
prosta

fp = prosta.reshape(3,4)
fp

mac1 = np.array([[2,3],[4,5],[9,9]])

mac1

mac1.shape

w1 = mac1.reshape(6)
w1

ar = np.array([1,6,78,9,1,4,21,24,12,1,1,3,-3])
ar.shape

ar[:7]

ar[2:5]

w = np.array([[1,2,3,4],[9,10,11,12],[35,36,21,99]])
w

w[w<5]

pc = (w>5)
w[pc]

pv = (w%2==0)
w[pv]

cv = w[(w>2)&(w<21)]
cv

sv = w[(w<8)|(w>50)]
sv

