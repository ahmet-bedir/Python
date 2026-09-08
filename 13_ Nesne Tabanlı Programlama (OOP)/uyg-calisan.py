### Sınıf nitelikleri sınıf çağrılmadan çalışmaya başlamaları ve sınıf niteliklerine atanan değerlerin, eğer yapılabiliyorsa bu değerler üzerinde sonradan yapılan değişiklikler o sınıfın bütün örneklerini etkiler.
"""
class Calisan:
    kabiliyetleri = []
    unvan = "işçi"
    maas = 1500
    memleketi = ''
    dogumTarihi = ''
"""
        
### Örnek niteliklerine erişebilmek için de ilgili sınıfı örneklememiz gerekir.
class Calisan:
    def __init__(self):
        self.kabiliyetleri = []
        self.unvan = 'işçi'
        self.maas = 35500
        self.memleketi = ''
        self.dogumTarihi = ''


ahmet = Calisan()
ahmet.kabiliyetleri.append("bilgisayar")
ahmet.kabiliyetleri.append("yazılım")
ahmet.unvan = "yönetici"


print(f"Ahmet\nKabiliyetleri: {ahmet.kabiliyetleri}")
print(f"Unvanı: {ahmet.unvan}")
print(f"Maaşı: {ahmet.maas}")

print('='*45)

mehmet = Calisan()
mehmet.kabiliyetleri.append("tamir")
mehmet.kabiliyetleri.append("tesisat")
mehmet.maas = 23000

print(f"Mehmet\nKabiliyetleri: {mehmet.kabiliyetleri}")
print(f"Unvan: {mehmet.unvan}")
print(f"Maaşı: {mehmet.maas}")
