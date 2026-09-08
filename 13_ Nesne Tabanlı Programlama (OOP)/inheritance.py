# Taban sınıf (base class), üst sınıf (super class) veya ebeveyn sınıf (parent class).
class Person:
    def __init__(self, name):
        self.name = name
        print("Person Created.")
    def instanceMethod(self):
        pass
    @classmethod
    def classMethod(cls):
        pass
    
# Alt sınıf (subclass).
class Student(Person): # Person sınıfından miras alındı.
    pass

###
s1 = Student("ali")
print(dir(s1)) # Person sınıfından miras alındığı için Person sınıfının tüm metod ve nitelikleri Student sınıfındada mevcut durumda.
print(s1.name)