menu = """
=== Hesap Makinesi ===
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme
(5) Karesini hesapla
(6) Karekökünü hesapla
"""
print(menu)

while True:
    giris = input("""
Programdan Çıkmak İçin 'q' Tuşuna Basınız...
İşlem Türü Seçiniz : """)
    if giris == '1' or giris == '2' or giris == '3' or giris == '4':
        s1 = int(input("1.Sayı : "))
        s2 = int(input("2.Sayı : "))
        if giris == '1':
            sonuc = s1 + s2
            print("{} + {} : {}".format(s1,s2,sonuc))
        elif giris == '2':
            sonuc = s1 - s2
            print("{} - {} : {}".format(s1,s2,sonuc))
        elif giris == '3':
            sonuc = s1 * s2
            print("{} * {} : {}".format(s1,s2,sonuc))
        elif giris == '4':
            sonuc = s1 / s2
            print("{} / {} : {}".format(s1,s2,sonuc))
    elif giris == '5':
        s1 = int(input("Karesini hesaplamak istediğiniz sayıyı girin : "))
        sonuc = s1 ** 2
        print("'{}' Sayısının Karesi : {}".format(s1,sonuc))
    elif giris == '6':
        s1 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin : "))
        sonuc = s1 ** 0.5
        print("'{}' Sayısının Karekökü : {}".format(s1,sonuc))
    elif giris == 'q':
        break
    else:
        print("Geçersiz Giriş! ")
        print("Aşağıdaki Seçeneklerden Birini Giriniz:", menu)




