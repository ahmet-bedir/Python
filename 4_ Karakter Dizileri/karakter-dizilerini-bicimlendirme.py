### % İşareti ile Biçimlendirme (Eski Yöntem)

parola = input("parola: ")

print("Girdiğiniz parola (%s) kurallara uygun bir paroladır!" %parola)

### s harfi karakter dizilerini ve karakter dizisine çevrilebilen değerleri temsil eder.
print("%s ve %s iyi bir ikilidir!" %("Python","Django"))

# hata! çünkü karakter dizisi içindeki %s işaretlerinin sayısı ile karakter dizisi dışında bu işaretlere karşılık gelen değerlerin sayısı birbirini tutmuyor.
#print("Benim adım %s , soyadım %s " %"Ali")

#
kelime = "istihza"
for sira, karakter in enumerate(kelime, 1):
    print("%s.karakter '%s'" %(sira, karakter))

#
for i in range(1,11):
    print("%%%s" %i)

# % ile s işaretleri arasına yerleştirdiğimiz sayı, biçimlendirilecek karakter dizisinin toplam kaç karakterlik yer kaplayacağını gösteriyor.
for i in dir(str):
    print("%15s" %i)

for i in dir(str):
    print("|%15s|" %i)
for i in dir(str):
    print("|%-15s|" %i)

##
dil = "Python Programlama Dili"
sayfa = """
<html>
    <head>
        <title> %s </title>
    </head>
    <body>
        <h1> %s </h1>
        <p> Web sitemize hoşgeldiniz! Konumuz: %s </p>
    </body>
</html>
"""
print(sayfa %(dil,dil,dil))

## veya tekrardan kaçınmak için:
dil = "Python Programlama Dili"
sayfa = """
<html>
    <head>
        <title> %(d)s </title>
    </head>
    <body>
        <h1> %(d)s </h1>
        <p> Web sitemize hoşgeldiniz! Konumuz: %(d)s </p>
    </body>
</html>
"""
print(sayfa %{"d":dil})

# "%(değişken_adı)s " % {"değişken_adı": "değişken_değeri"}
print("Depoda %(miktar)s kilo %(ürün)s kaldı" %{"ürün": "elma", "miktar": 25})

### d harﬁ sayıları temsil eder.
print("Şubat ayı bu yıl %d gün çekiyor" %28)

#
#print("Şubat ayı bu yıl %d gün çekiyor" %"28") #hata! Çünkü d harﬁ yalnızca sayı değerleri temsil edebilir, bu harﬂe birlikte karakter dizilerini kullanamayız.

print("%d" %10.3) #10

#
sayi = input("Sayı: ")

print("%d" %float(sayi))


### i harfi de integer, yani ‘tam sayı’ kelimesinin kısaltmasıdır. Kullanım ve işlev olarak, d harfinden hiç bir farkı yoktur.

### o harfi octal (sekizli) düzendeki sayıları temsil eder. Dolayısıyla bu harfi kullanarak onlu düzendeki bir sayıyı sekizli düzendeki karşılığına dönüştürebilirsiniz.
print("%i sayısının sekizli düzendeki karşılığı %o sayısıdır." %(10, 10))


### x harfi hexadecimal, yani onaltılı düzendeki sayıları temsil eder. Bu harfi kullanarak onlu düzendeki bir sayıyı onaltılı düzendeki karşılığına çevirebilirsiniz.
print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(20, 20))

print("%i sayısının onaltılı düzendeki karşılığı %x sayısıdır." %(10, 10))
print("%i sayısının onaltılı düzendeki karşılığı %X sayısıdır." %(10, 10))


### f kayan noktalı sayıları(float) temsil etmek için kullanılır.
print("Dolar %f TL olmuş..." %1.4710) #1.471000 (Python’da bir karakter dizisi içindeki sayıyı %f yapısı ile kayan noktalı sayıya çevirdiğimizde noktadan sonra öntanımlı olarak 6 hane yer alacaktır)
print("Dolar %.2f TL olmuş..." %1.4710) #1.47


