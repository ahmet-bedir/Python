"""
#Bu program fonksiyon kullanılarak; isbn, isim, eser ve yayınevi ölçütlerine göre bu listeden veri alabilmemizi sağlayacak.
liste = [('9789753424080',
          'Greenberg',
          'Sana Gül Bahçesi Vadetmedim',
          'Metis'),
         ('975872519X',
          'Evren',
          'Postmodern Bir Kız Sevdim',
          'İthaki'),
         ('9789754060409',
          'Nietzsche',
          'Böyle Buyurdu Zerdüşt',
          'Cem')]

def sorgula(olçut=None, deger=None):
    for li in liste:
        if not olçut and not deger:
            print(*li, sep=', ')

        elif olçut == 'isbn':
            if deger == li[0]:
                print(*li, sep=', ')

        elif olçut == 'yazar':
            if değer == li[1]:
                print(*li, sep=', ')

        elif olçut == 'eser':
            if deger == li[2]:
                print(*li, sep=', ')

        elif olçut == 'yayınevi':
            if deger == li[3]:
                print(*li, sep=', ')
                
print('-'*45)              
sorgula()
print('-'*45)
sorgula("isbn","975872519X")
print('-'*45)
sorgula(olçut="yayınevi",deger="Cem")
"""
# Aşağıdaki program 'alternatif inşa' yöntemi ile isbnden(), yazardan(), eserden() ve yayinevinden() adlı sınıf metotları, Sorgu() adlı sınıfı alternatif şekillerde inşa etmemizi sağlıyor.
class Sorgu():
    def __init__(self, deger=None, sira=None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]

        if not deger and not sira:
            l = self.liste
        else:
            l = [li for li in self.liste if deger == li[sira]]

        for i in l:
            print(*i, sep=', ')

    @classmethod
    def isbnden(cls, isbn):
        cls(isbn, 0)

    @classmethod
    def yazardan(cls, yazar):
        cls(yazar, 1)

    @classmethod
    def eserden(cls, eser):
        cls(eser, 2)

    @classmethod
    def yayinevinden(cls, yayinevi):
        cls(yayinevi, 3)
        
sorgu = Sorgu()
print('-'*45)
sorgu.isbnden("975872519X")
print('-'*45)
sorgu.yazardan("Greenberg")