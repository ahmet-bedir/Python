sesli_harfler = 'aeıioöuü'
sayac = 0

def kelime_sor():
    return input('Bir kelime girin: ')

def seslidir(harf):
    return harf in sesli_harfler

def artir(sayac, kelime):
    for harf in kelime:
        if seslidir(harf):
            sayac += 1
    return sayac

def ekrana_bas(kelime):
    mesaj = "{} kelimesinde {} sesli harf var."
    print(mesaj.format(kelime, artir(sayac, kelime)))

def calistir():
    kelime = kelime_sor()
    ekrana_bas(kelime)
    

if __name__ == '__main__':
    calistir()