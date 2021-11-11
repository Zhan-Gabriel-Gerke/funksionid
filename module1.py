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
    :rtype float:"""
    if a==12:
        print("Зима")
    elif 0<a<3:
        print("Зима")
    elif 2<a<6:
        print("Весна")
    elif 5<a<9:
        print("Лето")
    elif 8<a<12:
        print("Осень")
    else:
        print("Viga!")
    return("")
def Bank(a:int,b:int):
    """
    эта функция показывает сумму вклада
    """
    for x in range(b):
        c=a*1,1
        print(c("sinu money"))
        return()
        