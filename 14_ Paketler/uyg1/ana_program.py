## yöntem 1 <<kendi paketimizi içe aktarma>>
import paket.islemler
import paket.metinler as m

#print(dir(paket.islemler))
topla = paket.islemler.toplama(2,3)
print("Toplama:", topla)

#print(dir(m))
m.metin1()


## yöntem 2 <<kendi paketimizi içe aktarma>>
from paket import islemler
from paket import metinler as m

cikar = islemler.cikarma(2,1)
print("Çıkarma:", cikar)

m.metin2()


## yöntem 3 <<modül içindeki nitelik ve metotlara öneksiz olarak erişmek için>>
from paket.islemler import carpma
from paket.metinler import metin3

carp = carpma(2,3)
print("Çarpma:", carp)

metin3()


## yöntem 4 <<bir paket içindeki bir modülün bütün nitelik ve metotlarını mevcut isim alanına olduğu gibi aktarmak için>>
from paket.islemler import *
from paket.metinler import *

bol = bolme(8,2)
print("Bölme :", bol)

metin4()