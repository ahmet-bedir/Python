'''
if kullanici_adi == '':
if bool(kullanici_adi) == True:
if kullanici_adi:
Yukarıdaki üç kullanım şekilleri tamamen aynıdır...
'''
a = "=== Kullanıcı Girişi ==="
print('='*len(a), a, '='*len(a), sep='\n')

kullanici_adi = input("Kullanıcı Adı : ")
parola = input("Parola : ")

if kullanici_adi:
    if parola:
        if kullanici_adi == "user":
            if parola == "123":
                print("Kullanıcı Adınız ve Parolanız Doğru.")
            else:
                print("Parolanız Yanlış!")
        else:
            print("Kullanıcı Adınız Yanlış!")
    else:
        print("Parolanız Boş Bırakılamaz!")
else:
    print("Kullanıcı Adınız Boş Bırakılamaz!")