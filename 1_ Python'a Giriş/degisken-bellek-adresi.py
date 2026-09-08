"""
Sayılar immutable (değiştirilemez) olduğu için y değişkenini x'e eşitledikten sonra x'in değerini değiştirmemize rağmen, y değişkeni eski değerdedir.
"""
x = 42
y = x

print(f"x: {x}, Türü: {type(x)}, Bellek Adrsi: {id(x)}")  # x: 42, Türü: <class 'int'>, Bellek Adrsi: 94821295720600
print(f"y: {y}, Türü: {type(y)}, Bellek Adrsi: {id(y)}")  # y: 42, Türü: <class 'int'>, Bellek Adrsi: 94821295720600
print(x is y)  # True — aynı nesne!

print('-' * 50)

x = 99

print(f"x: {x}, Türü: {type(x)}, Bellek Adrsi: {id(x)}")  # x: 99, Türü: <class 'int'>, Bellek Adrsi: 94821295722424
print(f"y: {y}, Türü: {type(y)}, Bellek Adrsi: {id(y)}")  # y: 42, Türü: <class 'int'>, Bellek Adrsi: 94821295720600 (y hâlâ eski nesneye bağlı)

print(x is y)  # False
