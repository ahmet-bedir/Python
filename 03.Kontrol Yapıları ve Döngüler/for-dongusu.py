tr_harfler = "çÇğĞıİöÖşŞüÜ"

print("for döngüsü ile türkçe harfler.")
for harf in tr_harfler:
    print(harf, end='  ')
# Tanımladığımız tr_harfler değişkeni türkçeye özgü harfleri tutuyor. Daha sonra bir for döngüsü kurarak, tr_harfler adlı değişkenin her bir öğesini tek tek harf adlı değişkene atıp ekrana yazdırdık.


###
print("print fonksiyonu ile türkçe harfler.")
print(*tr_harfler, sep='  ')


### for döngüsü, üzerinde döngü kurulabilecek veri tiplerinin her bir öğesinin üzerinden tek tek geçer ve bu öğelerin her biri üzerinde bir işlem yapar. while döngüsü ise herhangi bir ifadenin bool değerini kontrol eder ve bu değerin bool değeri False olana kadar, belirlenen işlemi yapmayı sürdürür.
print("while döngüsü ile türkçe harfler.")
a = 0
while a < len(tr_harfler):
    print(tr_harfler[a], end='  ')
    a += 1


'''
sayilar = 123456789 #hata! çünkü sayılar üzerinde döngü kuramayız.
for sayi in sayilar:
    print(sayi)
'''
#Burada str_sayilar adlı değişkenin her bir öğesini bizim belirlediğimiz sayi adlı değişkenine aktardıkdan sonra, int() fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve her bir öğeyi 2 ile çarptık.
str_sayilar = "123456789"
for sayi in str_sayilar:
    print(int(sayi) * 2, end='  ')
print('\n', '-'*40, sep='')

#Burada int_sayilar adlı değişkeni önce stringe çevirip her bir öğesini bizim belirlediğimiz sayi adlı değişkenine aktardıkdan sonra, int() fonksiyonu yardımıyla bu öğeleri tek tek sayıya çevirdik ve her bir öğeyi 2 ile çarptık.
int_sayilar = 123456789
for sayi in str(int_sayilar):
    print(int(sayi) * 2, end='  ')
print('\n', '-'*40, sep='')
