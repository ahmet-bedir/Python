###
liste_metod = [i for i in dir([]) if '_' not in i]
print(*liste_metod)

#append() metodunu, bir listeye öğe eklemek için kullanıyoruz.
liste = ["elma", "armut", "çilek"]
liste.append("erik") #append() metodu orijinal liste üzerinde doğrudan değişiklik yapmamıza izin veriyor.
print(liste)

#
liste = ["elma", "armut", "çilek"]
liste = liste + ["erik"] #artı işlecini kullandığımızda ise, orijinal listeyi değiştirmek yerine yeni bir liste oluşturuyoruz.
print(liste)

###
isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
hepsi = isletim_sistemleri + platformlar
print(hepsi)

#
isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]

for platform in platformlar:
isletim_sistemleri.append(platform)

print(isletim_sistemleri)

###
liste = [1, 2, 3]
#liste.append(1,2,3) #hata!
for i in [4, 5, 6]:
liste.append(i)

print(liste)

#kullanıcının girdiği bütün sayıları birbiriyle çarpan bir uygulama.
toplam = 1
liste = []
while True:
giris = input("Sayı (çıkış 'q') : ")
if giris == 'q':
break
liste.append(giris)
toplam *= int(giris)

if len(liste) < 2:
print("En az iki sayı girilmeli!")
else :
print("Toplam :", toplam)


### extend() metodu listeleri genişletmek için kullanıyoruz.
li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1.append(li2) #append() metodu bir listeye her defasında sadece tek bir öğe eklenmesine izin verir.
print(li1) #[1, 3, 4, [10, 11, 12]]

li1 = [1, 3, 4]
li2 = [10, 11, 12]
li1.extend(li2) #extend() metodu tam da kelime anlamına uygun olarak listeyi yeni öğelerle genişletti.
print(li1) #[1, 3, 4, 10, 11, 12]

#
isletim_sistemleri = ["Windows", "GNU/Linux", "Mac OS X"]
platformlar = ["IPhone", "Android", "S60"]
isletim_sistemleri.extend(platformlar)
print(isletim_sistemleri)

### insert() metodu, öğeleri listenin istediğimiz bir konumuna yerleştirir.
liste = ["elma", "armut", "çilek"]
liste.insert(0, "erik")
print(liste)

### remove() metodu listeden öğe silmemizi sağlar.
liste = ["elma", "armut", "çilek"]
liste.remove("armut")
print(liste)

### reverse() metodu liste öğelerini ters çevirmek için kullanılır.
meyveler = ["elma", "armut", "çilek", "kiraz"]
print(meyveler[::-1]) #dilimleme yöntemi ile listeyi ters çevirme.

#reversed() metodu ile listeyi ters çevirme.
print(*reversed(meyveler))
#veya
print(list(reversed(meyveler)))
#yada
for meyve in reversed(meyveler):
print(meyve)

## listelerin reverse() metodu ile listeyi ters çevirme.
meyveler.reverse()
print(meyveler)

### pop() tıpkı remove() metodu gibi, bu metot da bir listeden öğe silmemizi sağlar.
liste = ["elma", "armut", "çilek"]
print("Listenin orjinal hali")
print(liste)

silinen = liste.pop()
print("Silinen eleman:", silinen)
print(liste)

silinen = liste.pop(0)
print("Silinen eleman:", silinen)
print(liste)

### sort() metodu bir listenin öğelerini belli bir ölçüte göre sıraya dizmemizi sağlar.
uyeler = ['Ahmet', 'Mehmet', 'Ceylan', 'Seyhan', 'Mahmut', 'Zeynep',
    'Abdullah', 'Kadir', 'Kemal','Kamil', 'Selin', 'Senem', 'Sinem', 'Tayfun', 'Tuna','Tolga']
uyeler.sort()
print(uyeler)

#
sayilar = [1, 0, -1, 4, 10, 3, 6]
sayilar.sort(reverse = True)
print(sayilar)

##
isimler = ["samet", "ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]

isimler.sort()
print(isimler)

#türkçe karakterleri düzgün sıralayabilmemiz için.
harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
cevrim = {
    harf: harfler.index(harf) for harf in harfler
}


isimler = ["samet", "ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]

isimler.sort(key = lambda x: cevrim.get(x[0]))
print(isimler)

### index() metodu bir liste öğesinin liste içindeki konumunu öğrenmek için kullanılır.
liste = ["elma", "armut", "çilek"]
print(liste.index("elma"))

### count() metodu bir öğenin o veri tipi içinde kaç kez geçtiğini söyler.
print(liste.count("armut"))

### copy() metodu liste kopyalamak için kullanılır.
liste2 = liste.copy()
print(liste2)
liste[0] = "ayva"
print(liste)
print(liste2)

### clear() metodunun görevi bir listenin içeriğini boşaltmaktır.
liste2.clear()
print(liste2)

### Demetlerin Metodları.
# index() metodu bir demet öğesinin demet içindeki konumunu söyler bize.
demet = ("elma", "armut", "çilek")
print(demet.index("elma")) #0

#count() metodu da bir öğenin o veri tipi içinde kaç kez geçtiğini söyler.
demet = ("elma", "armut", "elma", "çilek")
print(demet.count("elma")) #2