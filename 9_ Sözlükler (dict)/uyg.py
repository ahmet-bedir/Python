telefon_defteri = {
    "ahmet öz" : "0532 532 32 32",
    "mehmet su": "0543 543 42 42",
    "seda naz" : "0533 533 33 33",
    "eda ala"  : "0212 212 12 12"
}

kisi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")
if kisi in telefon_defteri:
    cevap = "{} adlı kişinin telefon numarası: {}"
    print(cevap.format(kisi, telefon_defteri[kisi]))
else:
    cevap = "{} adlı kişi bulunmamaktadır!"
    print(cevap.format(kisi))
