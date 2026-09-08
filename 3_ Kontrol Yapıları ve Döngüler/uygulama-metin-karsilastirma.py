### Karakter Dizilerinin İçeriğini Karşılaştırma.
metin1 = "abcabc"
metin2 = "acacdd"
fark = ''
esitler = ''

#metin1 adlı değişken içinde bulunan, ama metin2 adlı değişken içinde bulunmayan öğeleri ayırma.
for m1 in metin1: #metin1'deki bütün öğeleri 'm1' adını verdiğimiz değişkene verdik.
    if m1 not in metin2: #eğer 'm1' adlı bu öğe metin2'de yoksa...
        if m1 not in fark: #farklı öğelerin tekrarlayanlarını almamak için eğer 'm1' adlı bu öğe fark'dada yoksa 'fark' değişkenine farklı öğeleri ekle.
            fark += m1 
    elif m1 in metin2 and m1 not in esitler: #eğer 'm1' adlı bu öğe metin2'de varsa ve eğer 'm1' adlı bu öğe aynilari adlı değişkendede yoksa 'aynilari' değişkenine öğeleri ekle.
        esitler += m1
print("Farklı Karakterler :", *fark)
print("Aynı Karakterler :", *esitler)

   
