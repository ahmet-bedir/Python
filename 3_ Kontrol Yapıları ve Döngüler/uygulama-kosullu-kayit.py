kullanici_adi = input("""
=== Kullanıcı Kayıt İşlemi ===
Kullanıcı Adı Belirleyiniz
>> """)
parola = input("""
Parola Belirleyiniz
>> """)
uzunluk = len(kullanici_adi) + len(parola)
mesaj = "Girmiş Olduğunuz Kullanıcı Adı ve Parola {} Karakter Uzunluğundadır."
print(mesaj.format(uzunluk))

if uzunluk > 20:
    print("Kullanıcı Adı ve Parola Uzunluğu Yirmi Karakteri Geçmemelidir!")
else:
    print("Kaydınız Oluşturulmuştur.")