#Öncelikle kullanıcıdan bir internet adresi girmesini istiyoruz
url = input("Lütfen ulaşmak istediğiniz sitenin adresini yazın : ")
#Şimdi de bu adresin bulunamadığı konusunda kullanıcıyı bilgilendiriyoruz
print("Hata! Google Chrome '{}' sitesini bulamadı".format(url))


###
kelime = "xml"
mesaj = "Aradığınız kelime '{}' bulunamamıştır..."
print(mesaj.format(kelime))

###
print("{1} ve {0} iyi bir ikilidir...".format("C#","Java"))

###
tc = "55567922448" #input("T.C No : ")
isim = "Ahmet" #input("İsim : ")
soyisim = "Bedir" #input("Soyisim : ")
tel = "0262 225 45 34" #input("Telefon : ")

bilgiler = """
T.C No  : {}
İsim    : {}
Soyisim : {}
Telefon : {}
"""
print(bilgiler.format(tc,isim,soyisim,tel))

###
isim = "Ali"
soyisim = "Pak"
yas = 34
print("İsim {ad}, Soyisim {sad}, Yaş {y}".format(ad=isim,sad=soyisim,y=yas))
print("İsim {y}, Soyisim {ad}, Yaş {sad}".format(ad=isim,sad=soyisim,y=yas))


###
sayi = 7.2857142857142857
print("Sonuç : {s}".format(s=sayi))
print("Sonuç : {s:0.4}".format(s=sayi))
