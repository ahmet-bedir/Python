#girilen sayının tek veya çift sayı olup olmadığını bulan program.

i = int(input('Bir Sayı Giriniz : '))
if i % 2 == 0:
    print("Girilen Sayı Çiftdir...")
else:
    print("Girilen Sayı Tekdir...")

#girilen iki sayının birbirine tam bölüp bölünmediğini bulan program.

bolunen = int(input("Bir sayı girin : "))
bolen = int(input("Bir sayı daha girin : "))

sablon = "{} sayısı {} sayısına tam".format(bolunen, bolen)

if bolunen % bolen == 0:
    print(sablon, "bölünüyor!")
else:
    print(sablon, "bölünmüyor!")

