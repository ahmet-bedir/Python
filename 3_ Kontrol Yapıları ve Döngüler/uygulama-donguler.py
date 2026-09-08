###
tr_harfler = "çÇğĞıİöÖşŞüÜ"
parola = input("Parola Belirleyiniz : ")

for karakter in parola: #parola değişkenine girdiğimiz her karakteri tek tek karakter adlı değişkene attık.
    if karakter in tr_harfler: #karakter değişkenindeki her bir karakterin tr_harfler değişkenindeki karakterlerde olup olmadığına bakıyoruz.
        print("""Parolada Türkçe Karakter Kullanılamaz...
Lütfen Tekrar Deneyin!""")
        exit()
    
print("""Parolanız Başarılı Bir Şekilde Oluşturulmuştur...
Parolanız :""", parola)

###
tr_harfler = "çÇğĞıİöÖşŞüÜ"
while True:
  parola = input("Parola Belirleyiniz : ")
  for karakter in parola:
      if karakter in tr_harfler:
          print("Parolada Türkçe Karakter Kullanılamaz...")
          break
  else:
      print("Parolanız :", parola)
      break

###
while True:
    parola = input("Parola Belirleyiniz : ")
    if ' ' in parola:
        print("Parolanızda Boşluk Olmamalı.!")
    elif len(parola) in range(3, 9): #eğer parolanızın uzunluğu 2 ile 9 karakter aralığında ise...
        print("Parolalanız :", parola)
        break
    else:
        print("Parola 8 Karakterden Uzun, 3 Karakterden Kısa Olmamalı...")


#### metindeki her bir karakteri bir kere ekrana yaz...
metin = "python programlama dili..."

karakterler = ''
for harf in metin:
    if harf in metin and harf not in karakterler:
        karakterler += harf
print(*karakterler)