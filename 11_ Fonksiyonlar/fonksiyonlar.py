### orn1
def kayit(isim="",soyisim="",sistem="",sehir=""): #varsayılan değerli parametreler.
	print("-"*30)
	print("İsim\t\t:", isim)
	print("Soyisim\t\t:", soyisim)
	print("İşletim Sistemi\t:", sistem)
	print("Şehir\t\t:", sehir)
	print("-"*30)

kayit("ahmet","bedir","linux","kocaeli") #Sıralı veya isimsiz parametreler.
kayit("ali","koz","windows")
kayit("unix","istanbul","ersin","şeker") #Eğer fonksiyon parametrelerini bu sırayla kullanırsak aldığımız çıktı hatalı olacaktır.

kayit(sehir="muş",isim="canan",soyisim="alık",sistem="unix") #İsimli parametreler.
kayit(sistem="dos",isim="can",soyisim="saka")
"""
Python’da isimli bir parametrenin ardından sıralı bir parametre gelemez.
"""
#kayit(soyisim="Öz", isim="Ahmet", "Debian", "Ankara")


print("#"*40)
### orn2
def sistem_bilgisi():
	import sys
	print("\nSistemde kurulu Python'ın;")
	print("\tana sürüm numarası:", sys.version_info.major)
	print("\talt sürüm numarası:", sys.version_info.minor)
	print("\tminik sürüm numarası:", sys.version_info.micro)
	print("\nKullanılan işletim sisteminin;")
	print("\tadı:", sys.platform)

sistem_bilgisi()


print("#"*40)
### orn3
def uzunluk(kelime):
	i = 0
	for harf in kelime:
		i += 1
	print(f"'{kelime}' uzunluğu: {i}")

kelime = "python"
uzunluk(kelime)
# diğer kodlar...
uzunluk("ali")
# diğer kodlar...
liste = ["bardak",'a',5,True]
uzunluk(liste)