import re

### [] metakarakteri içinde gördüğü bütün karakterleri tek tek liste öğelerine uyguluyor. Önce “öz” ile başlayan bütün öğeleri alıyor, ardından “öz” hecesinden sonra “c” harﬁyle devam eden ve “an” hecesi ile biten öğeyi buluyor. Böylec “özcan” öğesini bulmuş oldu. Aynı işlemi, “öz” hecesinden sonra “h” harﬁni barındıran ve “an” hecesiyle biten öğeye uyguluyor. Bu şekilde ise “özhan” öğesini bulmuş oldu. En son hedef ise “öz” ile başlayıp “k” harﬁ ile devam eden ve “an” ile biten öğe. Yani listedeki “özkan” öğesi. En nihayetinde de elimizde “özcan”, “özhan” ve “özkan” öğeleri kalmış oluyor.
liste = ["özcan", "met", "mehmet", "süleyman", "selim", "ahmet", "özkan", "esra", "dündar", "esin", "esma", "özhan", "özlem", "özkan"]
# for l in liste:
#     sorgu = re.search("öz[kch]an", l)
#     if sorgu:
#         print(sorgu.group())
#
# print("-"*35)
# for l in liste:
#     if re.search("es[mr]a",l):
#         print(l)

## sayı ile başlayanları listelemek için:
# liste = ["23BH56","Ty76Z","4Y7UZ","TYUDZ","34534"]
# for l in liste:
#     if re.match("[0-9]", l):
#         print(l) # 23BH56 4Y7UZ 34534

# Düzenli ifademiz içinde geçen birinci [A-Z] ifadesi aradığımız karakter dizisi olan “Ty76Z” içindeki “T” harﬁni, ikinci [a-z] ifadesi “y” harﬁni, [0-9] ifadesi ise “7” sayısını temsil ediyor. Karakter dizisi içindeki geri kalan harﬂer ve sayılar otomatik olarak eşleştirilecektir. Listeden sadece “Ty76Z” öğesini alır.
# for l in liste:
#     if re.match("[A-Z][a-z][0-9]",l):
#         print(l)

### . (nokta) metakarakteri, yeni satır karakteri hariç bütün karakterleri temsil etmek için kullanılır. “.” metakarakteri sadece tek bir karakterin yerini tutuyor.
# for l in liste:
#     sorgu = re.match("es.a",l)
#     if sorgu:
#         print(sorgu.group())


#
# a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]
# for i in a:
#     if re.match(".[0-9a-z]", i):
#         print(i)
"""
1. Herhangi bir karakter ile başlayacak. Bu karakter sayı, harf veya başka bir karakter
olabilir.
2. Ardından bir sayı veya alfabedeki küçük harﬂerden herhangi birisi gelecek.
3. Bu ölçütleri karşıladıktan sonra, aradığımız karakter dizisi herhangi bir karakter ile
devam edebilir.
çıktı:
23BH56
34534
1agAY54
"""

### * (Yıldız) metakarakteri, kendinden önce gelen bir düzenli ifade kalıbını sıfır veya daha fazla sayıda eşleştirir.
# yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
# for i in yeniliste:
#     if re.match("sa*t",i):
#         print(i)
"""
Burada “*” sembolü kendinden önce gelen “a” karakterini sıfır veya daha fazla sayıda eşleştiriyor. Yani mesela “st” içinde sıfır adet “a” karakteri var. Dolayısıyla bu karakter yazdığımız düzenli ifadeyle eşleşiyor. “sat” içinde bir adet “a” karakteri var. Dolayısıyla bu da eşleşiyor. “saat” ve “saaat” karakter dizilerinde sırasıyla iki ve üç adet “a” karakteri var. Tabii ki bunlar da yazdığımız düzenli ifadeyle eşleşiyor. Listemizin en son öğesi olan “falanca”da da ilk hecede bir adet “a” karakteri var. Ama bu öğedeki sorun, bunun “s” harﬁyle başlamaması.
"""

# for l in liste:
#     if re.match(".*met",l):
#         print(l)
"""
Burada Python’a şu emri verdik: “Bana kelime başında herhangi bir karakteri (“.” sembolü herhangi bir karakterin yerini tutuyor) sıfır veya daha fazla sayıda içeren ve sonu da “met” ile biten bütün öğeleri ver!”
"""

# import os
# import re
# dizin = os.listdir("/home/ahmet/Masaüstü/yüklenenler/")
# for i in dizin:
#     if re.match(".*png",i):
#         print(i)


