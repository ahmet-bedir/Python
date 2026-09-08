##
def ornek():
	return "deneme."

a = ornek()
print(a)


##
def ismin_ne():
	isim = input("ismin ne? ")
	return isim

print("Merhaba {} . Nasılsın?".format(ismin_ne()))

##
def fonk(s):
	if s < 0:
		return "Eksi Değerli Sayı Olmamalı!"
	else:
		return s

a = fonk(-1)
print(a)
