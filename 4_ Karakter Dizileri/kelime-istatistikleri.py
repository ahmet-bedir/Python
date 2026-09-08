def kelime_istatistik(metin):
    """Metin istatistikleri hesapla"""
    kelimeler = metin.split()
    karakterler = len(metin)
    kelime_sayisi = len(kelimeler)
    cumle_sayisi = metin.count(".") + metin.count("!") + metin.count("?")
    benzersiz = len(set(k.lower().strip(".,!?;:") for k in kelimeler))
    
    print(f"Karakter sayısı: {karakterler}")
    print(f"Kelime sayısı:   {kelime_sayisi}")
    print(f"Cümle sayısı:    {cumle_sayisi}")
    print(f"Benzersiz kelime: {benzersiz}")
    
    if kelime_sayisi > 0:
        ort = karakterler / kelime_sayisi
        print(f"Ort. kelime uzunluğu: {ort:.1f}")

metin = "Python çok güzel bir dil. Python öğrenmek kolay. Herkes Python öğrenmeli!"
kelime_istatistik(metin)