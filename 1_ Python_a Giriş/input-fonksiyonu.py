###
giris = input("Adınız : ")
print("-" * 30)
print("Adınız\t:", giris)
print("-" * 30)

###input() fonksiyonundan gelen veri her zaman bir karakter dizisidir.
sayi1 = input("1.Sayı : ")
sayi2 = input("2.Sayı : ")
print("-" * 30)
print(sayi1, "+", sayi2, ":", sayi1 + sayi2) #Yanlış kullanım!
#Gelen veriyle herhangi bir aritmetik işlem yapabilmek için öncelikle bu veriyi bir sayıya dönüştürmemiz gerekir.
print(sayi1, "+", sayi2, ":", int(sayi1) + int(sayi2)) #Doğru kullanım...
print("-" * 30)

###
veri = input("Veri Giriniz : ")
tip = type(veri)
print("-" * 30)
print("Girilen Verinin Tipi :", tip) #Girilen Verinin Tipi : <class 'str'>
print("-" * 30)

###
r = input('Dairenin Yarıçapını Giriniz : ')
pi = 3.14
alan = pi * (int(r) ** 2)
cevre = 2 * pi * int(r)
print("-" * 30)
print(r, "Yarıçaplı Dairenin ;")
print("Alanı : ", alan, "\nÇevresi : ",
cevre)
print("-" * 30)

###
sayi = input("Sayı Giriniz : ")
basamak_uzunlugu = len(sayi)
print("-" * 30)
print("Girilen Sayı :", sayi)
print("Sayının Basamak Uzunluğu :", basamak_uzunlugu)
print("-" * 30)

###
s1 = "7.7"; s2 = "6.2"
print("-" * 30)
print(s1 + " ve " + s2 + " Birleşimi :", s1 + s2)
print(s1 + " ve " + s2 + " Toplamı :", float(s1) + float(s2))
print("-" * 30)

###
s = 13
print("-" * 30)
print(s, "Sayısının Veritipi :", type(s))
s = complex(s)
print(s, "Sayısının Veritipi :", type(s))
s = 9+0j
s = str(s)
print(s, type(s))
#s = int(s) #Hata! complex bir sayıyı tamsayıya çeviremeyiz...
print("-" * 30)

#print(int("2.5")) #Hata!
print(int(float("2.5")))