### c harf tek bir karakteri temsil eder. c harfinin bir başka özelliği de ASCII tablosunda sayılara karşılık gelen karakterleri de gösterebilmesidir.
print("%c" %"a")
#print("%c" %"ani") #hata!
print("%c" %65) #A
#
for i in range(128):    
    print("%i ==> %c" %(i, i))
#
for sira, karakter in enumerate(dir(str)):
    if sira % 3 == 0:
        print("\n", end="")
    print("%-20s" %karakter, end="")
#    
for i in range(20):
    print("%(deger)5d%(deger)5o%(deger)5x" %{"deger":i})
    
#####################################
### format() Metodu ile Biçimlendirme (Yeni Yöntem)
print("{} ve {} iyi bir ikilidir!".format("Django", "Python"))

# 1.yöntem
kalkis = input("Kalkış yeri: ")
varis = input("Varış yeri: ")
isim_soyisim = input("İsim ve soyisim: ")
bilet_sayisi = input("Bilet sayısı: ")
print("""{} noktasından {} noktasına, 14:30 hareket saatli sefer için
{} adına {} adet bilet ayrılmıştır!""".format(kalkis, varis, isim_soyisim, bilet_sayisi))

# 2.yöntem
kalkis = input("Kalkış yeri : ")
varis = input("Varış yeri : ")
isim_soyisim = input("İsim ve soyisim : ")
bilet_sayisi = input("Bilet sayısı : ")
metin = """{} noktasından {} noktasına, 14:30 hareket saatli sefer için
{} adına {} adet bilet ayrılmıştır!"""
print(metin.format(kalkis, varis, isim_soyisim, bilet_sayisi))

##
kodlama = "utf-8"
site_adi = "Python Programlama Dili"
dosya = open("deneme.html", "w", encoding=kodlama)
icerik = """
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset={0}"/>
        <title>{1}</title>
    </head>
    <body>
        <h1>istihza.com web sitesine hoş geldiniz!</h1>
        <p><b>{1}</b> için bir Türkçe belgelendirme projesi...</p>
    </body>
</html>
"""
print(icerik.format(kodlama, site_adi), file=dosya)
dosya.close()

##
print("{0} {1}".format("Ahmet","Bedir"))
print("{1} {0}".format("Ahmet","Bedir"))
print("{0} {1} {1} {0}".format("Ahmet","Bedir"))

#
print("{dil} dersleri".format(dil="python"))

print("|{:>15}|".format("python"))
print("|{:<15}|".format("python"))
print("|{:^15}|".format("python"))

#
for sira, karakter in enumerate(dir(str)):
    if sira % 3 == 0:
        print("\n", end="")
    print("{:<20}".format(karakter), end="")

### s harfi karakter dizilerini temsil eder.
print("{:s}".format("karakter dizisi"))
print("{:s}".format(1)) # hata!

### c harfi 0 ile 256 arası sayıların ASCII tablosundaki karşılıklarını temsil eder.
print("{:c}".format(97)) # a

### d harfi sayıları temsil eder.
print("{:d}".format(65))
print("{:d}".format("65")) # hata!

### o harfi onlu düzendeki sayıları sekizli düzendeki karşılıklarına çevirir.
print("{:o} ".format(65))

### x harfi onlu düzendeki sayıları onaltılı düzendeki karşılıklarına çevirir.
print("{:x} ".format(65))

print("{:x} ".format(10)) # a
print("{:X} ".format(10)) # A
#
for i in range(21):
    print("{:x}{:20X}".format(i,i))

### b harfi onlu düzendeki sayıları ikili düzendeki karşılıklarına çevirir.
print("{:b} ".format(5)) # 101

### f
print("{:.5f} ".format(50)) # 50.00000

## , işareti sayıları basamaklarına ayırmak için kullanılır.
print("{:,}".format(123456789)) # 123,456,789