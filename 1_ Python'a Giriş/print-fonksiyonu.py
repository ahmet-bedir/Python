####
print("Python Programlama Dili...")

# print("Python programlama dilinin adı "piton" yılanından gelmez") #hata!
print("Python programlama dilinin adı \"piton\" yılanından gelmez")
print('Python programlama dilinin adı "piton" yılanından gelmez')

# print('İstanbul'un 5 günlük hava durumu tahmini') #hata!
print("İstanbul'un 5 günlük hava durumu tahmini")

print("""Python programlama dilinin adı "piton" yılanından gelmez""")
print("""İstanbul'un 5 günlük hava durumu tahmini""")

print("""
[H]======BAŞLIK=====[-][o][x]
|                           |
|  Programa Hoşgeldiniz!    |
|        Sürüm 0.8          |
| Devam etmek için herhangi |
|    bir düğmeye basın.     |
|                           |
|===========================|
""")

print("Mehmet", "Öz", "İstanbul", "Çamlıca", 156, "/", 45)
print("Mehmet" " Öz" " İstanbul" " Çamlıca" " 156" " /" " 45")

print("http://","www.","google.","com")
print("http://","www.","google.","com", sep="")

print ("Pardus","Ubuntu",'RedHat', sep="\n")
print(1, 2, 3, 4, 5, sep="-")
print('a', 'b', sep=None, end="\n")

print("L", "i", "n", "u", "x", sep=".")
print(*"Linux", sep=".", end="\n\n")


dosya = open("deneme.txt","w")
print("1.Mesaj...", file=dosya)
dosya.close()

print("-" * 45)
# Varsayılan parametre değerleri...
import sys
print("Tahir olmak da ayıp değil",
"Zühre olmak da...", sep=" ", end="\n", file=sys.stdout, flush=False)

print('\n'"sys modülü ile kullanabileceğimiz değişken ve fonksiyonlar :\n", dir(sys), sep='', end="\n\n")
print("Standart çıktı :", sys.stdout) 
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
print("-" * 45)

dosya = open("deneme.txt","w")
print("2.Mesaj...", file=dosya, flush=True) 
# flush degerini True verirsek veriler tamponda bekletilmeksizin (dosyayı kapatmadan) hemen yazar...

# std.out kalıcı olarak değiştirme...
dosya = open("deneme.txt","w")
yedek = sys.stdout
sys.stdout = dosya
print("3.Mesaj...")

print("Standart Çıktı Dosyaya Aktarıldı :", sys.stdout)
# <_io.TextIOWrapper name='deneme.txt'  mode='w' encoding='utf-8'>

sys.stdout = yedek
print("Standart Çıktı Ekrana Aktarıldı :", sys.stdout)
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
