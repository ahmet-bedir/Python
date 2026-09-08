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
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 100
        
class Isci(Oyuncu): #alt sınıf
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 70
        
class Yonetici(Oyuncu): #alt sınıf
    def __init__(self, isim, rutbe):
        self.isim = isim
        self.rutbe = rutbe
        self.guc = 50
        
        
###
asker1 = Asker("ali","er")

print("İsim:", asker1.isim)
print("Rütbe:", asker1.rutbe)
print("Güç:", asker1.guc)

print('-'*45)
###
isci1 = Isci("erman","işçi")

print("İsim:", isci1.isim)
print("Rütbe:", isci1.rutbe)
print("Güç:", isci1.guc)

print('-'*45)
###
yonetici1 = Yonetici("can","yönetici")

print("İsim:", yonetici1.isim)
print("Rütbe:", yonetici1.rutbe)
print("Güç:", yonetici1.guc)
