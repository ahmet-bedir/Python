# Not Uygulaması

# 1- Menu 
    # 1- Not Gir
    # 2- Ortalamaları Göster 
    # 3- Notları Kayıt Et
    # 4- Çıkış

    # 90-100 -> AA 
    # 80-89  -> BA 
    # 75-79  -> BB
    # 70-74  -> CB
    # 65-69  -> CC
    # 60-64  -> DC
    # 50-59  -> DD
    # 40-49  -> FD
    # 0 -39  -> FF
"""
# Fonksiyon kullanarak.

def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "CC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DC"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "DD"
    elif ortalama >= 40 and ortalama <= 49:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 39:
        harf = "FF"

    return f"{ogrenciAdi} : {harf} - ({ortalama})\n"
    

def not_gir():
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyad: ")
    not1 = input("not 1: ")
    not2 = input("not 2: ")
    not3 = input("not 3: ")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + ',' + not2 + ',' + not3+'\n')

def notlari_oku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))

def notlari_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir))

        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)

while True:
    islem = input("1-Not Gir\n2-Notları Oku\n3-Notları Kayıt Et\n4-Çıkış\nseçim: ")

    if islem == "1":
        not_gir()
    elif islem == "2":
        notlari_oku()
    elif islem == "3":
        notlari_kaydet()
    else:
        break
"""
###
while True:
    islem = input("=== MENÜ ===\n\
1-Not Gir\n\
2-Notları Oku\n\
3-Çıkış\n\
Seçiminiz : ")
    
    if islem == "1":
        ad = input("Öğrenci ismi: ")
        soyad = input("Öğrenci soyismi: ")
        not1 = input("1.Sınav notu: ")
        not2 = input("2.Sınav notu: ")
        not3 = input("3.Sınav notu: ")
        ortalama = (int(not1) + int(not2) + int(not3)) / 3
        
        if ortalama >= 90 and ortalama <= 100:
            harf = "AA"
        elif ortalama >= 80 and ortalama <= 89:
            harf = "BA"
        elif ortalama >= 75 and ortalama <= 79:
            harf = "BB"
        elif ortalama >= 70 and ortalama <= 74:
            harf = "CB"
        elif ortalama >= 65 and ortalama <= 69:
            harf = "CC"
        elif ortalama >= 60 and ortalama <= 64:
            harf = "DC"
        elif ortalama >= 50 and ortalama <= 59:
            harf = "DD"
        elif ortalama >= 40 and ortalama <= 49:
            harf = "FD"
        elif ortalama >= 0 and ortalama <= 39:
            harf = "FF"
        print(f"Ortalama : {ortalama} ({harf})")
        
        onay = input("Girilen Bilgiler Kayıt Edilsinmi? [E/H]: ")
        if onay == "e" or onay == "E":
            with open("notlar.txt","a") as dosya:
                ogrenci = f"{ad} {soyad} : {not1}, {not2}, {not3} => {ortalama} ({harf})"
                dosya.write(ogrenci + "\n")
            print("Kayıt İşlemi Yapılmıştır.")
        elif onay == "h" or onay == "H":
            print("Kayıt İşlemi İptal Edilmiştir!")
        else:
            print("Yalış Seçim!")
    
    elif islem == "2":
        with open("notlar.txt") as dosya:
            print(dosya.read())

    elif islem == "3":
        break

    else:
        print("Yalış Seçim!")
   
