def bolme_islemi(bolunen, bolen):
    """Bölüm ve kalanı birlikte döndürür."""
    bolum = bolunen // bolen
    kalan = bolunen % bolen
    return bolum, kalan  # Aslında bir tuple: (bolum, kalan)

# Tuple unpacking ile al
bolum, kalan = bolme_islemi(17, 5)
print(f"17 ÷ 5 = {bolum}, kalan {kalan}")  # 17 ÷ 5 = 3, kalan 2

# Tek değişkene de atayabilirsin (tuple olarak)
sonuc = bolme_islemi(17, 5)
print(sonuc)        # (3, 2)
print(sonuc[0])     # 3 (bölüm)
print(sonuc[1])     # 2 (kalan)