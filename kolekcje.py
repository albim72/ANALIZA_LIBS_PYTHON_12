print("kolekcje języka Python")

a:int = 700
print(a)
print(type(a))

a = "siedemset"
print(a)
print(type(a))

#lista
cyfry = [2,7,4,2,1,3,8,9,6,4,5,3,2,1,4,6,7,8,9,3,0,4,2]
print(cyfry)
print(cyfry[0])
print(cyfry[3])
print(cyfry[4:7])
print(cyfry[5:])
print(cyfry[:7])
print(cyfry[-1])
print(cyfry[-2])
print(cyfry[2:10:2])

s = "lajkonik"

print(s)
print(s[0])
print(s[2:5])

print(s[::-1])

pparzyste = cyfry[::2]
print(pparzyste)

pnparzyste = cyfry[1::2]
print(pnparzyste)

cyfry.append(9)
print(cyfry)

cyfry.insert(3,1)
print(cyfry)

# cyfry.append([5,4,2,2])
# print(cyfry)

cyfry = cyfry + [5,4,2,2]
print(cyfry)

cyfry.extend([4,5,3,5,2,0])
print(cyfry)

cyfry.remove(2)
print(cyfry)


#krotka

miasta = ("Kraków","Lublin","Warszawa","Kraków","Lublin")
print(miasta)
print(type(miasta))

print(miasta[2:4])
print(miasta.count("Kraków"))
