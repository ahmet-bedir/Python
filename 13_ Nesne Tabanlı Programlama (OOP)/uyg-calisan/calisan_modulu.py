class Calisan:
    __personel = [] # Sınıf değişkeni gizli (private) olarak tanımlandı.
    def __init__(self,isim):
        self.isim = isim
        self.kabiliyetleri = []
        self.__personel_ekle()

    def __personel_ekle(self): # Gizli (private) metot tanımlandı.
        self.__personel.append(self.isim)
        print(f"'{self.isim}' adlı kişi personel listesine eklendi.")

    @classmethod
    def personel_listesi(cls):
        print("=== Personel Listesi ===")
        for kisi in cls.__personel:
            print(kisi)

    def kabiliyet_ekle(self,kabiliyet):
        self.kabiliyetleri.append(kabiliyet)
        
    def kabiliyet_listesi(self):
        print(f"'{self.isim}' adlı personelin kabiliyetleri:")
        for k in self.kabiliyetleri:
            print(k)

    @classmethod
    def personel_sayisi(cls):
        print(f"Personel Sayısı: {len(cls.__personel)}")