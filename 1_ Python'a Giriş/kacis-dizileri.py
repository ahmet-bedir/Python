###
print('İstanbul\'un 5 günlük hava durumu tahmini...')
print("Python 1990 yılında \
Guido Van Rossum tarafından \
geliştirilmeye başlanmış, \
oldukça güçlü ve yetenekli bir \
programlama dilidir.")

baslik = "| Türkiye'de Özgür Yazılımın Geçmişi |"
print('-' * len(baslik))
print(baslik, "\n", "-" * len(baslik), sep='')
print(baslik, "-" * (len(baslik)+2), sep="\n")

print("C:\nisan\masraflar.txt") # Yanlış kullanım...
print("C:\\nisan\\masraflar.txt") # Doğru kullanım...
print("C:/nisan/masraflar.txt") # Doğru kullanım...

#f = open("C:\nisan\masraflar.txt","w") # Hata!
#f = open("C:\nisan\masraflar\toplam_masraf.txt","w") # Hata!
#f = open("C:\\nisan\\masraflar\\toplam_masraf.txt","w") # Doğru!

print(*"12345", sep="\t") # Sekme (Tab)
print("Id", "Isim", "Soyisim", "Adres", sep="\t")

print("C:\nisan\masraflar\toplam_masraf.txt")
print("C:\\nisan\\masraflar\\toplam_masraf.txt")

print("\a" * 10) # bip! sesi
print("Merhaba\rZalim Dünya!") # Aynı Satır Başı (Zalim Dünya!)
print("Merhaba\rDünya") # Dünyaba
print("Düşey\vSekme")
# Düşey
#     Sekme
print("yahoo.com\b") # İmleç Kaydırma (yahoo.com)
print("yahoo.com\b.uk") # yahoo.co.uk
print('istihza\b\b\bsn') # istisna

# Küçük Unicode (\u)
#print("Dosya konumu: C:\users\zeynep\gizli\dosya.txt") # Hata!
print("\n\u0061","\u0130","\u0070","\u07F7") # a İ p ߷ (unicode)
print("\u0131","\U00000131") #ı ı
#kısa unicode , uzun unicode


import unicodedata as uni
print("\n", uni.name('a'), sep='') # LATIN SMALL LETTER A
print("\N{LATIN SMALL LETTER A}", end='\n\n') # a

harf = 'b'
print(harf, "harfinin unicode sistemindeki uzun adı :", uni.name(harf))
print(uni.name(harf), "uzun adının harf karşılığı : \N{LATIN SMALL LETTER B}", end='\n\n')

# Onaltılı (hexadecimal) Karakter (\x)
print("\x41","\x61", end='\n\n') # A a

# Etkisizleştirme (r)
print("Kurulum dizini: C:\aylar\nisan\toplam_masraf")
print(r"Kurulum dizini: C:\aylar\nisan\topla_masraf")
print("Kaçış dizileri: \ , \n , \t , \a , \\ , r")
print(r"Kaçış dizileri: \, \n, \t, \a, \\, r", end='\n\n')


#print("Kaçış dizisi: \") # Hata!
#print(r"Kaçış dizisi: \") # Hata!
print("Kaçış dizisi: \ ")
print("Kaçış dizisi: \\")

# Sayfa Başı (\f) 
"""
print("\fırat") # Yanlış kullanım...
f = open("deneme.txt", "w")
print("deneme\fdeneme", file=f)
f.close() 
"""