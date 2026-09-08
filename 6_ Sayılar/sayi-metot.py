### Tam Sayıların Metotları
metot = [i for i in dir(int) if not i.startswith("_")]
print(metot)

# bit_length() metodu herhangi bir tam sayının kaç bit’lik bir yer kapladığını öğrenmek için kullanılır.
for i in range(11):
    print(i, bin(i)[2:], str(len(bin(i)[2:])) + " bitlik.", sep="\t")
    
    
#
sayi = 10
print(f"{sayi} sayısı {sayi.bit_length()} bitlik bir yer kaplamaktadır.")

### Kayan Noktalı Sayıların Metotları
#as_integer_ratio() metodu, birbirine bölündüğünde ilgili kayan noktalı sayıyı veren iki adet tam sayı verir bize.
sayi = 4.5
print(sayi.as_integer_ratio()) #(9, 2)

#is_integer() bir kayan noktalı sayının ondalık kısmında 0 harici bir sayının olup olmadığını kontrol etmek için bu metodu kullanıyoruz.
print((12.0).is_integer()) #True

print((12.5).is_integer()) #False

###Karmaşık Sayıların Metotları
#imag imag adlı nitelik, bize bir karmaşık sayının sanal kısmını verir:

c = 12+4j
print(c.imag) #4.0

#real adlı nitelik bize bir karmaşık sayının gerçek kısmını verir:

c = 12+4j
print(c.real) #12.0