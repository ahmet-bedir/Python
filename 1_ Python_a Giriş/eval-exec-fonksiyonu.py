###
#print(eval("a = 3")) #hata.!

# exec("a = 3")
# print("a =", a)


# ###
# i = '7 * 3'
# print("7 * 3 =", eval(i))

# i = 'print("Hello Python.!")'
# islem = eval(i)
# print(islem)

# exec("a = '#'; b = 15; print(a*b)")


    
# ###
# d1 = """
# Python'da ekrana çıktı verebilmek için 
# print() adlı bir fonksiyondan yararlanıyoruz...
# Bu fonksiyonu şöyle kullanabilirsiniz:

# >>> print("Merhaba Dünya")

# Şimdi de aynı kodu siz yazın!

# >>> """

# girdi = input(d1)

# exec(girdi)

# d2 = """
# Gördüğünüz gibi print() fonksiyonu,
# kendisine parametre olarak verilen
# değerleri ekrana basıyor... 

# Böylece ilk dersimizi tamamlamış olduk.
# Şimdi bir sonraki dersimize geçebiliriz...
# """

# print(d2)


# ❌ Tip dönüşümü gibi kullanmak tehlikeli
data = eval(input("Giriş: "))

print(data)
# Kullanıcı şunu girerse:
# __import__('os').system('rm -rf /')  → Tüm sistemi siler!
# __import__('os').system('cat /etc/passwd')  → Şifreleri okur!

###
import ast

a = ast.literal_eval(input("Güvenli Giriş: "))

print(a)
# ast.literal_eval tehlikeli kodu çalıştırmaz:
# ast.literal_eval("__import__('os').system('ls')")  # ValueError!

