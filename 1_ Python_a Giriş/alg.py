##################################################
"""
Klavyeden girilen sayının karesini
hesaplayarak ekrana yazdıran programın
algoritması.
Başla
Sayıyı (A) gir
Sayının karesini hesapla (Kare = A*A işlemini yap)
Sonucu (Kare) yaz
Dur
"""

# sayi = int(input("Bir sayı girin: "))
# kare = sayi * sayi
# print("Girdiğiniz sayının karesi:", kare)

##################################################
"""
Verilen bir sıcaklık derecesine göre
suyun durumunu belirten bir sözde
program(pseudo kod).
1. Program açıklama mesajı yaz.
2. Kullanıcın sıcaklığı girmesi için bir uyarı mesajı yaz.
3. Girilen Sıcaklığı Oku.
5. Eğer Sıcaklık < 0 ise Durum=“Buz”
6. Eğer Sıcaklık>= 100 ise Durum=“Buhar”
7. Değilse Durum =“Su”
8. Sonucu Yaz.
"""

# print("Suyun durumunu belirlemek için sıcaklık derecesi girin.")
# sicaklik = float(input("Sıcaklık derecesi: "))
# if sicaklik < 0:
#     durum = "Buz"
# elif sicaklik >= 100:
#     durum = "Buhar"
# else:
#     durum = "Su"
# print("Suyun durumu:", durum)

###################################################
"""
Girilem A değişkeni ve B sabitini birleştirerek ekrana yazdıran programın algoritması.
Başla
A değişkenini gir
B sabitini tanımla (örneğin B="Merhaba")
A ve B'yi birleştir (C = A + " " + B)
C'yi ekrana yazdır
Dur
"""

# a = input("A değişkenini girin: ")
# b = "Merhaba"

# c = a + " " + b
# print(c)

#################################################
"""
1-5 arası sayıları ekrana yazdır.
Başla
i=1
i 5'ten küçük veya eşit olduğu sürece
i'yi ekrana yazdır
i'yi 1 artır (i = i + 1)
Dur
"""
# i = 1
# while i <= 5:
#     print(i)
#     i += 1

####################################################
"""
1 ile 10 arasındaki tek sayıların
toplamını hesaplayan programın algoritması.
Başla
top = 0
i = 1
i 10'dan küçük veya eşit olduğu sürece
Eğer i tek ise
i'yi ekrana yazdır
top'a i'yi ekle (top = top + i)
i'yi 1 artır (i = i + 1)
top'u ekrana yazdır
Dur
"""
# 2.yöntem

# top = 0
# i = 1

# while i < 11:
#     print(i)
#     top += i
#     i += 2

# print("Top:", top)
#####################################################
"""
Klavyeden girilen 5 sayısının ortalamasını bulan programın
algoritması.
1. Başla
2. top=0
3. S=0
4. Eğer S>4 ise git 9
5. S=S+1
6. Sayıyı (A) gir
7. top=top+A
8. Git 4
9. Ortalama=top/5
10. Yaz Ortalama
11. Dur
"""
# top = 0
# s = 0
# while s < 5:
#     s += 1
#     a = float(input("Sayıyı girin: "))
#     top += a
# ortalama = top / 5
# print("Ortalama:", ortalama)

#####################################################
"""
Klavyeden girilen N sayısının faktöriyelini hesaplayan
programın algoritmasını yazınız.
1. Başla
2. N sayısını gir
3. Fak=1
4. S=0
5. Eğer S>N ise git 9
6. S=S+1
7. Fak=Fak*S
8. Git 5
9. Yaz Fak
10. Dur
"""
n = int(input("N sayısını girin: "))
fak = 1
s = 0
while s < n:
    s += 1
    fak *= s
print("Faktöriyel:", fak)
