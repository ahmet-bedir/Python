########################
# 1.Aritmetik İşleçler #
# +   toplama          #
# -   çıkarma          #
# *   çarpma           #
# /   bölme            #
# **  kuvvet alma      #
# %   modülüs          #
# //  taban bölme      #
########################

print('#' * 45)
print(2.3 + 3.2)
print(9.3 - 1.2)
print(2.63 * 2.8)
print(8.4 / 2.2)
print(2 ** 3)  # 8
print(4 ** 0.5) #bir sayının 0.5'inci kuvveti, o sayının kareköküdür.
print("Python" + "Programlama") #buradaki + işleci toplama yerine string değerleri birleştirme işlemi yapıyor. 
print(4 % 3)  # 1 (kalanı verir)
print(9 // 2)  # 4 (tam bölme işlemi yapar)
print('#' * 45)  # buradaki * işleci çarpma yerine string değeri verilen sayı kadar tekrarlama işlemi yapıyor. 

### Çift/tek kontrolü
for i in range(1, 11):
    durum = "Çift" if i % 2 == 0 else "Tek"
    print(f"{i:2d} → {durum}")

##############
### Tekli (Unary) Operatörler
x = 5
print(+x)   # 5 (pozitif — genellikle bir etkisi yok)
print(-x)   # -5 (negatif)

y = -3
print(-y)   # 3 (negatifin negatifi)

#############################
# 2.Karşılaştırma İşleçleri #
# ==    eşittir             #
# !=    eşit değildir       #
# >     büyüktür            #
# <     küçüktür            #
# >=    büyük veva eşittir  #
# <=    küçük veya eşittir  #
#############################

x, y = 10, 20

print(f"{x} == {y}: {x == y}")   # False
print(f"{x} != {y}: {x != y}")   # True
print(f"{x} <  {y}: {x < y}")    # True
print(f"{x} >  {y}: {x > y}")    # False
print(f"{x} <= {y}: {x <= y}")   # True
print(f"{x} >= {y}: {x >= y}")   # False

# Farklı Tiplerde Karşılaştırma
# int ve float karşılaştırılabilir
print(1 == 1.0)      # True
print(1 < 1.5)        # True

# bool ve int
print(True == 1)       # True (bool int'in alt sınıfı)
print(False == 0)      # True

# String karşılaştırma (leksikografik — Unicode sırasına göre)
print("apple" < "banana")   # True
print("abc" == "abc")        # True
print("A" < "a")             # True (A=65, a=97)

# String'lerde büyüklük karşılaştırması karakter karakter yapılır
print("abc" < "abd")    # True (3. karakter: c < d)
print("abc" < "abcd")   # True (eşit başlangıç, kısa olan küçük)

### Zincirleme karşılaştırma — daha  okunaklı
x = 15

print(10 < x < 20)     # True (x, 10 ile 20 arasında mı?)
print(1 <= x <= 100)    # True
print(20 < x < 30)      # False

# Diğer dillerde böyle yazmak gerekir:
print(10 < x and x < 20)  # True — aynı şey ama daha uzun

# Üçlü zincir
a, b, c = 1, 2, 3
print(a < b < c)        # True
print(a < b > c)        # False

# Eşitlik zinciri
print(1 == 1 == 1)      # True
print(1 == 1 == 2)      # False

###
parola = "123"
giris = input("Parolayı Giriniz : ")

if parola == giris:
    print("Girilen Parola Doğru!")
elif parola != giris:
    print("Girilen Parola Yanlış!")

###
sayi = input("sayı giriniz : ")

if int(sayi) <= 100:
    print("sayı 100 veya 100'den küçük")
elif int(sayi) >= 100:
    print("sayı 100 veya 100'den büyük")
    
print('#' * 45)

########################
### 3.Bool İşleçleri ###
### and    ve        ###
### or     veya      ###
### not    değil     ###
########################

# 1- And (Her İkisi de True)
# True, True => True
# True, False => False
# False, False => False

# 2- Or (En Az Biri True)
# True, True => True
# True, False => True
# False, False => False

# 3- Not (Tersine Çevir)
# False => True
# True => False

print(1==1) #True
print(1!=1) #False

print("and :", 'a'=='a' and 5==5) #True
print("and :", 'a'=='a' and 5==-6) #False

print("or :", 'a'=='a' or 45==5) #True
print("or :", 'a'=='ab' or 5==-6) #False

print("not :", not 5==5) #False
print("not :", not 5!=5) #True

print(bool(3))  # True
print(bool("py"))  # True
print(bool(" "))  # True
print(bool("    "))  # True
print(bool("0"))  # True (0 bir sayı, “0”’ın ise bir karakter dizisidir. Sayı olan 0’ın bool değeri False’tur, ama karakter dizisi olan “0”’ın bool değeri True’dur)
print(bool(0))  # False
print(bool(""))  # False


parola = ""
print(bool(parola))  # False
print(not parola)  # True

parola = "123"
print(bool(parola))  # True
print(not parola)  # False

aktif = False
if not aktif:
    print("Hesap pasif")

############
### Short-Circuit (Kısa Devre)
# and: İlk False'ta durur (sonuç: False)
x = 0
if x != 0 and 10 / x > 2:  # 10/0 hatası oluşmaz!
    print("OK")

# or: İlk True'da durur (sonuç : True)
isim = "" or "Anonim"  # "Anonim"
print(isim)

# and ve or aslında operandlardan birini döner
print(1 and 2 and 3)        # 3 (hepsi truthy → son değer)
print(1 and 0 and 3)        # 0 (ilk falsy)
print(0 or "" or "hello")   # "hello" (ilk truthy)
print(0 or "" or [])         # [] (hepsi falsy → son değer)

# Varsayılan Değer Deseni
kullanici_adi = input("Kullanıcı adı: ") or "misafir"
print(kullanici_adi)  # Kullanıcı ismini girerse ismi, enter ile boş değer girerse "misafir" değeri görünecektir.

print('#' * 45)

###########################
# 4.Değer Atama İşleçleri #
# =     atama işleci      #
# +=    topla ata         #
# -=    çıkar ata         #
# *=    çarp ata          #
# /=    böl ata           #
# %=    modülüs ata       #
# **=   kuvvet ata        #
# //=   taban böl ata     #
# :=    walrus operatörü  #
###########################

a = 13

a += 5  # 18 (a = a + 5 işlemiyle aynı işi yapar)
a -= 5  # 13
a *= 2  # 26 (a = a * 2)
a /= 2  # 13
a %= 5  # 3 (a = a % 5)
a **= 2  # 9
a //= 2  # 4 (a = a // 2)
print(a)  # 4

# String'lerle de çalışır
mesaj = "Merhaba"
mesaj += " Dünya"
print(mesaj)  # Merhaba Dünya

# Listelerle
liste = [1, 2]
liste += [3, 4]    # liste.extend([3, 4]) ile aynı
print(liste)  # [1, 2, 3, 4]

# *= ile tekrarlama
cizgi = "-"
cizgi *= 40
print(cizgi)  # ----------------------------------------

### Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?
a, b, c = 4, 8, (12, 2)

sayi1 = int(input("sayı 1: "))
sayi2 = int(input("sayı 2: "))

carpim = sayi1 * sayi2
toplam = a + b + (c[0] + c[1])

sonuc = carpim - toplam

# Walrus Operatörü (:=) ifadeyi değerlendirirken aynı anda değişkene atama yapar.
# Walrus olmadan
n = len("merhaba")
if n > 5:
    print(f"Uzun string: {n} karakter")

# Walrus ile — atama ve kontrol tek satırda
if (n := len("merhaba")) > 5:
    print(f"Uzun string: {n} karakter")

# walrus olmadan
giris = len(input("Adın ne? "))
if giris < 4:
    print("Adın kısaymış.")
elif giris < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")
    
# walrus operatörü ile
if (giris := len(input("Adın ne? "))) < 4:
    print("Adın kısaymış.")
elif giris < 6:
    print("Adın biraz uzunmuş.")
else:
    print("Çok uzun bir adın var.")


# Walrus olmadan
satir = input("Giriş (q=çıkış): ")
while satir != "q":
    print(f"Yazdığınız: {satir}")
    satir = input("Giriş (q=çıkış): ")

# Walrus ile — daha temiz
while (satir := input("Giriş (q=çıkış): ")) != "q":
    print(f"Yazdığınız: {satir}")

################################
# 5.Bitwise (Bitsel) İşleçleri #
# &     Mantıksal And          #
# |     Mantıksal Or           #
# ^     Mantıksal XOR          #
# >>    Kaydırma               #
# <<    Kaydırma               #
# ~     Tümleme                #
################################
'''
And işlemi ile karşılaştırılmış iki bitten biri bile 0 olsa; 0 sonucunu alırsınız. 1 sonucu alabilmek için her iki bitin de 1 olması gerek.
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0
'''
a = 10                   # 0000 1010 = 10
b = 20                   # 0001 0100 = 20
print("AND :", a & b)    # 0000 0000 = 0

print("AND :", 15 & 11)  # 0000 1111 = 15
                         # 0000 1011 = 11
                         # 0000 1011 = 11
'''
Or işlemi ile karşılaştırılmış iki bitten sadece biri bile 1 olsa; 1 sonucunu alırsınız. 0 sonucu alabilmek için her iki bitin de 0 olması gerek.
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0
'''
a = 10                  # 0000 1010 = 10
b = 20                  # 0001 0100 = 20
print("OR :", a | b)    # 0001 1110 = 30

print("OR :", 15 | 11)  # 0000 1111 = 15
                        # 0000 1011 = 11
                        # 0000 1111 = 15
'''
XOR (ya da) ile karşılaştırma işleminin 1 (doğru) olabilmesi için önermelerin birbirinden farklı doğruluk değerlerine sahip olması gerekmektedir.
1 ^ 1 = 0
1 ^ 0 = 1
0 ^ 1 = 1
0 ^ 0 = 0
'''
a = 10                  # 0000 1010 = 10
b = 20                  # 0001 0100 = 20
print("XOR :", a ^ b)   # 0001 1110 = 30

print("XOR :", 15 ^ 11) # 0000 1111 = 15
                        # 0000 1011 = 11
                        # 0000 0100 = 4
'''
Tümleme (Invert) İşleci (~)
Bu işlecin görevi aldığı değeri tersine çevirmektir.
~1 = 0
~0 = 1
'''
a = 1                   # 0000 0001 = 1
print("Tümleme :", ~a)  # 1111 1110 = -2

b = 19                  # 0001 0011 = 19
print("Tümleme :", ~b)  # 1110 1100 = -20

'''
Shifting (kaydırma) İşleçleri (`>>` `<<`)
'''
a = 64                     # 0100 0000 = 64
print("Kaydırma :", a >> 3)# 0000 1000 = 8

b = 16                     # 0001 0000 = 16
print("Kaydırma :", b << 2)# 0100 0000 = 64

a = 15                     # 0000 1111 = 15
print("Kaydırma :", a >> 3)# 0000 0001 = 1
print('#' * 45)

##########################
### 6.Aitlik İşleçleri ###
# in      aitlik işleci  #
# not in  olumsuz        #
##########################
# Liste
meyveler = ["elma", "armut", "muz"]
print("elma" in meyveler)       # True
print("portakal" in meyveler)   # False
print("portakal" not in meyveler)  # True

# String (alt string arama)
metin = "Python programlama dili"
print("Python" in metin)        # True
print("Java" in metin)          # False

# Tuple
renkler = ("kırmızı", "yeşil", "mavi")
print("yeşil" in renkler)      # True

# Dictionary (key'lerde arar)
notlar = {"Ali": 85, "Veli": 72}
print("Ali" in notlar)          # True (key arar)
print(85 in notlar)             # False (value'da aramaz)
print(85 in notlar.values())    # True (value'da aramak için)

# Set
izinli = {"admin", "moderator", "editor"}
print("admin" in izinli)       # True

#############
### Kullanıcı girdisi doğrulama
gecerli_secenekler = ["EVET", "HAYIR", "E", "H"]

cevap = input("Devam? (evet/hayır): ").upper().strip()
if cevap in gecerli_secenekler:
    print(f"Seçiminiz: {cevap}")
else:
    print("Geçersiz seçenek!")

##########################
### 7.Kimlik İşleçleri ###
# id() identity (kimlik) #
# is   karşılaştırma     #
##########################

a = 100
print("id :", id(a))  # 137990748

k = "Dünya!"
print("id :", id(k))  # 14461728


a = 256
print(a is 256)  # True

a = 257
print(a is 257)  # False

a = -5
print(a is -5)  # True

a = -6
print(a is -6)  # False
print('#' * 45)

# is operatörünün en yaygın kullanımı None kontrolüdür:
x = None

# ✅ Doğru yol
if x is None:
    print("x tanımsız")

if x is not None:
    print("x'in bir değeri var")

# ❌ Yanlış yol (çalışır ama PEP 8'e aykırı)
if x == None:
    print("Bu da çalışır ama önerilmez")

# ⚠️ Dikkat: Değer karşılaştırması için her zaman == kullan, is değil. is sadece None kontrolü ve özel durumlar için. is ile True/False kontrolü de yapma — if x is True: yerine if x: yaz.