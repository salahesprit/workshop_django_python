nom_prenom = "John Doe"
age = 30
print(type(nom_prenom))
print(type(age))
if age <10:
    print("Vous êtes enfant.")
elif 10<age<=18:
    print("Vous êtes adolescent.")
else:
    print("Vous êtes adulte.")
entier =12
boolean =3>5
chaine = "Bonjour"
float_number = 3.14
complexe =2+3j
print(type(boolean))
liste =[1,2,3]
liste =[1,"deux",3.0,[4,5]]
dictionnaire ={"nom": "Alice", "age": 25}
exp_tuple =(1, "deux", 3.0)
ex_set ={1,2, 2, 3, 4, 4, 5}
print(type(ex_set))
var={}
print(type(var))

a=5
b=2
print(a+b)
print(a**b)
chaine1="Bonjour "
chaine2=" le monde!"
concat =chaine1 + chaine2
res= len (concat)
sous_chaine =concat[0:3]

print(concat)
print(sous_chaine)
print(res)
c=0
while c<5:
    print(c)
    if c>3:
        break
    c+=1
def somme(a,b):
    return a+b
print (somme(3,4))
print (somme("bonjour ","le monde!"))
nom=input("Entrez votre nom: ")
age=int(input("Entrez votre âge: "))
print(f"Bonjour {nom}, vous avez {age} ans.")

try :
    nombre=int(input("Entrez un nombre entier: "))
    res=nombre/5
    print(res)
except ValueError:
    print("Ce n'est pas un nombre entier valide.")
except ZeroDivisionError:
    print("Division par zéro impossible.")

    nom=input("Entrez votre nom: ")
    prenom=input("Entrez votre prénom: ")
    age=int(input("Entrez votre âge: "))
    print(f"hello {prenom} {nom}, you are {age} years old.")