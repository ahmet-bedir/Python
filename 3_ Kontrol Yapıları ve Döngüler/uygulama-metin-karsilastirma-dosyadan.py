### Dosyaların İçeriğini Karşılaştırma.
dosya1 = open("/sdcard/Download/python-programlama/3.Döngüler/isimler1.txt") # dosyayı açıyoruz
d1_satirlar = dosya1.readlines() # satırları okuyoruz

dosya2 = open("/sdcard/Download/python-programlama/3.Döngüler/isimler2.txt")
d2_satirlar = dosya2.readlines()

#for i in d1_satirlar:
#    print(i)

for i in d2_satirlar:
    if not i in d1_satirlar:
        print(i)
    
dosya1.close()
dosya2.close()