"""
Bir değişken oluşturduğunda:

- Python önce değeri (nesneyi) bellekte oluşturur

- Sonra değişken ismini bu nesneye "yapıştırır"

---
x = 42

Python bellekte 42 değerini taşıyan bir int nesnesi oluşturur

x ismini bu nesneye bağlar (etiketler)

---
x = 42
y = x

x de — y de aynı 42 nesnesine yapıştırılan bir etikettir. İki etiket, bir nesne.

---
x = 42
y = x
print(x is y)  # True — aynı nesne!

x = 99
print(y)  # 42 — y hâlâ eski nesneye bağlı

x = 99 dediğinde x etiketi eski nesneden koparılıp yeni 99 nesnesine yapıştırılır. y hâlâ 42'ye bağlı kalır. Etiketler bağımsızdır.
"""

### Çoklu Atama - Tek satırda birden fazla değişken atama.

x, y, z = 1, "2", 3.0

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Aynı Değeri Birden Fazla Değişkene Atama
x = y = z = 4 # x, y, z = 4, 4, 4
print(x, y, z)

#################################################

import keyword
print("Kullanabileceğimiz Fonksiyonlar (keyword) :\n", dir(keyword), sep="", end="\n\n")

a = keyword.kwlist
print("Tanımlayamayacağımız Değişken İsimleri :\n", a, sep="")
print("-" * 45)
print("Yasaklı Kelime Adedi :", len(a))

###
import keyword

liste = keyword.kwlist
for i,eleman in enumerate(liste,1):
    print(f"{i}:{eleman}")

#################################################

isletme = "Sefa Bilişim"
gun = 20
gidis_ucreti = 1.5
donus_ucreti = 1.4

masraf = gun * (gidis_ucreti + donus_ucreti)

print("-" * 31)
print("=== " + isletme + " ===")
print("-" * 31)
print("Çalışılan Gün Sayısı\t: ", gun)
print("İşe Gidiş Ücreti\t: ", gidis_ucreti)
print("İşten Dönüş Ücreti\t: ", donus_ucreti)
print("-" * 31)
print("Aylık Yol Masrafı\t: ", masraf)
print("-" * 31, end="\n\n")

################################################

cap = 16
yari_cap = cap / 2
pi = 3.14159

alan = pi * yari_cap * yari_cap
cevre = 2 * pi * yari_cap

print("Yarıçapı " + str(int(yari_cap)) + " Olan Dairenin Alanı : " + str(alan))
print("Yarıçapı", int(yari_cap) ,"Olan Dairenin Çevresi :", cevre)

################################################

ocak = mart = mayis = temmuz = agustos = ekim = aralik = 31
nisan = haziran = eylul = kasim = 30
subat = 28
mart_aylik_sarfiyat = 346
mart_fatura_tutari = 273.87

birim_fiyat = mart_fatura_tutari / mart_aylik_sarfiyat
gunluk_sarfiyat = mart_aylik_sarfiyat / mart
nisan_fatura = nisan * gunluk_sarfiyat * birim_fiyat

print("Nisan Ayı Faturası : ", nisan_fatura)

################################################

osman = "Araştırma Geliştirme Müdürü"
mehmet = "Proje Sorumlusu"

print("Osman :", osman)
print("Mehmet :", mehmet)

#Değisken değerlerini takas etme...
osman, mehmet = mehmet, osman
print("Osman :", osman)
print("Mehmet :", mehmet)

#################################################

# Bir listeden değişkenlere atama
koordinatlar = [41.01, 28.97]
print(koordinatlar, type(koordinatlar))  # [41.01, 28.97] <class 'list'>

enlem, boylam = koordinatlar
print(f"Enlem: {enlem} {type(enlem)}, Boylam: {boylam} {type(boylam)}")  # Enlem: 41.01 <class 'float'>, Boylam: 28.97 <class 'float'>


# Karakter dizisinden değişkenlere atama
koordinatlar = "41.01, 28.97"
print(koordinatlar, type(koordinatlar))  # 41.01, 28.97 <class 'str'>

enlem, boylam = koordinatlar.split(", ")
enlem = float(enlem)
boylam = float(boylam)
print(f"Enlem: {enlem} {type(enlem)}, Boylam: {boylam} {type(boylam)}")  # Enlem: 41.01 <class 'float'>, Boylam: 28.97 <class 'float'>


# Fonksiyon dönüş değerleriyle
def bolme_islemi(a, b):
    bolum = a // b
    kalan = a % b
    return bolum, kalan

sonuc, kalan = bolme_islemi(17, 5)
print(sonuc, type(sonuc))  # 3 <class 'int'>
print(kalan, type(kalan))  # 2 <class 'int'>
print(f"17 / 5 = {sonuc}, kalan {kalan}")  # 17 / 5 = 3, kalan 2

##################################################

# İlk ve son elemanı ayır, gerisini topla
ilk, *orta, son = [1, 2, 3, 4, 5]
print(ilk)   # 1
print(orta)  # [2, 3, 4]
print(son)   # 5

###################################################

### type() karşılaştırma
x = "42"
if type(x) == int:
    print("Bu bir tam sayı")

# isinstance() kullanımı:
if isinstance(x, int):
    print("Bu bir tam sayı (veya int'in alt sınıfı)")

print(type(True) == int)        # False
print(isinstance(True, int))    # True — bool, int'in alt sınıfı


### type() ile Dinamik Kontrol
def akilli_toplama(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + " " + b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return str(a) + str(b)

print(akilli_toplama(3, 5))           # 8
print(akilli_toplama("Merhaba", "Dünya"))  # Merhaba Dünya
print(akilli_toplama("Skor: ", 100))   # Skor:100

#################################################
"""
Değişken Türlerini Kontrol Etme
Python dinamik tipli bir dildir. Bir değişkenin tipi çalışma zamanında belirlenir ve istediğin zaman değişebilir.
"""
x = 42          # int
x = "merhaba"   # str — aynı değişken, farklı tip
x = [1, 2, 3]   # list — yine değişti
# Bu esneklik güçlü ama tehlikeli de olabilir. Python 3.5+ ile type hints (tip ipuçları) geldi:

# Tip ipuçları — zorunlu değil ama okunabilirliği artırır
isim: str = "Ali"
yas: int = 25
fiyat: float = 99.90
aktif: bool = True
"""
Tip ipuçları Python tarafından zorlanmaz — sadece dokümantasyon ve araç desteği içindir. Ama büyük projelerde okunabilirliği dramatik şekilde artırır.
"""
def selamla(isim: str, resmi: bool = False) -> str:
    if resmi:
        return f"Sayın {isim}, hoş geldiniz."
    return f"Selam {isim}!"

sonuc = selamla("Ali")
print(sonuc)  # Selam Ali!


#################################################

# Değişken Bilgilerini Görüntüleme

def degisken_bilgi(isim, deger):
    print(f"İsim:  {isim}")
    print(f"Değer: {deger}")
    print(f"Tip:   {type(deger).__name__}")
    print(f"ID:    {id(deger)}")
    print(f"Boyut: {deger.__sizeof__()} byte")
    print("-" * 30)

degisken_bilgi("sayi", 42)
degisken_bilgi("metin", "Python")
degisken_bilgi("liste", [1, 2, 3])
degisken_bilgi("bos", None)