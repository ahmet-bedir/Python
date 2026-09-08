### Dosya içindeki, Girilen Karakteri Sayma
metin = open("/storage/emulated/0/Download/python-programlama/3.Döngüler/hikaye.txt",encoding="utf-8")

#for karakter_dizisi in metin:
	#print(karakter_dizisi)
	
harf = input("Sorgulamak istediğiniz harfi giriniz : ")
harf_sayisi = 0

for karakter_dizisi in metin:
	for karakter in karakter_dizisi:
		if karakter == harf:
			harf_sayisi += 1
	
	
print("'{}' harfi metinde {} kez geçiyor...".format(harf, harf_sayisi))

metin.close()

