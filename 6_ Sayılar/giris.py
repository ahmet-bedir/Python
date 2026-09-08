"""
Sayı Okunabilirliği: Alt Çizgi Ayracı
Büyük sayıları okumak zordur. Python 3.6+ ile sayılara alt çizgi ekleyebilirsin — Python bunları yoksayar:
"""

nufus = 85_000_000        # 85 milyon
butce = 1_234_567_890     # 1.2 milyar
renk = 0xFF_FF_FF         # Hex renk kodu
binary = 0b1010_0011      # İkili sayı

print(nufus)  # 85000000 — alt çizgiler çıktıda görünmez


# float: Ondalıklı Sayılar ve Hassasiyet
# float hassasiyet örnekleri
print(f"{0.1:.20f}")     # 0.10000000000000000555
print(f"{0.2:.20f}")     # 0.20000000000000001110
print(f"{0.3:.20f}")     # 0.29999999999999998890

# Eşitlik kontrolünde dikkat!
a = 0.1 + 0.2
b = 0.3

# ❌ Yanlış
print(a == b)  # False

# ✅ Doğru — toleranslı karşılaştırma
print(abs(a - b) < 1e-9)  # True

# veya math.isclose kullan
import math
print(math.isclose(a, b))  # True
"""
⚠️ Dikkat: Finansal hesaplamalarda asla float kullanma! Para hesabı yapıyorsan decimal modülünü kullan. 0.1 cent'lik hatalar milyonlarca işlemde büyük farklar yaratır.
"""
#####################################################
"""
complex: Karmaşık Sayılar
Karmaşık sayılar bir gerçel (real) ve bir sanal (imaginary) kısımdan oluşur. Matematikte i ile gösterilen sanal birim, Python'da j ile gösterilir.
"""

z = 3 + 4j
print(z)           # (3+4j)
print(type(z))     # <class 'complex'>

# Gerçel ve sanal kısımlar
print(z.real)      # 3.0
print(z.imag)      # 4.0

# Eşlenik (conjugate)
print(z.conjugate())  # (3-4j)

# Büyüklük (modül)
print(abs(z))      # 5.0 — (3² + 4² = 25, √25 = 5)

###
# Karmaşık sayılarla aritmetik
z1 = 2 + 3j
z2 = 1 - 1j

print(z1 + z2)  # (3+2j)
print(z1 * z2)  # (5+1j)
print(z1 / z2)  # (-0.5+2.5j)

# complex() fonksiyonu ile oluşturma
z3 = complex(5, -2)  # 5 - 2j
print(z3)  # (5-2j)

