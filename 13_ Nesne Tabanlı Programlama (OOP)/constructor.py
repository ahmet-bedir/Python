### yapıcı metod.
class Personal:
  def __init__(self):
     print("Yapıcı metod!")

nesne1 = Personal() # sınıfın örneklendiği an yapıcı metod çalışır.

###
class Deneme:
    # sınıf niteliği.
    a = 5
    def __init__(self):
        # örnek niteliği.
        self.b = 7

# sınıf niteliğine erişmek için sınıf adını kullanıyoruz.
print("Sınıf niteliği:", Deneme.a)

# örnek niteliğine erişmek için örnek adını kullanıyoruz.
# 1.yöntem
ornek1 = Deneme()
print("Örnek niteliği:", ornek1.b)

# 2.yöntem
print("Örnek niteliği:", Deneme().b)