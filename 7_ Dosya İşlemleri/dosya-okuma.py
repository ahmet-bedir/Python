"""
    Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
    
    Kullanımı           : open(dosya_adi,dosya_erisme_modu)
    dosya_erisme_modu   : dosyayı hangi amaçla açtığımızı belirtir.
    "r" okuma modu      : okuma modu. belirtilen konumda dosya olmalıdır.
    seek                : cursor konumu

    Python’da bir dosyayı “r” kipinde açtığımızda o adda bir dosya olmalıdır, eğer o adda bir dosya yoksa hata alırız. Bir dosyayı okumak için read(), readline() ve readlines() adlı üç farklı metot kullanılır.
    
    encoding parametresi bir dosyanın hangi kod çözücü ile açılacağını belirtmemizi sağlar.

"""
###
f = open("log.txt","r",encoding="utf-8")

r = f.read() #Dosyanın tüm içeriğini okur.

print("Tip:", type(r)) #Tip: <class 'str'>
print(r)

f.close()


###
f = open("./log.txt","r")

r = f.readline() #Dosyayı satır satır okur.

print("Tip:", type(r)) #Tip: <class 'str'>
print(r)

r = f.readline()
print(r)

f.close()


###
f = open("log.txt") #Bir dosyayı okuma modunda açacaksanız "r" modunu belirtmeniz gerekmez.

r = f.readlines() #Dosyanın içedriği liste şeklinde okur.

print("Tip:", type(r)) #Tip: <class 'list'>
print(r) #['birinci satır\n', 'ikinci satır\n', 'üçüncü satır\n', 'dördüncü satır']

for satir in r:
    print(satir, end='')
    
f.close()


### Dosyayı otomatik olarak kapatır.
with open("log.txt") as file:
    print(file.read())

print(f.closed) #True (dosyanın kapatılma durumunu sorgular)

###Dosyayı İleri-Geri Sarmak
with open("log.txt") as file:
    print(file.read())

    file.seek(0) #Bu metoda verdiğimiz parametre, dosya içinde kaçıncı bayt konumuna gideceğimizi gösteriyor. Biz burada 0 sayısını kullanarak dosyanın ilk baytına, yani en başına dönmüş olduk.

    for i in file.read():
        print(i, end='')


#
with open("log.txt") as file:
    print(file.read())
    
    print(file.tell()) #Eğer o anda dosyanın hangi bayt konumunda bulunduğunuzu öğrenmek için.
    
    file.seek(5)
    print(file.tell())
    
    for i in file.read():
        print(i, end='')
        
    print(file.tell())
    
#
import locale
print(dir(locale))
print(locale.getpreferredencoding()) #dosyaların varsayılan olarak hangi kod çözücü ile açılacağını öğrenmek için kullanılır.