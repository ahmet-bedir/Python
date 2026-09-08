


class Circle:
    pi = 3.14159  # Class attribute — tüm daireler için aynı

    def __init__(self, radius):
        self.radius = radius  # Instance attribute — her daire için farklı

    def area(self):
        return Circle.pi * self.radius ** 2

c1 = Circle(5)
c2 = Circle(10)

print(c1.area())   # 78.53975
print(c2.area())   # 314.159

# Aynı sınıftan mı?
print(type(c1))           # <class '__main__.Circle'>
print(type(c2))           # <class '__main__.Circle'>
print(type(c1) == type(c2))  # True

# Ama farklı nesneler
print(c1 is c2)    # False
print(id(c1))      # farklı bellek adresi
print(id(c2))      # farklı bellek adresi
