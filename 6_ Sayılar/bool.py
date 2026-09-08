################
print(isinstance(True, int))   # True — bool, int'in alt sınıfı
print(True == 1)    # True
print(False == 0)   # True

# Aritmetik işlemlerde kullanılabilir
print(True + True)        # 2
print(True + False)       # 1
print(True * 10)          # 10
print(False * 10)         # 0

# Sayma trick'i — True'ları say
sayilar = [3, 7, 2, 9, 1, 8, 4]
buyuk_sayisi = sum(x > 5 for x in sayilar)
print(f"5'ten büyük: {buyuk_sayisi}")  # 3 (Bu, her True bir 1 olduğu için çalışır. sum() içinde her True 1 olarak toplanır)


################
# Doğru cevap yüzdesi
cevaplar = [True, False, True, True]
basari_orani = sum(cevaplar) / len(cevaplar)
print(f"Başarı: {basari_orani:.0%}")  # Başarı: 75%

################
# Bu değerlerin hepsi False olarak değerlendirilir
falsy_degerler = [
    False,      # bool False
    0,          # sıfır (int)
    0.0,        # sıfır (float)
    0j,         # sıfır (complex)
    "",         # boş string
    [],         # boş liste
    (),         # boş tuple
    {},         # boş dict
    set(),      # boş set
    None,       # None
    range(0),   # boş range
]

for deger in falsy_degerler:
    print(f"bool({str(deger)}) = {bool(deger)}")

# Bunların hepsi True olarak değerlendirilir
truthy_degerler = [
    True,           # bool True
    1,              # sıfır olmayan int
    -1,             # negatif sayılar da truthy
    3.14,           # sıfır olmayan float
    "merhaba",      # dolu string
    " ",            # boşluk bile truthy (boş değil çünkü)
    [1, 2],         # dolu liste
    {"a": 1},       # dolu dict
    (0,),           # dolu tuple (içi 0 olsa bile)
]

for deger in truthy_degerler:
    print(f"bool({str(deger):15s}) = {bool(deger)}")


###
liste = []
aktif = True
isim = "ali"

# ❌ Gereksiz karşılaştırma
if len(liste) > 0:
    print("Liste dolu")

if aktif == True:
    print("Aktif")

if isim != "":
    print("İsim var")

# ✅ Pythonic yol
if liste:
    print("Liste dolu")

if aktif:
    print("Aktif")

if isim:
    print("İsim var")

# Boş kontrolleri
def kullanici_bilgi(isim, email=None, telefon=None):
    print(f"İsim: {isim}")

    if email:
        print(f"E-posta: {email}")
    else:
        print("E-posta belirtilmemiş")

    if telefon:
        print(f"Telefon: {telefon}")
    else:
        print("Telefon belirtilmemiş")

kullanici_bilgi("Ali", email="ali@test.com")
# İsim: Ali
# E-posta: ali@test.com
# Telefon belirtilmemiş


# int ve float karşılaştırılabilir
print(1 == 1.0)     # True
print(1 < 1.5)      # True

# bool ve int karşılaştırılabilir (bool, int'in alt sınıfı)
print(True == 1)    # True
print(False == 0)   # True

# String karşılaştırma — leksikografik (Unicode sırasına göre)
print("apple" < "banana")   # True
print("abc" < "abd")        # True
print("A" < "a")            # True (A=65, a=97)

# Farklı tipler karşılaştırılamaz (< , > için)
# print("5" < 5)  # TypeError!
print("5" == 5)    # False — hata vermez ama False döner

###
def giris_kontrol(kullanici_adi, sifre, aktif_mi):
    if not kullanici_adi or not sifre:
        return "Kullanıcı adı ve şifre gerekli!"

    if not aktif_mi:
        return "Hesabınız aktif değil!"

    if len(sifre) < 8:
        return "Şifre en az 8 karakter olmalı!"

    return "Giriş başarılı!"

print(giris_kontrol("ali", "12345678", True))   # Giriş başarılı!
print(giris_kontrol("", "12345678", True))        # Kullanıcı adı ve şifre gerekli!
print(giris_kontrol("ali", "123", True))          # Şifre en az 8 karakter olmalı!
print(giris_kontrol("ali", "12345678", False))    # Hesabınız aktif değil!

#######################
# and operatöründe ilk değer False ise, ikinci değere bakmaya gerek yok — sonuç zaten False.
# İlk koşul False → ikinci koşul hiç çalışmaz
x = 0
if x != 0 and 10 / x > 2:  # 10/0 hatası olmaz!
    print("Koşul sağlandı")
