'''
range() fonksiyonu belli bir aralıkta bulunan sayıları göstermek için kullanılır.
range(ilk_sayı, son_sayı, atlama_degeri)
'''
for i in range(0, 11):
    print(i, end=' ')  # 0'dan 11'e kadar olan sayılar.(0 dahil, 11 hariç)
print('\n')
for i in range(11):  # 0'dan 11'e kadar
    print(i, end=' ')
print('\n')    
for i in range(3, 11):  # 3'den 11'e kadar
    print(i, end=' ')
print('\n')
for i in range(0, 11, 2):  # 0'dan 11'e kadar iki atlamalı
    print(i, end=' ')
print("\n")
for i in range(10, 0, -1):  # sayıları tersten sıralar
    print(i, end=' ')
print('\n')

print(*range(10), sep=' ')

###
giris = input("Giriş : ")

if len(giris) in range(0,6):
	print("Girilen Sayı 0 ile 5 Arasında.")
elif len(giris) in range(5,11):
	print("Girilen Sayı 5 ile 10 Arasında.")
else:
	print("Girilen Sayı 10'dan Uzundur.")

'''
pass deyimi ‘geçmek, pas geçmek’ gibi anlamlarda kullanılır.
break deyimi devam eden bir süreci kesintiye uğratmak yani bir döngüyü sona erdirmek için kullanılır.
'''
###
while True:
    parola = input("Parola Belirleyin : ")
    if not parola:
        pass
    elif len(parola) in range(3, 9):
        print("Yeni Parolanız :", parola)
        break
    else:
        print("Parola 8 Karakterden Uzun, 3 Karakterden Kısa Olmamalı...")

###
while True:
    sayı = int(input("Bir Sayı Girin (çıkış '0') : "))
    if sayı == 0:
        break
    elif sayı < 0:
        pass
    else:
        print(sayı)

# continue deyiminin görevi kendisinden sonra gelen her şeyin es geçilip döngünün başına dönülmesini sağlamaktır. 
while True:
    s = input("Bir Sayı Girin (çıkış 'q') : ")
    print ("Sayı :", s)
    if s == "q":
        break
    if len(s) <= 3:
        continue
    print("En Fazla Üç Haneli Bir Sayı Girebilirsiniz.")
      
# else deyimi döngüler ile birlikte kullanılırken break deyimi ile birlikte bir anlam kazanır. Eğer döngü break ifadesi kullanılarak sonlandırıldı ise else çalışmaz, döngü break ifadesi ile sonlandırılmadı ise else bölümü çalışır.
###
for i in range(3):
    print(i)
else:
    print("else çalıştı.")
    
###
for i in range(5):
    if i == 3:
        break
else:
    print("else çalıştı.")
    
###
a = 0
while True:
    a += 1
    print(a)
    if a==3:
        break
else:
        print("else çalıştı.")

### if bloğuna else ekleyip a harfi bulunamadı mesajı vermiş olsaydık karakter dizisindeki a harfine gelinceye kadar ekrana 'a harfi bulunamadı.' çıktısı verip, a harfini bulduğunda ise 'a harfi bulundu.' çıktısı verecekti.
karater_dizisi = "Merhaba dünya"
for harf in karater_dizisi: # karater_dizisi değişkenindeki her bir harfi harf değişkenine attık.
    if harf == 'a':
        print("a harfi bulundu.")
        break
else:
    print("a harfi bulunamadı.")

###
rakamlar = "0123456789"
giris = input("Giriş Yapınız : ")
for i in giris:
    if i not in rakamlar:
        print("Sayı Değerli Değil...")
        break
else:
	print("Sayı Değerli...")