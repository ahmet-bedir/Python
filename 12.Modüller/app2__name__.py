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
    if sayac != 0:
        print(f"'{kelime}' kelimesinde {artir(sayac, kelime)} sesli harf var.")
    else:
        print(f"'{kelime}' kelimesinde sesli harf yok!")
        
def calistir():
    kelime = kelime_sor()
    ekrana_bas(kelime)
    

if __name__ == '__main__':
    calistir()