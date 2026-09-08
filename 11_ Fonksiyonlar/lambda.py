### normal fonksiyonu tanımlama.
def topla(s1, s2):
	return s1+s2

print(topla(5,6))

### lambda fonksiyonu tanımlama.
carpma = lambda s1, s2 : s1*s2

print(carpma(5,6))


###
def ciftmi(sayi):
	return sayi % 2 == 0

print(ciftmi(999))

ciftmi = lambda sayi : sayi % 2 == 0
a = ciftmi(8)
print(a)



