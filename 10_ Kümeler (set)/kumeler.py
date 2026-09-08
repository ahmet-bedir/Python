kume = set()

print(kume, type(kume))

##
liste = ["elma","armut","erik"]
kume = set(liste)
print(kume, type(kume))

##
demet = ("ali","veli","ersin")
kume = set(liste)
print(kume, type(kume))

##
metin = "Python Programlama Dili."
kume = set(metin)
print(kume, type(kume))

##
sozluk = { 1 : "a",
		   2 : "b",
		   3 : "c"}
kume = set(sozluk)
print(kume, type(kume))

## Sözlüklerin ayırt edici işareti olan süslü parantezleri kullanarak ve öğeleri birbirinden virgülle ayırarak da küme adlı veri tipini elde edebiliyoruz.
kume = {'Python', 'C++', 'Ruby', 'PHP'}

print(kume, type(kume))

## Listede aynı öğeden iki-üç tane bulunsa bile, kümemiz bu öğeleri teke indirecektir.
liste = ["elma", "armut", "elma", "kebap", "şeker", "armut", "çilek", "ağaç", "şeker", "kebap", "şeker"]
for i in set(liste):
	print(i)

##
liste = ["elma", "armut", "elma", "kiraz", "çilek", "kiraz", "elma", "kebap"]

for i in set(liste):
	print("{} listede {} kez geçiyor!".format(i, liste.count(i)))

##
import random
liste = [random.randint(0,10) for i in range(10)]
print(set(liste))

