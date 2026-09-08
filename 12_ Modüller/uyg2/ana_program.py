# import modul  # Bütün nitelikler ve fonksiyonlar içe aktarılır.

# print(dir(modul))  # ['__builtins__', '__cached__', '__doc__', '__file__', '__fonk5', '__loader__', '__name__', '__package__', '__spec__', '_fonk4', '_x', 'fonk1', 'fonk2', 'fonk3_']
# print(modul.fonk1())

##############
# from modul import *  # Bu şekilde, ismi _ ile başlayanlar hariç bütün nitelik ve fonksiyonlar, mevcut etki alanına aktarılır.

# print(dir())  # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'fonk1', 'fonk2', 'fonk3_']
# print(fonk2())

##############
# İsmi _ ile başlayan fonksiyonları, doğrudan isimlerini kullanarak içe aktarma imkanına sahipsiniz:
# from modul import __fonk5
# from modul import _fonk4

# print(_fonk4())

##############
# Yalnızca kendi belirlediğiniz isimlerin içe aktarılması için __all__ adlı bir listeden yararlanabilirsiniz. Bu yöntem yannız yıldızlı içe aktarmada işe yarar.
from modul import *

print(dir())  # ['__all__', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_fonk4', 'fonk1', 'fonk3_']