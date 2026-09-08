###########################################################
ocak = mart = mayıs = temmuz = ağustos = ekim = aralık = 31
nisan = haziran = eylül = kasım = 30
şubat = 28

birimFiyat = 0.79

aylikSarfiyat = input("Aylık doğalgaz sarfiyatınızı metreküp olarak giriniz : ")

donem = input("""Hangi aya ait faturayı hesaplamak istersiniz?
(Lütfen ay adını tamamı küçük harf olacak şekilde giriniz)\n""")
ay = eval(donem) #ay değişkenine belirlenen ayların sayısal karşılıkları atanır.
print("Fatura Dönem Gün Sayısı :", ay)

#Kullanıcının günlük doğalgaz sarfiyatı
gunlukSarfiyat = int(aylikSarfiyat) / ay
#Fatura tutarı
fatura = birimFiyat * gunlukSarfiyat * ay
print("Günlük sarfiyatınız\t: ", gunlukSarfiyat, " metreküp\n",
"Tahmini fatura tutarı\t: ", fatura, " TL", sep='')