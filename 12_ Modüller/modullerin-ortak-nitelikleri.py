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
os = __import__('os')
print(os.getcwd())


### __doc__ Niteliği: Modüllerin __doc__ niteliğini kulanarak, bir modül dosyasının en başında bulunan belgelendirme dizilerine (docstring veya documentation string) ilgili modüle ilişkin kısa açıklama kılavuzlarına erişebiliriz.
import os ; print(os.__doc__)