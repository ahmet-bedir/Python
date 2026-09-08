### Eğer sınıf içinde tanımlayacağınız fonksiyon, örnek ya da sınıf niteliği üzerinde herhangi bir işlem yapmayacaksa statik metod kullanılır.
class Sinif():
    sınıf_niteligi = 0

    def __init__(self, veri):
        self.veri = veri

    def ornek_metodu(self):
        return self.veri

    @classmethod
    def sinif_metodu(cls):
        return cls.sinif_niteligi

    @staticmethod
    def statik_metot():
        print('Statik metot!')
        
#Statik metotları hem örnekler hem de sınıf adları üzerinden kullanabiliriz.
ornek = Sinif("veri")
ornek.statik_metot() #örnek üzerinden

Sinif.statik_metot() #sınıf üzerinden