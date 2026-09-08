sayi = int(input('Üç Basamaklı Bir Sayı Giriniz : '))

uzunluk = len(str(sayi))

birler = sayi % 10
onlar = (sayi // 10) % 10
yuzler = sayi // 100

if uzunluk == 3:
  print("birler basamağı", birler)
  print("onlar basamağı", onlar)
  print("yüzler basamağı", yuzler)
elif uzunluk == 2:
  print("birler basamağı", birler)
  print("onlar basamağı", onlar)
else:
  print("birler basamağı", birler)
