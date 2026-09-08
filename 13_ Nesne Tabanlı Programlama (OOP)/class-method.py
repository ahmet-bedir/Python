### 
class Sinif():
    sinif_niteligi = 0

    def __init__(self):
        self.ornek_niteligi = 0

    def ornek_metodu(self):
        self.ornek_niteligi += 1
        return self.ornek_niteligi

    @classmethod
    def sinif_metodu(cls):
        cls.sinif_niteligi += 2
        return cls.sinif_niteligi

#sınıf metodunu sınıfın ismiyle çağırıyoruz.
print("Sınıf metodu:", Sinif.sinif_metodu())

#örnek metodunu sınıfı örnekledikten sonra çağırıyoruz.
ornek = Sinif()
print("Örnek metodu:", ornek.ornek_metodu())