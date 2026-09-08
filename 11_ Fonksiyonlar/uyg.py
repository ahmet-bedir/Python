# Rastgele Sayıda İsimsiz Parametre Belirleme.
def toplama(*sayilar):
	toplam = 0
	for sayi in sayilar:
		toplam += sayi
	print("Toplam :", toplam)

toplama(1,2,3)

toplama(2,2,2,4)

# Rastgele Sayıda İsimli Parametre Belirleme.
def fonksiyon(**parametreler):
    print(parametreler)

fonksiyon(isim="Ahmet", soyisim="Öz", meslek="Mühendis", şehir="Ankara")

##
def kayit(**bilgiler):
	print("-"*30)
	for anahtar, deger in bilgiler.items():
	    print("{:<10} : {}".format(anahtar, deger))
	print("-"*30)

kayit(Ad="Fırat", Soyad="Özgül", Şehir="İstanbul", Tel="533 321 3232")