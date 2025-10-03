class  Vehicule:
    def __init__(self ,marque , annee, kilometrage, numero_serie):
        self._marque=marque #PROTECTED
        self.__annee=annee #PRIVATE
        self.kilometrage=kilometrage #PUBLIC
        self.numero_serie=numero_serie
    #getters
    @property
    def annee(self):
        return self.__annee 
    #setters      
    @annee.setter
    def annee(self,nouvel_val):
        self.__annee=nouvel_val
    def __str__(self):
        return f"les information de vehicule sont: marque: {self._marque}, annee: {self.annee}, kilometrage: {self.kilometrage}, numero_serie: {self.numero_serie}"
class Voiture(Vehicule):
    def __init__(self,marque, annee,kilometrage, numero_serie, color,price):
        super().__init__(marque, annee, kilometrage, numero_serie)
        self.price=price
        self.color=color
    def __str__(self):
        return f"les informations de voiture sont: price: {self.price}, color: {self.color}"    

v=Vehicule("Toyota", 2023, 20000, "123ABC")
voiture=Voiture("Toyota", 2023, 20000, "123ABC","rouge",10000)
print(voiture.__class__)
print(voiture)
print(v)
print (v.__dict__)#afficher les informations de l'objet 
v.annee=20
print (v._marque)
print (v._Vehicule__annee)#pour acceder a un attribue private 
