tr_harfler = "çÇğĞıİöÖşŞüÜ"
while True:
    parola = input("Parola Belirleyiniz (çıkış 'q') : ")
    
    for harf in parola:
        if harf in tr_harfler:
            print("Parolanızda Türkçe Karakter Kullanamazsınız!")
            break
    else:
        if parola == 'q':
            print("Programdan Çıkılıyor...")
            break
        elif not parola:
                print("Parola Bölümü Boş Olmamalıdır!")
        elif ' ' in parola:
                print("Parolanızda Boşluk Karakteri Kullanamazsınız!")
        elif len(parola) not in range(3,8):
            print("Parolanız Üç Karakterden Kısa, Yedi Karakterden Uzun  Olmamalıdır!")
        else:
            print("""Parolanız Başarılı Bir Şekilde Oluşturulmuştur.
Parolanız :""", parola)
            break
        