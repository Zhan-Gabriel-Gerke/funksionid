from module1 import *
while True:
    print("funksioind".center(50,"+"))
    v=input("arithmetic- A, \nis_year_leap- B, \nsquare- C, \nseason- D \nBank-E, \nkodeeriumine_de-X, \nDate-H, \nPrime-K ")
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
        kv=int(input("Sisestage ruudu külg: "))
        result=square(kv)
        print(result)
    elif v.upper()=="D":
        a=int(input("Sisestage kuu"))
        result=Aastajad(a)
        print(result)
    elif v.upper()=="E":
        a=float(input("money: "))
        b=int(input("aasta"))
        result=bank(a,b)
        print(result)
    elif v.upper()=="X":
        print("kodeeriumine".center(60,"*"))
        rezult=xor_cipher(input("siseta text"), input("sisesta võti :"))
        print(rezult)
        print("Dekoderiumine". center(60,"*"))
        de_rezult=xor_uncipher(rezult, input("sisesta võti:"))
        print(de_rezult)
    elif v.upper()=="H":
        a=int(input("Sisestage päev: "))
        b=int(input("Sisestage kuu: "))
        c=int(input("Sisestage aasta: "))
        result=date(a,b,c)
        print(result)
    elif v.upper()=="K":
        a=int(input("Sisestage number: "))
        result=is_prime(a)
        print(result)