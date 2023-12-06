# import dane
# import dane as dn
from dane import nb as filia
from dane import book as bk
from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.cklasa import CDane

print("_________________ czytanie bezpośrednie _________________")
print(filia)
print(bk)
print("_________________ czytanie za pomocą funkcji _________________")
czytaj_liste(filia)
czytaj_slownik(bk)
print("_________________ czytanie za pomocą obiektu _________________")
cd = CDane(filia,bk)
cd.czytajl()
cd.czystajs()
