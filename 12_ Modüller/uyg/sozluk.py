# Bulunduğumuz dizinde bulunan kendimizin oluşturduğu "sozluk" modülünü içe aktarıyoruz.
import sozluk_modulu as sozluk

print(dir(sozluk))
#print(sozluk.__file__) #buradan aldığımız çıktı bize "sozluk_modulu" modülünün kaynak dosyasının nerede olduğunu gösterir.

while True:
    menu = """
=== MENÜ ===
1.Ekle
2.Ara
3.Sil
4.Sözlüğü Görüntüle
5.Çıkış
Seçiminiz : """
    giris = input(menu)
    if giris == '5':
        break
    elif giris == '4':
        sozluk = sozluk.sozluk
        print('+', '-'*15, '+', '-'*15, '+', sep='')
        print("|{:^15}|{:^15}|".format("Türkçe", "İngilizce"))
        print('+', '-'*15, '+', '-'*15, '+', sep='')
        for anahtar, deger in sozluk.items():
            print("|{:<15}|{:<15}|".format(anahtar, deger))
            print('+', '-'*15, '+', '-'*15, '+', sep='')
    elif giris == '3':
        sil = input("Silinecek Kelime : ")
        sozluk.sil(sil)
    elif giris == '2':
        bul = input("Aranacak Kelime : ")
        print(sozluk.ara(bul))
    elif giris == '1':
        kelime = input("Yeni Kelime : ")
        ing_anlam = input("Kelimenin İngilizce Karşılığı : ")
        sozluk.ekle(kelime, ing_anlam)
    else:
        print("Hatalı giriş!")