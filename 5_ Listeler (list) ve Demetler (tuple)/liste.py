### listeler değiştirilen (mutable) veri tipleridir.
liste = ["Python", 1, 2.5, [True,False]]
print(f"Liste : {liste}, Türü : {type(liste)}")

print(liste[0])
print(liste[1])
print(liste[2])
print(liste[3][0])
print(liste[3][1])
print(liste[-1])
print(liste[0:2])
print(liste[::-1])
print(liste[4]) #hata! liste 4 elemanlı bir liste, biz olmayan elemanı yazdıramayız.

yeni_liste = liste[3]
print(yeni_liste[0])
print(yeni_liste[1])

for i in range(len(liste)):
    print("{} -> {}".format(i+1,liste[i]))
    
for i, eleman in enumerate(liste,1):
    print(f"Listenin {i}. elemanı : '{eleman}' türü : {type(eleman)}")

print("Eleman Sayısı :", len(liste))
print("Kullanabileceğimiz metodlar :\n", dir(list), "\n", type(dir([])), sep='')

bldy = "İzmit Büyükşehir Belediyesi"
print(bldy, type(bldy))
s_bldy = bldy.split()
print(s_bldy, type(s_bldy))

##
sayilar = [[0, 10], [6, 60], [12, 54], [67, 99]]
for i in sayilar:
    print(*range(i[0],i[1])) #print(*range(*i))

## list fonksiyonu.
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
liste = list(alfabe)
print(liste)

## sıfırdan ikiyüze kadar olan sayılardan bir liste oluşturma.
liste = list(range(200))
print(liste)


### listeyi güncelleme.
liste = ["Python", 1, 2.5, [True,False]]
liste[1] = "Php"
print("Listenin 2.elemanı 'Php' ile değiştirildi.")
print(liste)

###
liste = [1, 2, 3]
print(liste)
liste[0:len(liste)] = 5, 6, 7 #liste[:] = 5, 6, 7
print(liste)

### listeye eleman ekleme.
liste += [False, 'A', "Ali", 2]
print("Listeye 4 eleman daha eklendi.")
print(liste)

### listeleri birleştirme.
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller + yorumlanan_diller
print(programlama_dilleri)

#Kullanıcı tarafından girilen beş adet sayının ortalamasını hesaplayan program.
sayilar = 0
for i in range(5):
    sayilar += int(input("{}.sayı : ".format(i+1)))

print("Ortalama :", sayilar/5)

#Kullanıcı tarafından girilen beş adet sayıyı listeye ekleyip ortalamasını hesaplayan program.
sayilar = []
toplam = 0
for i in range(5):
    sayi = int(input(f"{i+1}.sayı : "))
    sayilar += [sayi]
print('#'*25)  
for i in range(5):
    print(f"{i+1}.sayı : {sayilar[i]}")
    toplam += sayilar[i]

print("Ortalama :", toplam/5)

#Kullanıcı tarafından sınırsız girilen sayıların ortalamasını hesaplayan program.
sayilar = list()
toplam = 0
while True:
    sayi = input("Sayı (çıkış 'q') : ")
    if sayi == "q":
        break
    sayilar += [sayi]
print('#'*25)
for i,sayi in enumerate(sayilar,1):
    toplam += int(sayi)
    print(f"{i}.sayı : {sayi}")

print("Ortalama :", toplam/len(sayilar))

#
liste = []
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
for harf in alfabe:
    liste += harf

print(liste)

#
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
liste = list(alfabe)
print(liste)

#
sayi = 12345 #hata!
liste = list(sayi)
print(liste)

# listeden eleman silme.
del liste[0]
print("Listenin ilk elemanı silindi.")
print(liste)

# listeyi silme.
liste = [1, 5, 3, 2, 9]
print(liste)
del liste
print(liste)

# listeyi kopyalama.
liste = ['a','b','c']
print(liste)
liste2 = liste
print(liste2)

liste[0] = 1
print(liste)
print(liste2)
#liste ve liste2 adlı listeler aynı kimlik numarasına sahip. Yani bu iki nesne birbiriyle aynı. Dolayısıyla birinde yaptığınız değişiklik öbürünü de etkiler. 
print(id(liste) == id(liste2)) #True

#
liste = ['a','b','c']
print(liste)
liste2 = liste[:]
print(liste2)

liste[0] = 1
print(liste)
print(liste2)

print(id(liste) == id(liste2)) #False

#
liste = ['a','b','c']
print(liste)
liste2 = list(liste)
print(liste2)

liste[0] = 1
print(liste)
print(liste2)

print(id(liste) == id(liste2)) #False

# listede eleman arama.
eleman = "Python"
varMi = eleman in liste
if varMi:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmaktadır.")
else:
    print(f"Liste içerisinde '{eleman}' elemanı bulunmamaktadır!")
    
### Liste Üreteçleri (List Comprehensions)
liste = []
for i in range(1000):
    liste += [i]
print(liste)

liste = [i for i in range(1000)] #Burada 0’dan 1000’e kadar olan sayıları tek satırda bir liste haline getirdik.
print(liste)

#
liste = [i for i in range(1000) if i % 2 == 0]
print(liste)

#Burada iç içe geçmiş 4 adet liste var. Bu listenin bütün öğelerini tek bir listeye alma.
liste = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12]]
tumu = []
for i in liste:
    for z in i:
        tumu += [z]
print(tumu)

#liste üretecleri ile.
tumu = [z for i in liste for z in i]
print(tumu)

#Burada amacınız liste1 içinde yer alan iç içe geçmiş listelerden hangisinin liste2 içindeki sayıların alt kümesi olduğunu, yani liste2 içindeki sayıların, liste1 içindeki üçlü listelerden hangisiyle birebir eşleştiğini bulmak.
liste1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15],
          [16, 17, 18],
          [19, 20, 21],
          [22, 23, 24],
          [25, 26, 27],
          [28, 29, 30],
          [31, 32, 33]]
          
liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33,
          22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44,
          59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51,
          89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71,
          16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20,
          33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78,
          34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64,
          26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35,
          72, 38, 100, 52, 16, 49, 79]

for i in liste1:
    for z in i:
        if z in liste2:
            print(z)
            
#liste üreteçleri ile.
for i in liste1:
    ortak = [z for z in i if z in liste2]
    if len(ortak) == len(i):
        print(i)