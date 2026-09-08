x = 2
y = 3.35
metin = "True"
mantiksal = False

print("Başlangıç Tip Değerleri")
print("x :", x, type(x))
print("y :", y, type(y))
print("metin :", metin, type(metin))
print("mantıksal :", mantiksal, type(mantiksal))

print("int => float")
x = float(x)
print("x :", x, type(x))

print("float => int")
y = int(y)
print("y :", y, type(y))

print("float int => str")
s = str(x) + str(y)
print("x + y :", s, type(s))

print("bool => int")
m = int(mantiksal)
print("mantıksal :", m, type(m))

print("str => bool")
s = bool(metin)
print("metin :", s, type(s))

###
metin = "6.5"
print(metin, type(metin)) #6.5 <class 'str'>

metin = float(metin)
print(metin, type(metin)) #6.5 <class 'float'>

metin = "6.5"
#metin = int(metin) #hata!
metin = int(float(metin))
print(metin, type(metin)) #6 <class 'int'>

metin = "6"
metin = int(metin)
print(metin, type(metin)) #6 <class 'int'>

metin = "6"
metin = float(metin)
print(metin, type(metin)) #6.0 <class 'float'>

### input fonksiyonundan gelen değer her zaman bi karakter dizisidir.
sayi1 = input("1.sayı: ")
sayi2 = input("2.sayı: ")
toplam = sayi1 + sayi2 #toplama işlemi yerine string birleştirme işlemi yapar.
print('Birleşim :', toplam)

#toplam = int(sayi1) + int(sayi2) #toplama işlemi yapar.
#print('Toplam :', toplam)

toplam = float(sayi1) + float(sayi2) #ondalıklı sayı girdiğimizde hata almamak için.
print('Toplam :', toplam)


###
while True:
    girdi = input("Bir tam sayı girin: ")
    try:
        sayi = int(girdi)
        print(f"Girdiğiniz sayı: {sayi}")
        break
    except ValueError:
        print(f"'{girdi}' geçerli bir tam sayı değil! Tekrar deneyin.")

###
# sayi = int("1.2") #hata!

sayi = int(float("1.2"))
print(type(sayi))


################
# ord() — karakter → sayı (Unicode code point)
print(ord('A'))    # 65
print(ord('a'))    # 97
print(ord('0'))    # 48
print(ord('Z'))    # 90
print(ord(' '))    # 32
print(ord('ş'))    # 351
print(ord('€'))    # 8364
print(ord('🐍'))   # 128013

# chr() — sayı → karakter
print(chr(65))     # A
print(chr(97))     # a
print(chr(48))     # 0
print(chr(351))    # ş
print(chr(128013)) # 🐍


###
# ASCII tablosu yazdır
for i in range(32, 127):
    print(f"{i:3d} = {chr(i)}", end="  ")
    if (i - 31) % 8 == 0:
        print()

# Harf → sıra numarası
harf = 'C'
sira = ord(harf) - ord('A') + 1
print(f"'{harf}' alfabenin {sira}. harfi")  # 'C' alfabenin 3. harfi

# Karakterleri kontrol et
print(chr(65).isalpha())   # True — A
print(chr(48).isdigit())   # True — 0
print(chr(32).isspace())   # True — boşluk

# Büyük-küçük harf dönüşümü (elle)
karakter = 'a'
buyuk = chr(ord(karakter) - 32)  # a(97) - 32 = A(65)
print(buyuk)  # A

# Tabii ki .upper() kullanmak daha iyi:
print('a'.upper())  # A

##################
### bin(), oct(), hex(): Sayı Sistemleri

sayi = 255

# İkili (binary) — taban 2
print(bin(sayi))   # '0b11111111'

# Sekizli (octal) — taban 8
print(oct(sayi))   # '0o377'

# Onaltılı (hexadecimal) — taban 16
print(hex(sayi))   # '0xff'

# Ön ek olmadan
print(bin(sayi)[2:])   # '11111111'
print(oct(sayi)[2:])   # '377'
print(hex(sayi)[2:])   # 'ff'

# f-string ile (ön ek olmadan)
print(f"{sayi:b}")     # 11111111
print(f"{sayi:o}")     # 377
print(f"{sayi:x}")     # ff
print(f"{sayi:X}")     # FF (büyük harf)

# Ön ek ile
print(f"{sayi:#b}")    # 0b11111111
print(f"{sayi:#o}")    # 0o377
print(f"{sayi:#x}")    # 0xff

# geri dönüşümü
# String → int (belirli tabandan)
print(int('11111111', 2))   # 255
print(int('377', 8))        # 255
print(int('ff', 16))        # 255
print(int('0xff', 16))      # 255 (ön ekle de çalışır)
print(int('0b11111111', 2)) # 255

# Pratik: Renk kodu dönüşümü
renk_hex = "#FF8C00"  # Koyu turuncu
r = int(renk_hex[1:3], 16)  # 255
g = int(renk_hex[3:5], 16)  # 140
b = int(renk_hex[5:7], 16)  # 0
print(f"RGB({r}, {g}, {b})")  # RGB(255, 140, 0)


# Bit İşlemleri Gösterimi
a = 0b1100  # 12
b = 0b1010  # 10

print(f"a       = {a:04b} ({a})")    # 1100 (12)
print(f"b       = {b:04b} ({b})")    # 1010 (10)
print(f"a & b   = {a & b:04b} ({a & b})")    # 1000 (8)
print(f"a | b   = {a | b:04b} ({a | b})")    # 1110 (14)
print(f"a ^ b   = {a ^ b:04b} ({a ^ b})")    # 0110 (6)


