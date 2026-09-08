kelimeler = {
    "kitap"      : "book",
    "bilgisayar" : "computer",
    "programlama": "programming",
    "dil"        : "language",
    "defter"     : "notebook"
}

print(type(kelimeler))
print(len(kelimeler))

print('\n')
# Sözlük Öğelerine Erişme
print(kelimeler["kitap"])

for i in kelimeler:
    print(kelimeler[i])

print("\n")
#
sozluk = {
    "Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],
    "Mehmet Yağız"   : ["Adana", "Mühendis", 40],
    "Seda Bayrak"    : ["İskenderun", "Doktor", 30]
}
print(f"Memleket : {sozluk["Seda Bayrak"][0]}\nMeslek : {sozluk["Seda Bayrak"][1]}\nYaş : {sozluk["Seda Bayrak"][2]}")

print('\n')
#
kisiler = {
    "Ahmet Özkoparan": {
        "Memleket": "İstanbul",
        "Meslek"  : "Öğretmen",
        "Yaş"     : 34
    },
    "Mehmet Yağız"   : {
        "Memleket": "Adana",
        "Meslek"  : "Mühendis",
        "Yaş"     : 40
    },
    "Seda Bayrak"    : {
        "Memleket": "İskenderun",
        "Meslek"  : "Doktor",
        "Yaş"     : 30
    }
}
print(f"Memleket : {kisiler["Ahmet Özkoparan"]["Memleket"]}\nMeslek : {kisiler["Ahmet Özkoparan"]["Meslek"]}\nYaş : {kisiler["Ahmet Özkoparan"]["Yaş"]}")

print("+-+"*48)
### Sözlüklere Öğe Eklemek
#Bir değerin ‘anahtar’ olabilmesi için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması gerekir. Python’da Demetler, Sayılar, Karakter Dizileri değiştirilemeyen veri tipleridir.
sozluk = {}
sozluk["a"] = 1
sozluk[2] = "b"
sozluk["liste"] = ['x','y','z']
sozluk["sözlük"] = {
    "ad" : "ahmet", 
    "soyad" : "bedir", 
    "yaş" : 35}
sozluk["a"] = True
sozluk[(1,2,3)] = 'd'
print(sozluk)

print("+-+"*48)
### Sözlük Öğeleri Üzerinde Değişiklik Yapmak
sozluk['a'] = 555
print(sozluk)

print("+-+"*48)
### Sözlük Üreteçleri (Dictionary Comprehensions)
harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
#
sozluk = {}
#for i in harfler:
    #sozluk[i] = harfler.index(i)
    
#print(sozluk)

#
#for i in range(len(harfler)):
    #sozluk[harfler[i]] = i
    
#print(sozluk)

#
sozluk = {i: harfler.index(i) for i in harfler}
print(sozluk)

#isim listesindeki isim ve kelime sayısını sözlük üreteçleri kullanarak yapmak.
isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
sozluk = {i:len(i) for i in isimler}
print(sozluk)

