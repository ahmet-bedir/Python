# keys() metodu bir sözlüğün sadece anahtarlarını almak için kullanılır.
sozluk = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sozluk.keys())
print(list(sozluk.keys()))
print(tuple(sozluk.keys()))
print(''.join(sozluk.keys()))
print(str(sozluk.keys()), end='\n\n')

# values() metodu bir sözlüğün sadece değerlerini almak için kullanılır.
print(sozluk.values())
print(list(sozluk.values()))
print(tuple(sozluk.values()))
print(''.join([str(i) for i in sozluk.values()]))
print(str(sozluk.values()), end='\n\n')

# items() metodu, bir sözlüğün hem anahtarlarını hem de değerlerini aynı anda almamızı sağlar:
print(sozluk.items())

#
for anahtar, deger in sozluk.items():
    print("{} = {}".format(anahtar, deger))
    
print('\n')

# get() metodu sözlükte kelime sorgulama için kullanılır.
ing_sozluk = {
    "dil"       : "language",
    "bilgisayar": "computer",
    "masa"      : "table"}

sorgu = input("Lütfen anlamını öğrenmek istediğiniz kelimeyi yazınız : ")

print(ing_sozluk.get(sorgu, "Bu kelime veritabanımızda yoktur!"), end='\n\n')

# clear() metodunun görevi sözlükteki öğeleri temizlemektir.
print(ing_sozluk)
ing_sozluk.clear()
print(ing_sozluk)

#
del ing_sozluk #bir sözlüğü bellekten tamamen kaldırmak için del kullanıyoruz.
#print(ing_sozluk)


#
sozluk = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

kopya_sozluk = sozluk #Varolan bir sözlüğü başka bir değişkene atadığımızda aslında yaptığımız şey bir kopyalama işleminden ziyade bellekteki aynı nesneye gönderme yapan iki farklı isim belirlemekten ibaret.

print(sozluk)
print(kopya_sozluk)

kopya_sozluk["d"] = 4 #kopya_sozluk adlı sözlüğe yaptığımız ekleme sozluk adlı sözlüğü de etkiledi. Eğer bunu istemiyorsak sözlüklerin copy() adlı metodu kullanılmalı.

print(sozluk)
print(kopya_sozluk)

# copy()
sozluk = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

kopya_sozluk = sozluk.copy()

print(sozluk)
print(kopya_sozluk)

kopya_sozluk["d"] = 4 #Gördüğünüz gibi kopya_sozluk adlı sözlüğe yaptığımız ekleme sozluk adlı sözlüğü etkilemedi.

print(sozluk)
print(kopya_sozluk)


# fromkeys()’in görevi listeler veya demetlerden yararlanarak yeni bir sözlük oluşturmaktır.
# fromkeys()’in görevi listeler veya demetlerden yararlanarak yeni bir sözlük oluşturmaktır.
elemanlar = "Ahmet", "Mehmet", "Can"
elemanlar = ["Ahmet", "Mehmet", "Can"]
elemanlar = "Ahmet Mehmet Can"

adresler = dict.fromkeys(elemanlar, "Kadıköy")

print(adresler)


# pop() metodu sözlükte belirlediğimiz anahtarın değerini silerek ve sildiği bu öğenin değerini ekrana basacaktır.
sepet = {
    "meyveler": ("elma", "armut"),
    "sebzeler": ("pırasa", "fasulye"),
    "içecekler": ("su", "kola", "ayran")}

print(sepet.pop("meyveler"))

#print(sepet.pop("mey")) #hata! Eğer silmeye çalıştığımız anahtar sözlükte yoksa Python bize bir hata mesajı gösterecektir.
print(sepet.pop("mey","Silinecek öğe sözlükte bulunmamaktadır!"))


### update() buu metot yardımıyla oluşturduğumuz sözlükleri yeni verilerle güncelleyeceğiz.

stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}

yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}

stok.update(yeni_stok)
print(stok)
