class Book:
    #definicja stanu - konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = "miękka"
        self.create_book()

    #zachowanie -> funkcje klasy(metody)

    def create_book(self):
        print("Utworzono obiekt klasy: Book! (nową książkę)")

    def print_book(self):
        print(f"książka: {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return self.cena*procent/100

    def getcena(self):
        return self.cena

    def setcena(self,nowacena):
        self.cena = nowacena

    @property
    def oprawa(self):
        return self._oprawa

    @oprawa.setter
    def oprawa(self,innaoprawa):
        self._oprawa = innaoprawa


bk1 = Book(25,"Poradnik początkującego biegacza","Michał Stec")
bk1.print_book()
print(f'rabat od ceny {bk1.getcena()} zł wynosi: {bk1.rabat(7.5):.2f} zł')
print("zmiana ceny książki nr 25")
bk1.setcena(41)
print("zmiana rodzaju oprawy")
bk1.oprawa = "twarda"
print(f"następiła zmiana oprawy ze standardowej na {bk1.oprawa}")
bk1.print_book()
print("_"*50)
bk2 = Book(67,"ABC Kulturysty","Mariusz Pudzianowski",45)
bk2.oprawa = "obwoluta"
bk2.print_book()
print(f'rabat od ceny {bk2.getcena()} zł wynosi: {bk2.rabat(11):.2f} zł')

"""
utworzenie klasy Encyklopedia z dziedziczeniem klasy Book
"""

class Empty:
    pass

class Encyklopedia(Book,Empty):

    def __init__(self, id, tytul, autor, rodzaj, wydawca, cena=30):
        super().__init__(id, tytul, autor, cena)
        self.rodzaj = rodzaj
        self.wydawca = wydawca

print("*"*50)
ec1 = Encyklopedia(56,"Encyklopedia informatyki","Jan Kot","techniczna","ABC",160)
ec1.oprawa = "tekturowa"
ec1.print_book()
print(f'rabat od ceny {ec1.getcena()} zł wynosi: {ec1.rabat(5):.2f} zł')
