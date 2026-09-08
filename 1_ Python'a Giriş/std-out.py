# standart çıktı(ekran) kalıcı olarak dosyaya aktarma.
import sys

isim = "Ahmet"
yas = 35

print("Standart Çıktı :", sys.stdout) # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
print(sys.stdout.name, sys.stdout.mode, sys.stdout.encoding, sep='\n')
# <stdout>
# w
# utf-8

f = open("dosya.txt","w")
sys.stdout, f = f, sys.stdout
print("Standart Çıktı Dosyaya Aktarıldı :", sys.stdout) # <_io.TextIOWrapper name='/home/ahmet/Masaüstü/dosya.txt' mode='w' encoding='UTF-8'>
print(sys.stdout.name, sys.stdout.mode, sys.stdout.encoding, sep='\n')
# dosya.txt
# w
# utf-8

print("---------------")
print("İsim\t:", isim)
print("Yaş\t:", yas)
print("---------------")


f, sys.stdout = sys.stdout, f
print('-' * 47)
print("Standart Çıktı Ekrana Aktarıldı :", sys.stdout) # <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
print(sys.stdout.name, sys.stdout.mode, sys.stdout.encoding, sep='\n')
# <stdout>
# w
# utf-8

f.close()

###
import os
print(dir(os))
print("Çalışmakta Olduğumuz Konum :", os.getcwd())