#######################
### str.maketrans(), translate()
kaynak = "a"
hedef  = "A"

ceviri = str.maketrans(kaynak, hedef)
print(ceviri) #{97: 65} ascii tablosundaki sayı karşılıkları.
#
kaynak = "şçöğüıŞÇÖĞÜİ"
hedef  = "scoguiSCOGUI"

ceviri_tablosu = str.maketrans(kaynak, hedef)

metin = "Bildiğiniz gibi, internet üzerinde bazen Türkçe karakterleri kullanamıyoruz."
print(metin.translate(ceviri_tablosu))

#Türkçe-F klavye düzeni ile yazılmış metni, Türkçe-Q kavye düzenine çevirme.
metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

q_klavye_duzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_klavye_duzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

ceviri_tablosu = str.maketrans(q_klavye_duzeni, f_klavye_duzeni)

print(metin.translate(ceviri_tablosu))

#metinde bulunan bütün sesli harflerin silinmesi.
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""

sesli_harfler = "aeıioöuüAEIİOÖUÜ"

yeni_metin = ""

for i in metin:
    if not i in sesli_harfler:
        yeni_metin += i

print(yeni_metin)

#
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""

silinecek = "aeıioöuüAEIİOÖUÜ"

ceviri = str.maketrans('','',silinecek)

print(metin.translate(ceviri))

#
metin = "Can Yılmaz"

kaynak = "CY"
hedef  = "cy"
silinecek = "aı "

çeviri_tablosu = str.maketrans(kaynak, hedef, silinecek)

print(metin)
print(metin.translate(çeviri_tablosu))


#######################
### isalpha() metodu bir karakter dizisinin tamamının ‘alfabetik’ olup olmadığını denetlemek için kullanılır.
a = "izmit"
print(a.isalpha()) #True

a = "izmit41"
print(a.isalpha()) #False


#######################
### isdigit() metodu bir karakter dizisinin 'sayı değerli karakter dizisi' olup olmadığını denetlemek için kullanılır.
a = "123"
print(a.isdigit()) #True

a = "123a"
print(a.isdigit()) #False


#######################
### isalnum() metodu bir karakter dizisinin ‘alfanümerik’ olup olmadığını denetlememizi sağlar.(sayı ve/veya harflerden oluşan karakter dizilerine alfanümerik karakter dizileri adı verilir)
a = "123abc"
print(a.isalnum()) #True

a = "123abc."
print(a.isalnum()) #False

###
print("12345".isdigit())    # True
print("123.45".isdigit())   # False (nokta rakam değil)
print("12 34".isdigit())    # False (boşluk rakam değil)

# isalpha — sadece harf mi?
print("Python".isalpha())   # True
print("Python3".isalpha())  # False

# isalnum — harf veya rakam mı?
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False (boşluk)

# isspace — sadece boşluk karakteri mi?
print("   ".isspace())      # True
print(" \t\n".isspace())    # True


#######################
### isdecimal() metodu bir karakter dizisinin ondalık sayı cinsinden olup olmadığını denetlemek için kullanılır.
a = "123"
print(a.isdecimal()) #True

a = "2.5"
print(a.isdecimal()) #False


#######################
### isidentifier() metodu, neyin tanımlayıcı olup neyin tanımlayıcı olamayacağını denetlememizi sağlar.(python’da değişkenler, fonksiyon ve modül adlarına ‘tanımlayıcı’ denir)
#1a = 12 #değişken adları sayı ile başlayamaz.
print("1a".isidentifier()) #False

a1 = 12
print("a1".isidentifier()) #True


#######################
### isnumeric() metodu bir karakter dizisinin nümerik olup olmadığını denetler. Yani bu metot yardımıyla bir karakter dizisinin sayı değerli olup olmadığını denetleyebiliriz.
print("12".isnumeric()) #True

print("dasd".isnumeric()) #False


#######################
### isspace() bu metot yardımıyla bir karakter dizisinin tamamen boşluklardan oluşup oluşmadığını denetleyebiliriz.
a = " "
print(a.isspace()) #True

a = "              "
print(a.isspace()) #True

a = "" #karakter dizimiz tamamen boş. içinde boşluk karakteri bile yok...
print(a.isspace()) #False

a = "fd"
print(a.isspace()) #False


#######################
### isprintable() metodu bir karakterin basılabilen bir karakter mi yoksa basılmayan bir karakter mi olduğunu sorgular.(ekranda görünmeyen karakterlere ‘basılmayan karakterler’ (non-printing characters) adı verilir. ‘b’, ‘c’, ‘z’, ‘x’, ‘=’, ‘?’, ‘!’ ve benzeri karakterler ise ‘basılabilen karakterler’ (printable characters) olarak adlandırılır)
karakter = "a"
print(karakter.isprintable()) #True

karakter = "\n"
print(karakter.isprintable()) #False