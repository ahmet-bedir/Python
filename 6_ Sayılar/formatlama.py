# Sayı Formatlama: f-string ile

sayi = 3.14159265

# Ondalık basamak sayısı
print(f"{sayi:.2f}")   # 3.14
print(f"{sayi:.4f}")   # 3.1416
print(f"{sayi:.0f}")   # 3

# Minimum genişlik
print(f"{sayi:10.2f}")  # '      3.14' (10 karakter genişlik)
print(f"{sayi:<10.2f}") # '3.14      ' (sola hizalı)
print(f"{sayi:^10.2f}") # '   3.14   ' (ortaya hizalı)

# Sıfır doldurma
print(f"{sayi:010.2f}") # '0000003.14'

# Binlik Ayraç
buyuk_sayi = 1234567890

# Virgülle ayır
print(f"{buyuk_sayi:,}")      # 1,234,567,890

# Alt çizgiyle ayır
print(f"{buyuk_sayi:_}")      # 1_234_567_890

# Ondalıklı ve virgüllü
fiyat = 1234567.89
print(f"{fiyat:,.2f}")        # 1,234,567.89
print(f"₺{fiyat:,.2f}")      # ₺1,234,567.89

# Yüzde Formatı
oran = 0.856
print(f"{oran:.1%}")   # 85.6%
print(f"{oran:.0%}")   # 86%

basari = 45 / 60
print(f"Başarı oranı: {basari:.2%}")  # Başarı oranı: 75.00%

# Bilimsel Gösterim
buyuk = 6.022e23
kucuk = 1.6e-19

print(f"{buyuk:.3e}")   # 6.022e+23
print(f"{kucuk:.2e}")   # 1.60e-19
print(f"{buyuk:.3E}")   # 6.022E+23 (büyük E)

# Farklı Sayı Sistemleri

sayi = 255

print(f"{sayi:b}")   # 11111111 (binary)
print(f"{sayi:o}")   # 377 (octal)
print(f"{sayi:x}")   # ff (hex küçük)
print(f"{sayi:X}")   # FF (hex büyük)
print(f"{sayi:d}")   # 255 (decimal)

# Ön ek ile
print(f"{sayi:#b}")  # 0b11111111
print(f"{sayi:#o}")  # 0o377
print(f"{sayi:#x}")  # 0xff

# İşaret Gösterimi
# Pozitif sayılarda da + göster
print(f"{42:+d}")    # +42
print(f"{-42:+d}")   # -42

# Pozitif sayılarda boşluk, negatif sayılarda -
print(f"{42: d}")    # ' 42'
print(f"{-42: d}")   # '-42'
