###
isim = 'Buğra'
print(f'Selam {isim}!')

##
isim = 'Ahmet'
yas = 36
metin = f'Benim adım {isim} ve ben {yas} yaşındayım.'
print(metin)

## aynı işlem format() metoduyla...
isim = 'Ahmet'
yas = 36
metin = 'Benim adım {} ve ben {} yaşındayım.'
print(metin.format(isim,yas))

#
sayi1 = 3
sayi2 = 2
print(F'{sayi1} + {sayi2} = {sayi1+sayi2}')

#
fstring = "f-string"
print(f"{{ {fstring} : f'{{ifade}}' şeklinde kullanılır. }}")
# { f-string : f'{ifade}' şeklinde kullanılır. }

# Çok satırlı f-string
isim = "Ali"
yas = 25
sehir = "İstanbul"

bilgi = (
    f"İsim: {isim}\n"
    f"Yaş: {yas}\n"
    f"Şehir: {sehir}"
)
print(bilgi)

# = ile değişken adını ve değerini birlikte gösterme.
kaynak = "Python"
sene = 2022
print(f"{kaynak = } {sene = }")
# kaynak = 'Python' sene = 2022

x = 42
y = "merhaba"
z = [1, 2, 3]

# = ile değişken adını ve değerini birlikte göster
print(f"{x = }")    # x = 42
print(f"{y = }")    # y = 'merhaba'
print(f"{z = }")    # z = [1, 2, 3]

# İfadelerle de çalışır
print(f"{x * 2 = }")         # x * 2 = 84
print(f"{len(z) = }")        # len(z) = 3
print(f"{y.upper() = }")     # y.upper() = 'MERHABA'

###
print(f"|{kaynak:^20}|")
# |       Python       |
print(f"|{kaynak:#^20}|")
# |#######Python#######|
print(f"|{kaynak:<20}|")
# |Python              |
print(f"|{kaynak:>20}|")
# |              Python|
print(f"|{kaynak:<020}|")
# |Python00000000000000|

#
print(f'Sayıların toplamı {int(input("Birinci sayıyı girin: ")) + int(input("İkinci sayıyı girin: "))} eder.')

# sayı formatlama...
sayi = 123
print(f"{sayi:>6}") #'   123'

print(f"{sayi:0>+6}") #'00+123'

print(f"{sayi:0=+6}") #'+00123'


# Genişlik ve hizalama
isim = "Ali"
print(f"|{isim:<10}|")   # |Ali       | (sola hizalı)
print(f"|{isim:>10}|")   # |       Ali| (sağa hizalı)
print(f"|{isim:^10}|")   # |   Ali    | (ortalı)
print(f"|{isim:*^10}|")  # |***Ali****| (yıldızla doldur)

# Sayı formatlama
sayi = 1234567.89
print(f"{sayi:,.2f}")    # 1,234,567.89
print(f"{sayi:>15,.2f}") #   1,234,567.89

# Yüzde
oran = 0.856
print(f"{oran:.1%}")     # 85.6%

# Sayı sistemleri
x = 255
print(f"{x:b}")   # 11111111
print(f"{x:o}")   # 377
print(f"{x:x}")   # ff
print(f"{x:#x}")  # 0xff


print(f"Binary: {sayi:b} | Octal: {sayi:o} | Hexadecimal: {sayi:x}") #'Binary: 1111011 | Octal: 173 | Hexadecimal: 7b'

print(f"Binary: {sayi:#b} | Octal: {sayi:#o} | Hexadecimal: {sayi:#x}") #'Binary: 0b1111011 | Octal: 0o173 | Hexadecimal: 0x7b'


ondalik = 0.123
print(f"{ondalik:.2f}") # f | F ondalık formatlama  '0.12'

print(f"{ondalik:.5f}") #'0.12300'

print(f"{ondalik:.5g}") # g | G fazla sıfırlar dahil edilmez  '0.123'

sayi = 123456
print(f"{sayi:_}") #'123_456'

print(f"{sayi:-^15_}") #'----123_456----'

print(f"{sayi:,}") #'123,456'

# Yüzde gösterimi
oran = 0.856
print(f"Başarı oranı: {oran:.1%}")  # 85.6%

islem = 1 / 12
print(f"{islem:.2%}") # Sonucun 100 ile çarpılmış halini yüzde olarak çıktı verir  '8.33%'

#
selam = "Hello, World!"
hizalama = {"Sol": "<", "Orta": "^", "Sağ": ">"}
genislik = 25
for hiza, operator in hizalama.items():
    print(f"{hiza:>5}: '{selam:{operator}{genislik}}'")
"""
 Sol: 'Hello, World!            '
Orta: '      Hello, World!      '
 Sağ: '            Hello, World!'
"""

# Hizalama
for urun, fiyat in [("Elma", 5), ("Portakal", 7.5), ("Muz", 12)]:
    print(f"{urun:<10} {fiyat:>6.2f} TL")
"""
Elma         5.00 TL
Portakal     7.50 TL
Muz         12.00 TL
"""

###
yy, aa, gg = "2022-12-31".split("-")

print(f"{gg}/{aa}/{yy} ({type(gg)}{type(aa)}{type(yy)})")


##################
### String Karşılaştırma
## Her karakter unicode değerine göre karşılaştırılır.
print("apple" < "banana")   # True (a < b)
print("apple" < "apricot")  # True (3. karakter: p < r)
print("ABC" < "abc")        # True (A=65, a=97)

# Büyük/küçük harf duyarsız karşılaştırma
s1 = "Python"
s2 = "python"
print(s1 == s2)                # False
print(s1.lower() == s2.lower()) # True

# in operatorü
metin = "Python programlama dili"

print("Python" in metin)      # True
print("Java" in metin)        # False
print("python" in metin)      # False (büyük-küçük harf duyarlı)
print("program" in metin)     # True (alt string arama)

# not in
print("Java" not in metin)    # True

# Koşulda kullanım
email = "ali@example.com"
if "@" in email and "." in email:
    print("Geçerli e-posta formatı")
    
# Üyelik Kontrolü Deseni
# Yasaklı kelime kontrolü
yasak_kelimeler = ["spam", "reklam", "dolandırıcılık"]
mesaj = "Bu bir reklam mesajıdır"

for kelime in yasak_kelimeler:
    if kelime in mesaj.lower():
        print(f"Yasaklı kelime bulundu: {kelime}")
        break