else:
    print("x sıfır")  # Bu çalışır

# Güvenli erişim deseni
liste = []
if liste and liste[0] > 5:  # Boş liste → IndexError olmaz!
    print("İlk eleman 5'ten büyük")

# or operatöründe ilk değer True ise, ikinci değere bakmaya gerek yok — sonuç zaten True
# İlk koşul True → ikinci koşul hiç çalışmaz
x = 10
if x > 5 or cok_pahali_fonksiyon():  # Bu fonksiyon çağrılmaz!
    print("Koşul sağlandı")

##############
# Varsayılan Değer Deseni
# or operatörünün bu davranışı, varsayılan değer atamak için kullanılır:
# Kullanıcı isim girmemişse varsayılan kullan
isim = input("İsminiz: ") or "Anonim"

print(isim)

##############
# Fonksiyon parametrelerinde
def selamla(isim=None):
    isim = isim or "Dünya"
    return f"Merhaba, {isim}!"

print(selamla())         # Merhaba, Dünya!
print(selamla("Ali"))    # Merhaba, Ali!

##############
### None: Python'un "hiçbir şey" değeridir. Bir değişkenin henüz bir değeri olmadığını veya bir fonksiyonun bir şey döndürmediğini belirtir.

# None şunlardan farklıdır:
# 0 (bir sayı — değeri var, o değer sıfır)
# "" (bir string — değeri var, o değer boş metin)
# False (bir boolean — değeri var, o değer yanlış)
# [] (bir liste — değeri var, o değer boş bir koleksiyon)
# None ise "değer yok, tanımsız, belirsiz" demektir.
print(type(None))      # <class 'NoneType'>
print(type(0))         # <class 'int'>
print(type(""))        # <class 'str'>
print(type(False))     # <class 'bool'>

#
print(None == 0)       # False
print(None == "")      # False
print(None == False)   # False
print(None == None)    # True

##############
# None kontrolünde her zaman is operatörü kullanılır, == değil.
x = None

# ✅ Doğru
if x is None:
    print("x None")

# ✅ Doğru
if x is not None:
    print("x None değil")

# ❌ Yanlış (çalışır ama doğru değil)
if x == None:
    print("x None")

##############
# Bir fonksiyon açıkça return ifadesi kullanmazsa veya return tek başına kullanılırsa, None döner.
def selamla(isim):
    print(f"Merhaba, {isim}!")
    # return yok → None döner

sonuc = selamla("Ali")
print(sonuc)       # None
print(type(sonuc)) # <class 'NoneType'>

###
# return tek başına da None döner
def ara_ve_dur(liste, hedef):
    for eleman in liste:
        if eleman == hedef:
            print(f"{hedef} bulundu!")
            return  # None döner
    print(f"{hedef} bulunamadı")
    # return yok → None döner

sonuc = ara_ve_dur([1, 2, 3], 2)
print(sonuc)  # None

##############
### any() — En az bir True varsa True döner
print(any([False, False, True]))   # True
print(any([False, False, False]))  # False
print(any([]))                      # False (boş → False)

# Pratik kullanım
notlar = [45, 72, 38, 91, 55]
gecen_var_mi = any(n >= 50 for n in notlar)
print(f"Geçen öğrenci var mı? {gecen_var_mi}")  # True

# String kontrolü
sifre = "MyPassword123"
has_digit = any(c.isdigit() for c in sifre)
len_digit = 0
for c in sifre:
    if c.isdigit():
        len_digit += 1

has_upper = any(c.isupper() for c in sifre)
len_upper = 0
for c in sifre:
    if c.isupper():
        len_upper += 1

has_lower = any(c.islower() for c in sifre)
len_lower = 0
for c in sifre:
    if c.islower():
        len_lower += 1

print(f"Şifre: {sifre}")
print(f"Rakam: {has_digit} -> {len_digit}\nBüyük: {has_upper} -> {len_upper}\nKüçük: {has_lower} -> {len_lower}")

##############
### all() - Hepsi True ise True döner
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([]))                     # True (boş → True, dikkat!)

# Pratik kullanım
notlar = [65, 72, 58, 91, 55]
hepsi_gecti_mi = all(n >= 50 for n in notlar)
print(f"Herkes geçti mi? {hepsi_gecti_mi}")  # True

# Form doğrulama
form = {
    "isim": "Ali",
    "email": "ali@test.com",
    "sifre": "12345678",
}
tum_alanlar_dolu = all(form.values())
print(f"Tüm alanlar dolu mu? {tum_alanlar_dolu}")  # True