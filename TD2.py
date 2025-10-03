class Personne :
    def __init__(self, nom,  age):
        self._nom = nom 
        self._age = age
    def se_presenter(self):
        return f"Bonjour, je m'appelle {self._nom} et j'ai {self._age} ans."
    def __str__(self):
        return f"Bonjour, je m'appelle {self._nom} et j'ai {self._age} ans."
    def __del__(self):
        print(f"L'objet {self._nom} est supprimé.")
class Etudiant(Personne):
    def __init__(self, nom, age, niveau):
        super().__init__(nom, age)
        self.niveau = niveau
    def etudier(self):
        return f"je suis  en {self.niveau} et j'etudie dur."
class Panier :
    def __init__(self, articles):
        self.articles = articles
    def __len__(self):
        return len(self.articles)
    def __getitem__(self, index):
        return self.articles[index]
class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
    def __eq__(self, value):
        if self.nom == value.nom and self.prix == value.prix:
            return True
        return False
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p1=Personne("Alice", 30)
print(p1.se_presenter())
print(p1)
e1=Etudiant("Bob", 20, "Licence")
print(e1.se_presenter())
print(e1.etudier())
p2=Panier(["pomme", "banane"])
print(len(p2))
print(p2[0])
prod1=Produit("Livre", 10.0)
prod2=Produit("Livre", 15.0)
print(prod1==prod2)
point1=Point(1, 2)
point2=Point(3, 4)
print(point1 + point2)
p3=Personne("Charlie", 25)
del p3
point3=Point(5, 6)
point4=Point(7, 8)
print(point3 + point4)