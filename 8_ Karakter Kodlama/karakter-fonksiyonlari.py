### Python programlama dilinde nesneler iki farklı şekilde temsil edilir:
#1.Python’ın göreceği şekilde
#2.Kullanıcının göreceği şekilde
### repr() fonsiyonuda pythonun bakış açısını yansıtır.
print("Python\n")

print(repr("Python\n"))


a = "elma "

print("{} kilo {} kaldı!".format(13,a)) #Gördüğünüz gibi, “elma” karakter dizisinin sol tarafında bir boşluk olduğu için ‘elma’ ile ‘kaldı’ kelimeleri arasında gereksiz bir açıklık meydana geldi. Bu boşluğu print() ile göremiyoruz, ama bu değişkeni repr() fonsiyonu ile kontol edebiliriz:
print(repr(a))
print("{} kilo {} kaldı!".format(13,a.strip()))

print('-'*47)
### ascii() fonksiyonu karakterlerin UNICODE kod konumlarını (code points) gösterir.
print(ascii('İ')) #'\u0130'

print(repr('İ')) #'İ' (Gördüğünüz gibi repr() fonksiyonu ASCII tablosunda yer almayan karakterleri de göründükleri gibi temsil ediyor.)

#ascii() fonksiyonunun UNICODE kod konumlarını gösterme özelliğinin bir benzerini, encode() metodu yardımıyla da elde edebilirsiniz:
print("€".encode("unicode_escape")) #b'\\u20ac'
print(ascii('€')) #'\u20ac'


print('-'*47)
### ord() fonksiyonu bir karakterin Unicode kod noktasını, yani decimal karşılığını verir:

print(ord("\n")) #10
print(ord('€')) #8364

k = "€"
print(k.encode("utf-8"))
print(int("e282ac",16))
print((14844588).bit_length(), "bit.")

##
karakterler = "a⁶⁷z/~@£Çç€°✓∆§π√•|"
for i in karakterler:
    a = i.encode("utf-8")
    print(f"'{i}' karakteri {ord(i)} sayısı ile temsil edilmektedir, {len(a)} bayt uzunluğundadır.")


##
print('ç'.encode("utf-8")) #b'\xc3\xa7'
print(int('c3a7',16)) #50087
print((50087).bit_length()) #16 bit

print(ord('ç')) #231


### chr() fonksiyonu bir sayının karakter karşılığını verir:
print(chr(231))

for i in range(800):
    print(f"{i} => {chr(i)}")
    
    
#Kullandığınız işletim sisteminde öntanımlı kod çözücünün hangisi olduğunu şu komutla bulabilirsiniz:
import locale
print(locale.getpreferredencoding())