### “+” metakarakteri ise kendisinden önceki bir veya daha fazla sayıda tekrar eden karakterleri ayıklar.
# for l in liste:
#     if re.match(".+met",l):
#         print(l)


### ? (Soru İşareti) eşleşme sayısının sıfır veya bir olduğu durumları kapsıyor.

yeniliste = ["st", "sat", "saat", "saaat", "falanca"]
# for i in yeniliste:
#     if re.match("sa?t",i):
#         print(i)
"""
Kendisinden önce gelen karakterin hiç bulunmadığı (yani sıfır sayıda olduğu) ve bir adet bulunduğu durumları içine alıyor.
"""

### Metindeki Uluslararası, uluslararası, uluslar arası kelimelerini bulmak için:
# metin = """Uluslararası hukuk, uluslar arası ilişkiler altında bir disiplindir. İlişkilerin uluslararası hukuksal boyutunu bilimsel bir disiplin içinde inceler. Devletlerarası hukuk da denir. Ancak uluslararası ilişkilere yeni aktörlerin girişi bu dalı sadece devletlerarası olmaktan çıkarmıştır."""
#
# nesne = re.findall("[Uu]luslar ?arası", metin)
# for i in nesne:
#     print(i)

### { } (Küme Parantezi) metakarakteri yardımıyla bir eşleşmeden kaç adet istediğimizi belirtebiliyoruz.
# for i in yeniliste:
#     if re.search("sa{3}t",i):
#         print(i)

### Küme içinde iki farklı sayı yazarak, bir karakterin en az ve en çok kaç kez tekrar etmesini istediğimizi belirtebiliriz.
# for i in yeniliste:
#     if re.search("sa{1,3}t",i):
#         print(i)


### ^ sembolünün iki işlevi var. Birinci işlevi, bir karakter dizisinin en başındaki veriyi sorgulamaktır. İkinci işlevi karakter dizisindeki sorgulamak istediğimiz kelimeyi hariç tutmak için.
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', '1agAY54']
# for i in a:
#     sorgu = re.search("^[A-Z]+[0-9]",i)
#     if sorgu:
#         print(sorgu.group())

# for i in a:
#     nesne = re.match("[0-9A-Z][^a-z]+",i)
#     if nesne:
#         print(nesne.group())
"""
1. Aradığımız öğe bir sayı veya büyük harf ile başlamalı
2. En baştaki sayı veya büyük harften sonra küçük harf GELMEMELİ (Bu ölçütü “^” işareti
sağlıyor)
3. Üstelik bu “küçük harf gelmeme durumu” bir veya daha fazla sayıda tekrar etmeli. . . Yani
baştaki sayı veya büyük harften sonra kaç tane olursa olsun asla küçük harf gelmemeli
(Bu ölçütü de “+” işareti sağlıyor”)
not: “^” işaretinin “hariç” anlamı sadece “[]” metakarakterinin içinde kullanıldığı zaman geçerlidir.
"""

### $ "dolar işareti" karakter dizilerinin nasıl biteceğini belirliyor.
liste = ["at", "katkı", "fakat", "atkı", "rahat", "mat", "yat", "sat", "satılık", "katılım"]
# for i in liste:
#     if re.search("at$",i):
#         print(i) # sonu "at" ile biten kelimeleri sorgular.


### \ (ters bölü) “kaçış sembolü”
# liste = ["10$", "25¿", "20$", "10TL", "25£"]
# for i in liste:
#     sorgu = re.match("[0-9]+\\$",i) # “\” sembolünü kullanarak “$” işaretinin özel anlamından kaçtık.
#     if sorgu:
#         print(sorgu.group())


### | (Dik Çizgi) bu metakarakter, birden fazla düzenli ifade kalıbını birlikte eşleştirmemizi sağlar.
# for i in liste:
#     if re.search("^at|at$",i):
#         print(i)
"""
“|” metakarakterini kullanarak başta ve sonda “at” hecesini içeren kelimeleri ayıkladık.
at
fakat
atkı
rahat
mat
yat
sat
"""

### ( ) (Parantez) metakarakteri düzenli ifade kalıplarını gruplar. Bu metakarakter bizim bir karakter dizisinin istediğimiz kısımlarını ayıklamamızda çok büyük kolaylıklar sağlayacak.
import re
from urllib.request import urlopen
url = "https://web.archive.org/web/20121025012131/http://www.istihza.com/py2/icindekiler_python.html"
f = urlopen(url)
regex = 'href=".+html">.+</a>'
for i in f:
    nesne = re.search(regex, str(i, 'utf-8'))
    if nesne:
        print(nesne.group())

