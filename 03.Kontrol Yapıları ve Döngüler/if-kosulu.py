"""
Koşul True olduğunda kod bloğu çalışır, False olduğunda kod bloğu çalışmaz.
if <koşul>: 
   <kod bloğu>

if True:
    print("kod bloğu...")

if (False):
    print("kod bloğu...")
"""

###
kosul = (3 == 5)
if kosul:
    print("koşul sağlandığında çalışacak kod bloğu...")

###
login = False
if login:
    print("giriş başarılı...")

###
email = "info@gmail.com"
parola = "123"
login = (email == "inf@gmail.com") and (parola == "123")
if login:
    print("giriş başarılı...")

### Verimsiz yöntem, çünkü 10'un altında bir değer girilmesi durumunda hem birinci hem ikinci if bloğu çalışır.
# İlk yöntem.
# sayi = int(input("Sayı Giriniz : "))
#
# if sayi < 10:
#     print("sayı 10'dan küçüktür.")
#
# if sayi < 20:
#     print("sayı 20'den küçüktür.")
#
# if sayi > 20:
#     print("sayı 20'den büyüktür.")
#
# if sayi > 30:
#     print("sayı 30'dan büyüktür.")
#
### if bize olası bütün sonuçları listeler, elif ise sadece doğru olan ilk sonucu verir.
# İkinci yöntem.
# sayi = int(input("Sayı Giriniz : "))
#
# if sayi < 10:
#     print("sayı 10'dan küçüktür.")
# elif sayi < 20:
#     print("sayı 20'den küçüktür.")
# elif sayi > 30:
#     print("sayı 30'dan büyüktür.")
# elif sayi > 20:
#     print("sayı 20'den büyüktür.")
#

### Python koşulları yukarıdan aşağıya doğru sırayla kontrol eder. İlk True olan koşulun bloğu çalışır ve geri kalanlar atlanır.
not_ortalamasi = 79

if not_ortalamasi >= 90:
    harf = "AA"
elif not_ortalamasi >= 80:
    harf = "BA"
elif not_ortalamasi >= 70:
    harf = "BB"
elif not_ortalamasi >= 60:
    harf = "CB"
else:
    harf = "FF"

print(f"Harf notun: {harf}")  # Harf notun: BB


### Ternary Expression (Üçlü İfade)
# değer_true if koşul else değer_false
n = 7

# Klasik yol
if n > 0:
    sonuc = "pozitif"
else:
    sonuc = "negatif"

# Ternary yol
sonuc = "pozitif" if n > 0 else "negatif"
print(sonuc)  # pozitif


###
_not = 51
status = "Geçti" if _not > 50 else "Kaldı"
print(f"{status}")

# Değişken ataması
yas = 18
durum = "yetişkin" if yas >= 18 else "çocuk"

# Return ifadesinde
def mutlak_deger(n):
    return n if n >= 0 else -n

# f-string içinde
print(f"Sayı {'çift' if n % 2 == 0 else 'tek'}")


#################
# Bunların hepsi False olarak değerlendirilir:
falsy_degerler = [
    False,      # Boolean False
    None,       # None
    0,          # Sıfır (int)
    0.0,        # Sıfır (float)
    0j,         # Sıfır (complex)
    "",          # Boş string
    [],         # Boş liste
    {},         # Boş dictionary
    set(),      # Boş set
    (),         # Boş tuple
    range(0),   # Boş range
]

for deger in falsy_degerler:
    print(f"{str(deger):12} -> bool: {bool(deger)}")
# Bunlar dışındaki her şey truthy'dir. "False" string'i bile truthy'dir (boş olmayan string olduğu için)!

###############
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — değerleri aynı
print(a is b)   # False — farklı nesneler
print(a is c)   # True  — aynı nesne

# None kontrolünde her zaman is kullan
x = None
if x is None:      # ✅ Doğru
    print("x None")

if x == None:      # ❌ Çalışır ama tavsiye edilmez
    print("x None")
# == değer eşitliği, is kimlik eşitliği (aynı nesne mi?) kontrol eder. None kontrollerinde her zaman is kullan.

