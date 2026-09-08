######################
## String Metodları ##
###################### 
i = 0
for metot in dir(str):
    if '_' not in metot:
        i += 1
        print("{}.{}".format(i,metot))


#####################
### replace() bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirmek için kullanılır.
kelime = "elma"
print(kelime.replace("e","E")) #Elma
print(kelime) #elma
print("memleket".replace('e','')) #mmlkt
print("memleket".replace('e','',2)) #mmlket

###
metin = "Python 2 harika, Python 2 hızlı"

# Tüm eşleşmeleri değiştir
yeni = metin.replace("Python 2", "Python 3")
print(yeni)  # Python 3 harika, Python 3 hızlı

# Sadece ilk n eşleşmeyi değiştir
yeni2 = metin.replace("Python 2", "Python 3", 1)
print(yeni2)  # Python 3 harika, Python 2 hızlı

# Karakter silme
metin = "  M e r h a b a  "
temiz = metin.replace(" ", "")
print(temiz)  # Merhaba


#####################
### split() metodu üzerine uygulandığı karakter dizilerini parçalarına ayırır ve kelime kelime ayırarak böler, rsplit() metodu bölme işlemine sağdan başlar, splitlines() metodu bir karakter dizisini satır satır ayırmak için kullanılır.
metin = "İstanbul Büyükşehir Belediyesi"

print(metin[0],metin[9],metin[20],sep='') #İBB (Verimsiz yöntem, çünkü bu metot yalnızca “İstanbul Büyükşehir Belediyesi” adlı karakter dizisi için geçerlidir. Eğer karakter dizisi değişirse bu yöntem geçersiz olur)

kelimeler = metin.split()
print(kelimeler) #[İstanbul', 'Büyükşehir', 'Belediyesi']

print(kelimeler[0][0],kelimeler[1][0],kelimeler[2][0],sep='') #İBB (kendi tanımladığımız değişken dışında verimsiz yöntem)

for i in range(len(kelimeler)):
    print(kelimeler[i][0], end='') #İBB

for kelime in metin.split():
    print(kelime[0], end='') #İBB


# split — string'i listeye çevir
cumle = "Python çok güzel bir dil"
kelimeler = cumle.split()
print(kelimeler)  # ['Python', 'çok', 'güzel', 'bir', 'dil']

# Belirli bir ayraçla
tarih = "2024-01-15"
parcalar = tarih.split("-")
print(parcalar)  # ['2024', '01', '15']

# CSV verisi
satir = "Ali,25,İstanbul"
alanlar = satir.split(",")
print(alanlar)  # ['Ali', '25', 'İstanbul']

# Maksimum bölme sayısı
metin = "bir-iki-üç-dört"
print(metin.split("-", 2))  # ['bir', 'iki', 'üç-dört']
    
##
giris = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin : ")
giris_kelimeler = giris.split()
for i in range(len(giris_kelimeler)):
    print(giris_kelimeler[i][0],end='')
##
giris = input("Kısaltmasını öğrenmek istediğiniz kurum adını girin : ")
for kelime in giris.split():
    print(kelime[0],end='')

kardiz = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
print(kardiz.split()) #['Bolvadin,', 'Kilis,', 'Siverek,', 'İskenderun,', 'İstanbul']
print(kardiz.split(', ')) #[Bolvadin', 'Kilis', 'Siverek', 'İskenderun', 'İstanbul']
print(metin.split(' ',1)) #['İstanbul', 'Büyükşehir Belediyesi']
print(metin.rsplit(' ',1)) #['İstanbul Büyükşehir', 'Belediyesi']

# split() metoduyla boşluklardan bölerek bir liste elde ettik. Bu listenin ilk öğesi, kullandığımız Python serisinin sürüm numarasını verecektir.
import sys
print(sys.version.split()[0]) #3.12.1

## Metnimiz enter tuşuna bastığımız noktalardan bölündü.
metin = """Python programlama dili
Guido Van Rossum adlı Hollandalı
bir programcı tarafından 90'lı yılların
başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına
bakarak, bu programlama dili,
adını piton yılanından aldığını düşünür.
Ancak zannedildiğinin aksine
bu programlama dilinin adı
piton yılanından gelmez..."""
print(metin.splitlines())
print(metin.splitlines(True))


###########################
### lower() metodu, karakter dizisindeki bütün harfleri küçük harfe çeviriyor.
print("Kocaeli".lower()) #kocaeli

isim = "Ali Er"
isim = isim.lower(); print(isim) #ali er
if isim == "ali er":
    print("İsim : Ali Er","Şehir : Kocaeli","Yaş : 43", sep="\n")
else:
    print("Aradığınız kişi veritabanında bulunmamaktadır!")

print("İstanbul Iğdır".replace('İ','i').replace('I','ı').lower()) #istanbul ığdır


###########################
### upper() metodu, karakter dizisindeki bütün harfleri büyük harfe çeviriyor.
print("konya".upper()) #KONYA

print("izmit".upper()) #IZMIT
print("izmit".replace('i','İ').upper()) #İZMİT


###########################
### islower() metodu karakter dizisinin tamamen küçük harflerden oluşup oluşmadığını sorguluyor.
print("python".islower()) #True
print("Python".islower()) #False

ad = "ali tonbul"
if not ad.islower():
    print("Sadece Küçük Harf Kullanın!")
else:
    print("İsminiz : ", ad)


#########################
### isupper() metodu karakter dizisinin tamamen büyük harflerden oluşup oluşmadığını sorguluyor.
print("PYTHON".isupper()) #True
print("Python".isupper()) #False

mesaj = """
SELAM NasıLsıN 
İşlerin Nasıl gidiyor
neler yapıyorsun?"""
bol = mesaj.split()
for i in bol:
    if i.isupper():
       print("Tamamı Büyük Harf Olmamalı!")
       break


########################
### endswith() metodu bir karakter dizisinin hangi karakter dizisi ile bittiğini sorguluyor.
print("izmit".endswith('it')) #True
print("izmit".endswith('il')) #False

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"

## mp3 uzantılı dosyaları listeleme.
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11: #bütün değişkenleri for döngüsü içine alıyoruz.
    if i.endswith(".mp3"): #değişkenlerin herbirinin içeriğini tek tek kontrol ediyoruz, eğer baktığımız bu değişkenlerin değerleri “.mp3” ifadesi ile bitiyorsa...
        print(i)
## 2.yöntem      
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i[-4:len(i)] == ".ogg":
        print(i)


########################
### startswith() metodu bir karakter dizisinin hangi karakter dizisi ile başladığını sorguluyor.
for i in d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11:
    if i.startswith("p"): #yada (if i[0] == "p":)
        print(i)
        
###
dosya = "rapor_2024.pdf"

print(dosya.startswith("rapor"))   # True
print(dosya.endswith(".pdf"))      # True
print(dosya.endswith(".txt"))      # False

# Birden fazla seçenekle (tuple)
print(dosya.endswith((".pdf", ".doc", ".txt")))  # True

# URL kontrolü
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print("Geçerli URL")
