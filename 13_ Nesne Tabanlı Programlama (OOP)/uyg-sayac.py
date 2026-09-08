"""
### fonksiyon kullanılarak girilen kelimede geçen sesli harflerin sayısını bulma.
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
    
if __name__ == "__init__":
    calistir()
    
### OOP kullanılarak girilen kelimede  sadece sesli harflerin sayısını bulma.
class HarfSayaci:
    def __init__(self):
        self.sesliler = "aeıioöuü"
        self.sayac = 0
        
    def giris(self):
        return input("Kelime Giriniz: ")
        
    def seslidir(self, harf):
        return harf in self.sesliler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac += 1
        return self.sayac

    def ekrana_bas(self):
        mesaj = "{} kelimesinde {} sesli harf var."
        sesli_harf_sayisi = self.artir()
        print(mesaj.format(self.kelime, sesli_harf_sayisi))

    def calistir(self):
        self.kelime = self.giris()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()
"""
### OOP kullanılarak girilen kelimede sesli ve sessiz harf sayısını bulma.
class HarfSayaci:
    def __init__(self):
        self.sesli_harfler = 'aeıioöuü'
        self.sessiz_harfler = 'bcçdfgğhjklmnprsştvyz'
        self.sayac_sesli = 0
        self.sayac_sessiz = 0

    def kelime_sor(self):
        return input('Bir kelime girin: ')

    def seslidir(self, harf):
        return harf in self.sesli_harfler

    def sessizdir(self, harf):
        return harf in self.sessiz_harfler

    def artir(self):
        for harf in self.kelime:
            if self.seslidir(harf):
                self.sayac_sesli += 1
            if self.sessizdir(harf):
                self.sayac_sessiz += 1
        return (self.sayac_sesli, self.sayac_sessiz)

    def ekrana_bas(self):
        sesli, sessiz = self.artir()
        mesaj = "'{}' kelimesinde {} sesli, {} sessiz harf var."
        print(mesaj.format(self.kelime, sesli, sessiz))

    def calistir(self):
        self.kelime = self.kelime_sor()
        self.ekrana_bas()

if __name__ == '__main__':
    sayac = HarfSayaci()
    sayac.calistir()