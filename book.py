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
    

bk1 = Book(25,"Poradnik początkującego biegacza","Michał Stec")
    
