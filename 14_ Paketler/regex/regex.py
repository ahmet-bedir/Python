import re

# print(dir(re))

### match() metodu bir karakter dizisinde yalnızca en başında belirtilen kelimenin geçip geçmediğini öğrenmek için kullanılır.

a = "python güçlü bir programlama dilidir."

# sorgu = re.match( "python",a)
# if sorgu:
#     print(f"'{sorgu.group()}' kelimesi karakter dizisinin en başında geçmektedir.")
#     print("Konum:", sorgu.span())
# else:
#     print("Aranan kelime karakter dizisinin en başında geçmemektedir!")
#
# # alternatif
# bol = a.split()
# print(bol[0] == "python")
# print(a.startswith("python"))

### search() metodu karakter dizisinin genelinde belirtilen kelimenin geçip geçmediğini öğrenmek için kullanılır.
# sorgu = re.search("güçlü",a)
#
# if sorgu != None:
#     print(f"'{sorgu.group()}' kelimesi karakter dizisinde geçmektedir.")
#     print("Konum:", sorgu.span())
# else:
#     print("Aranan kelime karakter dizisinde geçmemektedir!")

#
# liste = ["elma","armut","erik"]
# for i in liste:
#     sorgu = re.search("armut",i)
#     if sorgu:
#         print(f"'{sorgu.group()}' kelimesi liste içerisinde geçmektedir.")

for i in dir(re):
	sorgu = re.search("searcha",i)
	if sorgu:
		print("Bu metod mevcut.")

### ﬁndall() metodu aranan kelimelefi liste şeklinde verir.
metin = """Guido Van Rossum Python'ı geliştirmeye 1990 yılında başlamış... Yani
aslında Python için nispeten yeni bir dil denebilir. Ancak Python'un çok uzun
bir geçmişi olmasa da, bu dil öteki dillere kıyasla kolay olması, hızlı olması,
ayrı bir derleyici programa ihtiyaç duymaması ve bunun gibi pek çok nedenden
ötürü çoğu kimsenin gözdesi haline gelmiştir. Ayrıca Google'ın da Python'a özel
bir önem ve değer verdiğini, çok iyi derecede Python bilenlere iş olanağı
sunduğunu da hemen söyleyelim. Mesela bundan kısa bir süre önce Python'ın
yaratıcısı Guido Van Rossum Google'de işe başladı..."""

##
# sorgu = re.findall("işe",metin)
# i = 0
# for eleman in sorgu:
# 	i += 1
# 	print(f"{i}.{eleman}")

## search metodu ile...
liste = metin.split()
i = 0
for eleman in liste:
	sorgu = re.search("Python",eleman)
	if sorgu:
		i += 1
		print(f"{i}.{sorgu.group()}")
