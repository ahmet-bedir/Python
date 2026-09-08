class PersonClass:
    # class attributes
    city = "izmit"
    
    # constructor methods
    def __init__(self, name, year):
		# object attributes
        self.name = name
        self.year = year
        print("Yapıcı Metod (constructor metod) Çalıştı.")
        
    # instance methods
    def introFunc(self):
        print("Selam, " + self.name)
        
    def ageCalcFunc(self):
        return 2026 - self.year

print('-'*40)
# object (instance)
object1 = PersonClass("ali",1988)
# accessing object attributes
print(f"İsim: {object1.name}\nDoğum Yılı: {object1.year}\nŞehir: {object1.city}")
object1.introFunc()
print("Yaş:", object1.ageCalcFunc())

print('-'*40)
object2 = PersonClass(year=2002,name="aylin")
print(f"İsim: {object2.name}\nDoğum Yılı: {object2.year}\nŞehir: {object2.city}")
object2.introFunc()
print("Yaş:", object2.ageCalcFunc())

print('-'*40)
# updating
object1.name = "ahmet"
object1.city = "ankara"

print(f"İsim: {object1.name}\nŞehir: {object1.city}")
object1.introFunc()
