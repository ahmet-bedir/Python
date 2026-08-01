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


### "import os" gibi bir komutla bütün o isimleri içe aktarmak yerine, yalnızca kullanacağınız isimleri içe aktarmayı tercihde edebilirsiniz. Mesela os modülünün yalnızca name niteliğini ve listdir fonksiyonunu kullanacaksanız:
from os import name, listdir #bir modül içindeki bütün fonksiyon ve nitelikleri içe aktarmak için: "from os import *" kullanılır. Böylece os modülü içindeki bütün fonksiyon ve nitelikleri, başlarına modül adını eklemeye gerek olmadan kullanabilirsiniz.
print(name)
#print(getcwd()) #hata!
print(listdir())


# path
import sys
print(sys.path) # Python bir modül dosyasını ararken, import komutunun verildiği dosyanın dizini ile birlikte, sys.path çıktısında görünen dizinlerin içine bakar.

sys.path.append('/home/ahmet/Masaüstü/') # path listesinin sonuna yeni dizin yani masaüstü dizinini ekliyoruz. (sys.path.insert(0, 'dizin/adı') kodu path listesinin en başına ekleme yapar)
print(sys.path)
import modul #böylece masaüstünde bulunan "modul" modülüne ulaşabiliriz.
print(modul.degisken)
modul.fonksiyon()
