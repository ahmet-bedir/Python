# -*- coding: utf-8 -*-
import sys
_2x_metni = u"""
Python'un 2.x sürümünü kullanıyorsunuz...
Programı çalıştırabilmek için 3.x sürümünün kurulu olması gerekiyor..."""

_3x_metni = u"""
Python'un 3.x sürümünü kullanıyorsunuz...
Programa hoşgeldiniz...
"""
if sys.version_info.major < 3:
    print(_2x_metni)
else:
    print(_3x_metni)
    
version = sys.version_info #version_info değişkeni bize python sürümünün major(ana sürüm), minor(alt sürüm) ve micro(en alt sürüm) gibi parametreler aracılığıyla sunduğu sayı değerli veri olarak verir.
print("Kullanmış Olduğunuz Python Sürümü :", version)
print("major :", version.major)
print("minor :", version.minor)
print("micro :", version.micro)

'''
version = sys.version #version değişkeni bize python sürümünü bir karakter dizisi olarak verir.
print("Kullanmış Olduğunuz Python Sürümü :", version)

if sys.version_info.major == 3 and sys.version_info.minor > 12: #python sürümü 3.12'den yüksek ise...
    print("Kullanmış Olduğunuz Python Sürümü :", sys.version_info)
if "3.2" in sys.version: #python sürümü 3.2 ise...
    print("Kullanmış Olduğunuz Python Sürümü :", sys.version_info)
'''