"""
while <koşul>: koşul true olduğu müddetce döngü çalışır.
    <kodlar>   
"""
a = 1
while a <= 10: #a’nın değeri 10’dan küçük olduğu müddetçe döngü çalışmaya devam eder.
    print('Döngü {}.defa çalıştı...'.format(a))
    a += 1 #a'nın değerini bir arttırmazsak programlamı sonsuz döngüye (infinite loop) sokmuş oluruz.

########################################
tekrar = 1

while tekrar <= 3:
    print("tekrar değeri :", tekrar)
    tekrar += 1
    print("tekrar değerinin bool değeri :", bool(tekrar <= 3))
    input("Devam etmek için enter tuşuna basınız...")
    
"""
tekrar değeri : 1
tekrar değerinin bool değeri : True
Devam etmek için enter tuşuna basınız...
tekrar değeri : 2
tekrar değerinin bool değeri : True
Devam etmek için enter tuşuna basınız...
tekrar değeri : 3
tekrar değerinin bool değeri : False
Devam etmek için enter tuşuna basınız...
"""

########################################
#Klavyeden 'q' tuşuna basılmadığı müddetce işlemi tekrarlayan program.
menu = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme """
print(menu)

s1 = int(input("1.sayı : "))
s2 = int(input("2.sayı : "))

i = 1
while i == 1: #i bir olduğu sürece döngü sürekli çalışır.
    secim = input("""
Çıkış 'q'
işleminiz : """)
    if secim == "q": #Klavyeden 'q' tuşuna bastığımızda i'nin değerini bir arttırdık böylece döngüden çıkmış olduk.
        i += 1
    elif secim == "1":
        print("Toplama : ", s1+s2)
    elif secim == "2":
        print("Çıkarma : ", s1-s2)
    elif secim == "3":
        print("Çarpma : ", s1*s2)
    elif secim == "4":
        print("Bölme : ", s1/s2)
    else:
        print("Hatalı Giriş...")

########################################
#Klavyeden 'q' tuşuna basılmadığı müddetce işlemi tekrarlayan program.
menu = """
(1) Toplama
(2) Çıkarma
(3) Çarpma
(4) Bölme """
print(menu)

s1 = int(input("1.sayı : ")) 
s2 = int(input("2.sayı : "))

while True: #True olduğu sürece döngü sürekli çalışır.
    secim = input("""
Çıkış 'q'
İşleminiz : """)
    if secim == "q":
        break #Klavyeden 'q' tuşuna bastığımızda döngüden çıkar.
    elif secim == "1":
        print("Toplama : ", s1+s2)
    elif secim == "2":
        print("Çıkarma : ", s1-s2)
    elif secim == "3":
        print("Çarpma : ", s1*s2)
    elif secim == "4":
        print("Bölme : ", s1/s2)
    else:
        print("Hatalı Giriş...")

########################################
#1'den 20'e kadar olan tek ve çift sayılar...
a = 0
while a < 20:
    a += 1
    if a % 2 == 0:
        print("Çift :", a)
    else:
        print("Tek :", a)
