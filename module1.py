from math import *
def arithmetic(a: float,b:float,c:str):
    """Lihtne kalkulaator
    +-liitmine
    --lahutamine
    *-korrutamine
    /-jagamine
    :param float a: Esimene arv
    :param float b: Teine arv
    :param str c: Arimeetiline tehing
    :rtype float:"""
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b
    elif c=="*":
        r=a*b
    elif c==":":
        if b!=0:
            r=a/b
        else:
            print("Div0")
            r=0.0
    else:
        print("viga")
    print(r)
    return r
def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigasta ja Flase kui ei ole 
    :parem int aasta: Aasata number 
    :rtype bool: Funksionid vastus loogilised formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus 
def square():
    """
    Она вычисляет переметр квадрата, площадь квадрата, диогональ квадрата
    """
    a=float(input("sisesta a"))
    p=a*4
    s=a**2
    f=a.sqrt+a.sqrt
    print("p",p)
    print("s",s)
    print("диагональ",f)
    return a
    return p
    return s
    return f
def Aastajad(a:int):
    """эта функция определяет время года по его месяцу
    :parem float a месяц
    :rtype str:"""
    if a==12 or 0<a<3:
        res="Зима"
    elif 0<a<3:
        res="Зима"
    elif 2<a<6:
        res="Весна"
    elif 5<a<9:
        res="Лето"
    elif 8<a<12:
        res="Осень"
    else:
        res="Viga!"
    return res
def Bank(a:int,b:int):
    """paneme raha bilanssi ja ootame mitu aastat
    :param float a: Esimene number
    :param float years: Teine number
    :rtüüp ujuk
    """
    for _ in range(a):
        a=((1.1*1/100)*a)*100
    print("sinu balance:",a)
    return("")
def xor_cipher(string:str, key:str)->str:
    """Tavaline sõna kodeeritakse
    :param str string: Esimene arv
    :param str key: Teine arv
    """
    result=""
    temp = int()
    for i in range(len(string)):
        temp = ord(string[i])#näitab sümboli kood
        for j in range(len(key)):
            temp ^=ord(key[j])
        result += chr(temp)
    return result 
def xor_uncipher(string:str, key: str)->str:
    """koderiumine text dekodeeritakse
    :param str string: Esimene arv
    :param str key: Teine arv
    """
    result = ""
    temp = []
    for i in range(len(string)):
        temp.append(string[i])
        for j in reversed(range(len(key))):
            temp[i] = chr(ord(key[j]) ^ ord(temp[i]))
        result += temp[i]
    return result
def date(a:int, b:int, c:int):
    """kuupäeva funktsioon võtab 3 argumenti päev, kuu ja aasta. Tagasta True, kui selline kuupäev on meie kalendris olemas, ja False muul juhul.
    :param int a: Esimene arv
    :param int b: Teine arv
    :param int c: Kolmas arv
    """
    set_b = {1: 31,2: 28, 3: 31,4: 30,5: 31,6: 30,7: 31,8: 31,9: 30,10: 31,11: 30,12: 31}
    if c>0 and (b>=1 and b<=12):
        if a in range(1, set_b[b]+1):
           return True
        else:
            return False
    else:
        return False
def is_prime(a:int):
    """kirjutad arvu vahemikus 0 kuni 1000 ja sulle antakse algarvu kas see on lihtne kui see on lihtne siis see on tõsi.
    :param int a:Esimene arv
    :rtype str
    """
    b=2
    while a%b!=0:
        b+=1
    return b==a
