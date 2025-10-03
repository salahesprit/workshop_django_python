"""
nom=input("Entrez votre nom: ")
prenom=input("Entrez votre prénom: ")
age=int(input("Entrez votre âge: "))
print(f"hello {prenom} {nom}, you are {age} years old.")

num=int(input("Entrez un nombre entier: "))
if num%2==0:
    print(f"{num} est un nombre pair.")
else:
    print(f"{num} est un nombre impair.")

ch= input("Entrez une chaîne de caractères: ")
for i in ch:
    print(i)  
somme=0
for i in range(1,101):
    somme+=i
print(f"{somme}")

liste=[12, 15, 9, 18, 14]
print(max(liste))
print(min(liste))
avg=sum(liste)/len(liste)
print(f"{avg}")

student= {"name": "Ali", "age": 20, "study field":"computer science"}
student["email"]="ali@example.com"
print(student)
"""
ex_set= {"cat", "dog", "bird", "cat"}
print(ex_set)

truple= ("salah", 20, "rades")
for i in truple:
    print(i)