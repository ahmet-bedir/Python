"""
PEP 8'e göre import'lar şu sırada ve gruplar halinde yazılır:

1.Standart kütüphane (os, sys, json)

2.Üçüncü parti paketler (requests, numpy)

3.Yerel modüller (matematik_yardimci)

Her grup arasında boş satır bırak.
"""

import os

if os.name == 'posix':
	print('Hoşgeldin Linux Kullanıcısı!')
elif os.name == 'nt':
	print('Hoşgeldin Windows Kullanıcısı!')


#
print(os.getcwd()) # o anda hangi dizin altında bulunduğunuzu öğrenmek için.

#
print(os.makedirs('DATA')) # o anda içinde bulunduğunuz dizinde yeni bir dizin oluşturmak için.


# subprocess modülü, harici komutları Python içinden çalıştırabilmemizi sağlayan bir araçtır.
import subprocess as sp
sp.call(['bash','komut.sh'])


# webbrowser modülü, bilgisayarımızda kurulu internet tarayıcısını kullanarak internet sitelerini açabilmemizi sağlar.
import webbrowser as web
web.open('www.duckduckgo.com')


### "import os" komutuyla bütün fonksiyon ve nitelikleri içe aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarabilirsiniz. Mesela os modülünün yalnızca 'name' niteliğini ve 'listdir' fonksiyonunu kullanacaksanız:
from os import name, listdir  

print(getcwd())  # hata!
print(listdir())
print(name)  # Bu durumda os.name komutu hata verecektir. Çünkü biz from os import name komutunu verdiğimizde, os modülünü değil, bu modül içindeki bir nitelik olan name’i içe aktarmış oluyoruz. Dolayısıyla os ismini kullanamıyoruz sadece nitelik veya fonksiyon ismini modül öneki olmadan kullanılır.

##############
from os import path as p
from os import listdir as ld
# Bir modül içindeki bütün fonksiyon ve nitelikleri içe aktarmak için: "from os import *" kullanılır. Böylece os modülü içindeki bütün fonksiyon ve nitelikleri, başlarına modül adını eklemeye gerek olmadan kullanabilirsiniz. Ancak bu yöntem pek tavsiye edilmez. Çünkü bu şekilde, modül içindeki bütün isimleri kontrolsüz bir şekilde mevcut ortama ‘boşaltmış’ oluyoruz. Mesela eğer sys modülü bu şekilde içe aktarılmadan önce version diye başka bir değişken tanımlamışsanız, modül içe aktarıldıktan sonra, önceden tanımladığınız bu version değişkeninin değeri kaybolacaktır.

##############
# path
import sys
print(sys.path)  # Python bir modül dosyasını ararken, import komutunun verildiği dosyanın dizini ile birlikte, sys.path çıktısında görünen dizinlerin içine bakar.

sys.path.append('/home/ahmet/Masaüstü/') # path listesinin sonuna yeni dizin yani masaüstü dizinini ekliyoruz. (sys.path.insert(0, 'dizin/adı') kodu path listesinin en başına ekleme yapar)
print(sys.path)
import modul  # böylece masaüstünde bulunan "modul" modülüne ulaşabiliriz.

print(modul.degisken)
modul.fonksiyon()

##############
# __all__ listesi içinde belirttiğimiz fonksiyonlar içe aktarılır. Bu listeyi kullanarak, yıldızlı içe aktarmalarda nelerin içe aktarılıp nelerin dışarıda bırakılacağını kontrol edebilirsiniz. Yalnız unutmamanız gereken nokta, bu yöntemin öteki içe aktarma türlerinde hiçbir işe yaramayacağıdır.
__all__ = ['fonk1', 'fonk2', 'fonk3']

from modül import *

