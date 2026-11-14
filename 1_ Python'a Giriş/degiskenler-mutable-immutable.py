"""
> Immutable (Değiştirilemez) Nesneler
Bir nesne oluşturulduktan sonra değeri değiştirilemiyorsa, o nesne immutable'dır.

Immutable tipler:

- int (tam sayılar)

- float (ondalıklı sayılar)

- str (stringler)

- tuple (demetler)

- bool (True/False)

- frozenset

> Mutable (Değiştirilebilir) Nesneler
Bir nesne oluşturulduktan sonra değeri değiştirilebiliyorsa, o nesne mutable'dır.

Mutable tipler:

- list (listeler)

- dict (sözlükler)

- set (kümeler)
"""

### 
x = "merhaba"
# x[0] = "M"  # TypeError! String değiştirilemez.

print(x, id(x))  # merhaba 139680153029968

# x değişkenini tekrar tanımlıyoruz.
x = "Merhaba"  # Bu yeni bir string nesnesi oluşturur
               # x etiketi yeni nesneye yapıştırılır
               # Eski "merhaba" nesnesi artık sahipsiz

print(x, id(x))  # Merhaba 139680153030160
"""
Bir string'i "değiştirdiğini" düşündüğünde, aslında yeni bir string oluşturuyorsun ve etiketi yeni nesneye yapıştırıyorsun.
"""

###
liste = [1, 2, 3]
print(id(liste))  # 140234567890
print(liste)  # [1, 2, 3]

liste.append(4)
print(id(liste))  # 140234567890 — aynı id, aynı nesne!
print(liste)      # [1, 2, 3, 4]

"""
Neden Önemli?
Bu ayrım, özellikle fonksiyonlara parametre geçerken ve değişken kopyalamada çok önemli hale gelir.
"""

# Immutable — güvenli
def arttir(sayi):
    sayi += 1
    print(f"Fonksiyon içinde: {sayi} {id(sayi)}")

x = 10
arttir(x)
print(f"Fonksiyon dışında: {x} {id(x)}")
# Fonksiyon içinde: 11
# Fonksiyon dışında: 10 — x değişmedi!
# id'ler farklı


# Mutable — dikkat!
def eleman_ekle(liste):
    liste.append(99)
    print(f"Fonksiyon içinde: {liste} {id(liste)}")

my_list = [1, 2, 3]
eleman_ekle(my_list)
print(f"Fonksiyon dışında: {my_list} {id(my_list)}")
# Fonksiyon içinde: [1, 2, 3, 99]
# Fonksiyon dışında: [1, 2, 3, 99] — my_list de değişti!
# id'ler aynı

"""
Fonksiyona bir liste geçtiğinde, fonksiyon orijinal listeyi değiştirebilir. Çünkü fonksiyona listenin kendisi değil, listeye olan referans geçilir.
"""