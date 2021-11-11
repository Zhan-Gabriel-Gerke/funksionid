from module1 import *
while True:
    print("funksioind".center(50,"+"))
    v=input("arithmetic- A, \nis_year_leap- B, \nsquare- C, \nseason- D \nBank-E")
    if v.upper()=="A":
        a=float(input("esimene arv"))
        b=float(input("teine arv"))
        sym=input("Tehe:")
        rezult=arithmetic(a,b,sym)
        print(rezult)
    elif v.upper()=="B":
        year=int(input("sisesta aasta"))
        rezolut=is_year_leap(year)
        print(rezolut)
    elif v.upper()=="C":
        kv=int(input("Sisesta ruudi külg:"))
        resul=square(kv)
        print(result)
    elif v.upper()=="D":
        a=int(input("Sisestage kuu"))
        result=Aastajad(a)
        print(result)
    elif v.upper()=="E":
        a=int(input("sisesta aasta"))
        b=int(input("sisesta money"))
        result=Bank(a,b)
        print(result)