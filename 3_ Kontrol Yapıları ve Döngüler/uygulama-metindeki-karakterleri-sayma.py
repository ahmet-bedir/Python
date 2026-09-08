### Karakter Dizisindeki, Girilen Karakteri Sayma
metin = """Bu programlama dili Guido
Van Rossum adlı Hollandalı bir 
programcı tarafından 90’lı yılların 
başında geliştirilmeye başlanmıştır..."""

print(metin)
giris = input("Sorgulamak isrediğiniz harfi giriniz : ")
harf_sayisi = 0

for harf in metin: #metin içindeki her bir öğeyi 'harf' değişkenine yolla.
    if harf == giris: #harf değişkeni eşitse girilen harfe...
        harf_sayisi += 1 #harf_sayisi değişkenini bir arttır.
print("'{}' harfi metinde {} kez geçiyor...".format(giris, harf_sayisi))

### 2.yöntem
metin = """Bu programlama dili Guido
Van Rossum adlı Hollandalı bir 
programcı tarafından 90’lı yılların 
başında geliştirilmeye başlanmıştır..."""

print(metin)
giris = input("Sorgulamak isrediğiniz harfi giriniz : ")
harf_sayisi = ''

for harf in metin: #metin içindeki her bir öğeyi 'harf' değişkenine yolla.
    if harf == giris: #harf değişkeni eşitse girilen harfe...
        harf_sayisi += harf #harf_sayisi değişkenine girilen harfi ekle.
print("'{}' harfi metinde {} kez geçiyor...".format(giris, len(harf_sayisi)))



### metindeki her karakterin kaç kez geçtiğini bulma.(yapım aşamasında)
metin = "pythonpytho"
sayi = 0
karakterler = ''
for harf in metin:
	if harf in metin and harf not in karakterler:
		karakterler += harf
	elif harf in karakterler:
		


for harf in karakterler:
	if harf in karakterler:
		sayi += 1
		print("'{}' harfi metinde {} kez geçiyor.".format(harf,sayi))
		