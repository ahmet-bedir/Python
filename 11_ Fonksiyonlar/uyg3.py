###1
sesli_harfler = 'aeıioöuü'
sayac = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler
    
for harf in kelime:
    if seslidir(harf):
        sayac += 1

mesaj = "'{}' kelimesinde {} tane sesli harf vardır!"
print(mesaj.format(kelime, sayac))

###2
sesli_harfler = 'aeıioöuü'
sayac = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır():
    global sayac
    for harf in kelime:
        if seslidir(harf):
            sayac += 1
    return sayac

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))

###3
sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    print('sayaç değişkeninin değeri şu anda: ', sayaç)
    return harf in sesli_harfler

def artır():
    global sayaç
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır()))

###4
sesli_harfler = 'aeıioöuü'
sayaç = 0

kelime = input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

mesaj = '{} kelimesinde {} sesli harf var.'
print(mesaj.format(kelime, artır(sayaç)))

###5
sesli_harfler = 'aeıioöuü'
sayaç = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artır(sayaç, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayaç += 1
    return sayaç

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artır(sayaç, kelime)))

def çalıştır():
    kelime = kelime_sor()
    ekrana_bas(kelime)

çalıştır()