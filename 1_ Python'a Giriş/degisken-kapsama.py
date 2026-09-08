# Global değişken
mesaj = "Merhaba"

def selamla():
    # Fonksiyon içinden global değişkene erişilebilir
    print(mesaj)

selamla()  # Merhaba

def degistir():
    # Ama değiştiremezsin (yeni bir lokal değişken oluşur)
    mesaj = "Güle güle"
    print(mesaj)

degistir()     # Güle güle
print(mesaj)   # Merhaba — global değişmedi!

"""
Fonksiyon içinde aynı isimle bir değişken oluşturduğunda, bu yeni bir lokal değişkendir. Global olan etkilenmez. Global değişkeni fonksiyon içinden değiştirmek istersen global anahtar kelimesini kullanman gerekir — ama bu genellikle iyi bir pratik değildir.
"""
###
def func():
    global sayi
    sayi = 7
    
func()
print("fonksiyonun içindeki sayi =", sayi)