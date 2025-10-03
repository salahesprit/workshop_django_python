liste=["Paris","Tunisie", "Maroc","Paris","Paris" , "Tunsie","Chine" ,"Canada"]
"""
set_liste=set(liste)
turple_liste=tuple(set_liste)
for i in turple_liste:
"""
res={}
for i in liste:
    if i in res:
        res[i]+=1
    else:
        res[i]=1
max=0
pays=""
for p,m in res.items():
    if m>max:
        max=m
        pays=p
print(f"{pays} est le pays le plus repété avec {max} fois.")