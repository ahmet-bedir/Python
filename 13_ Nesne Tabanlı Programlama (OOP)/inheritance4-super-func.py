"""
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
        super().__init__(isim, rutbe)
        #super() fonksiyonu, miras alınan üst sınıfın __init__() metodu içindeki kodların, miras alan alt sınıfın __init__() metodu içine aktarılmasını sağlıyor. Böylece hem taban sınıfın __init__() metodu içindeki self.isim ve self.rutbe niteliklerini korumuş, hem de self.guc adlı yeni bir nitelik ekleme imkanı elde etmiş oluyoruz.
        self.guc = 100
        
class Isci(Oyuncu): #alt sınıf
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)
        self.guc = 70
        
class Yonetici(Oyuncu): #alt sınıf
    def __init__(self, isim, rutbe):
        super().__init__(isim, rutbe)
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
"""

### Eğer taban sınıfın __init__() metodundaki parametre listesini alt sınıflarda da tek tek tekrar etmesini istemiyorsanız kodları şöyle yazabilirsiniz:
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
    def __init__(self, *args):
        super().__init__(*args)
        #Oyuncu.__init__(self, *args)
        self.guc = 100
    def hareket_et(self):
        super().hareket_et()
        print('hedefe ulaşıldı.')
        
class Isci(Oyuncu): #alt sınıf
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 70
        
class Yonetici(Oyuncu): #alt sınıf
    def __init__(self, *args):
        super().__init__(*args)
        self.guc = 50
        
        
###
asker1 = Asker("ali","er")

print("İsim:", asker1.isim)
print("Rütbe:", asker1.rutbe)
print("Güç:", asker1.guc)
asker1.hareket_et()

print('-'*45)
###
isci1 = Isci("erman","işçi")

print("İsim:", isci1.isim)
print("Rütbe:", isci1.rutbe)
print("Güç:", isci1.guc)
isci1.hareket_et()

print('-'*45)
###
yonetici1 = Yonetici("can","yönetici")

print("İsim:", yonetici1.isim)
print("Rütbe:", yonetici1.rutbe)
print("Güç:", yonetici1.guc)
yonetici1.hareket_et()