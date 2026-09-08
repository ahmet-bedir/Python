while True:
  kelime = input("Kelime Giriniz : ")
  uzunluk = len(kelime)
  tersi = ""
  while 0 < uzunluk:
    tersi += kelime[uzunluk-1]
    uzunluk -= 1
  print("Kelimenin Tersi : ", tersi)
  if kelime == tersi:
    print("Palindomik Kelime...",
    "Çıkılıyor...", sep="\n")
    break
  else:
    print("Palindomik Kelime Değil...")
