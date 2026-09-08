# Rastgele 6 adet sayı üretme.
def sayi_uret(basla=0,bitis=10,adet=5):
	import random
	sayilar = set()

	while len(sayilar) < adet:
		sayilar.add(random.randint(basla,bitis))
		#print(sayilar)
	return sayilar

for i in range(10):
    a = sayi_uret()
    print(a)