"""Fonksiyon = First-Class Object
Python'da fonksiyonlar birinci sınıf nesnelerdir (first-class objects). Bu ne demek? Fonksiyonları tıpkı sayılar, stringler veya listeler gibi kullanabilirsin:

1.Bir değişkene atayabilirsin

2.Başka bir fonksiyona parametre olarak geçebilirsin

3.Bir fonksiyondan return edebilirsin

4.Bir listeye veya dictionary'ye koyabilirsin."""
# 1.
def selamla(isim):
    return f"Merhaba, {isim}!"

# Fonksiyonu bir değişkene ata (parantez YOK!)
selam_fonksiyonu = selamla

# Artık her iki isimle de çağırabilirsin
print(selamla("Ali"))           # Merhaba, Ali!
print(selam_fonksiyonu("Ali"))  # Merhaba, Ali!

# Aynı fonksiyon nesnesi mi?
print(selamla is selam_fonksiyonu)  # True

# 2.
def uygula(fonksiyon, deger):
    """Verilen fonksiyonu verilen değere uygular."""
    return fonksiyon(deger)

def kare(x):
    return x ** 2

def kup(x):
    return x ** 3

print(uygula(kare, 5))   # 25
print(uygula(kup, 5))    # 125


# 3.
def topla(a, b):
    return a + b

def cikar(a, b):
    return a - b

def carp(a, b):
    return a * b

def bol(a, b):
    return a / b if b != 0 else "Sıfıra bölünemez!"

# Fonksiyonları bir dictionary'de tut
islemler = {
    "+": topla,
    "-": cikar,
    "*": carp,
    "/": bol
}

# Kullanıcıdan operatör al ve çalıştır
operator = "+"
sonuc = islemler[operator](10, 3)
print(f"10 {operator} 3 = {sonuc}")  # 10 + 3 = 13

# Tüm işlemleri dene
for op, fonk in islemler.items():
    print(f"10 {op} 3 = {fonk(10, 3)}")