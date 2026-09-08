for i in range(3):
    print(str(i+1) + ". hakkınız")
    parola = input("Parola Belirleyin : ")
    if i == 2:
        print("""Parolayı 3 kez yanlış girdiniz.
Lütfen 30 dakika sonra tekrar deneyin!""")
    elif not parola:
        print("Parola Bölümü Boş Geçilemez!")
    elif len(parola) in range(3, 9):
        print("Yeni Parolanız : ", parola)
        break
    else:
        print("Parola 8 Karakterden Uzun, 3 Karakterden Kısa Olmamalı...")
