"""
# Modüllerin Özel Nitelikleri
import os, sys, random
set_os = set(dir(os))
set_sys = set(dir(sys))
set_random = set(dir(random))

print(set_os & set_sys & set_random)
# Bu kodlar, os, sys ve random modüllerinin kesişim kümesini, yani her üç modülde ortak olarak bulunan nitelikleri verecektir:
# {'__doc__', '__package__', '__loader__', '__name__', '__spec__'}


# Kodların yeniden kullanılabilir özellikte olması (code reusability) için:
moduller = ['os', 'sys', 'random']
print("Modüller : ", *moduller, sep='  ')

def ortak_nitelikler(moduller):
	kumeler = [set(dir(__import__(modul))) for modul in moduller]
	return set.intersection(*kumeler)

print(ortak_nitelikler(moduller))

"""
###
moduller = ['os','random']
for modul in moduller:
    __import__(modul)
    
os = __import__('os')
print(os.getcwd())


### __doc__ Niteliği
#import uyg1.sozluk_modulu ; print(uyg1.sozluk_modulu.__doc__)



### __loader__ Niteliği

### __spec__ Niteliği

### __package__ Niteliği