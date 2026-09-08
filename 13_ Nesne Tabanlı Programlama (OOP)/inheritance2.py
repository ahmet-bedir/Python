class Oyuncu(): #taban sınıf, üst sınıf (super class)
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 0

    def hareket_et(self):
        print('hareket ediliyor...')

    def puan_kazan(self):
        print('puan kazanıldı')

    def puan_kaybet(self):
        print('puan kaybedildi')
        
class Asker(Oyuncu): #alt sınıf
    def hareket_et(self):
        # Taban sınıfta zaten hareket_et() adlı bir örnek metodu olduğu için, alt sınıfta tanımladığımız aynı adlı örnek metodu, taban sınıftaki metodun yerine geçip üzerine yazıyor(override).
        print('yeni hareket_et() metodu')
        
        
###
asker1 = Asker("ali","er")
asker1.hareket_et()

"""
Eğer alt sınıfa eklenen herhangi bir nitelik veya metot taban sınıfta zaten varsa, alt sınıfa eklenen nitelik ve metotlar taban sınıftaki metot ve niteliklerin yerine geçecektir.
"""