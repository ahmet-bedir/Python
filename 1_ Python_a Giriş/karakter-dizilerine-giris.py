print('-' * 30)
#karakter dizilerini birleştirme işlemi.
print("www" + ".google." + "com") #www.google.com
print("www" "." "google" "." "com") #www.google.com
print("www",".","google",".","com") #www . google . com

#print("sınav notu : " + 5) #hata! str ve int veri türlerini normal bir şekilde  birleştiremeyiz...
print("sınav notu : " + str(75)) #sınav notu : 75

print('-' * 30)

print(type(""), type(" ")) #<class 'str'> <class 'str'>
metin = "ahmet"
print(type(metin), type("&+$2")) #<class 'str'> <class 'str'>
print(type(123), type("123")) #<class 'int'> <class 'str'>

print('-' * 30)

print(2 + 3) #5
print("2" + "3") #23
print(2 * 3) #6
print("2" * 3) #222 (tekrarlama)
#print("2" + 3) #hata! str ve int veri türlerini toplayamayız.

print("-" * 30)

print(len("123")) #3
#print(len(123)) #hata! len fonksiyonu int türüyle kullanılamaz...
print(len(str(123))) #3
print(type(len("123"))) #<class 'int'>

print("-" * 30)

kullanici_adi = "ahmet-bedir41"
parola = "#5jF*79n:b"
print('Kullanıcı Adı : ' + kullanici_adi)
print("Parola : " + parola)
print("Toplam Uzunluk :", 
len(kullanici_adi) +
len(parola))

print("-" * 30)