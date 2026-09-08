#1.yöntem
x = int(input("Notunuz : "))

if x > 100 or x < 0:
    print("Yanlış giriş!")
elif x >= 90 and x <= 100:
    print("A aldınız.")
elif x >= 80 and x <= 89:
    print("B aldınız.")
elif x >= 70 and x <= 79:
    print("C aldınız.")
elif x >= 60 and x <= 69:
    print("D aldınız.")
elif x >= 0 and x <= 59:
    print("F aldınız.")
    
#2.yöntem
x = int(input("Notunuz : "))

if x > 100 or x < 0:
    print("Yanlış giriş!")
elif x >= 90 <= 100:
    print("A aldınız.")
elif x >= 80 <= 89:
    print("B aldınız.")
elif x >= 70 <= 79:
    print("C aldınız.")
elif x >= 60 <= 69:
    print("D aldınız.")
elif x >= 0 <= 59:
    print("F aldınız.")
    
#3.yöntem
x = int(input("Notunuz : "))

if x > 100 or x < 0:
    print("Yanlış giriş!")
elif 90 <= x <= 100: #x, 90 ile 100 arasında bir sayı ise
    print("A aldınız.")
elif 80 <= x <= 89: #x, 80 ile 89 arasında bir sayı ise
    print("B aldınız.")
elif 70 <= x <= 79:
    print("C aldınız.")
elif 60 <= x <= 69:
    print("D aldınız.")
elif 0 <= x <= 59:
    print("F aldınız.")
    
#4.yöntem
x = int(input("Notunuz : "))

if x > 100 or x < 0:
    print("Yanlış giriş!")
elif x >= 90:
    print("A aldınız.")
elif x >= 80:
    print("B aldınız.")
elif x >= 70:
    print("C aldınız.")
elif x >= 60:
    print("D aldınız.")
elif x >= 0:
    print("F aldınız.")
