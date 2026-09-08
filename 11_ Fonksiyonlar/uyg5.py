def istatistik(sayilar):
    """Bir sayı listesinin min, max ve ortalamasını döndürür."""
    en_kucuk = min(sayilar)
    en_buyuk = max(sayilar)
    ortalama = sum(sayilar) / len(sayilar)
    return en_kucuk, en_buyuk, ortalama

notlar = [70, 85, 90, 65, 78, 92]
minimum, maksimum, ort = istatistik(notlar)
print(f"Min: {minimum}, Max: {maksimum}, Ort: {ort:.1f}")
# Min: 65, Max: 92, Ort: 80.0

###
def ad_soyad_ayir(tam_ad):
    """Tam adı ad ve soyad olarak ayırır."""
    parcalar = tam_ad.strip().split()
    ad = parcalar[0]
    soyad = parcalar[-1] if len(parcalar) > 1 else ""
    return ad, soyad

ad, soyad = ad_soyad_ayir("Ahmet Yılmaz")
print(f"Ad: {ad}, Soyad: {soyad}")  # Ad: Ahmet, Soyad: Yılmaz

### Docstring, fonksiyonun hemen altına yazılan üçlü tırnak ("""...""") içindeki açıklama metnidir. Bu sadece bir yorum değil — Python bunu fonksiyonun __doc__ attribute'una kaydeder.
def bmi_hesapla(kilo, boy):
    """Vücut kitle indeksini (BMI) hesaplar.
    
    Args:
        kilo (float): Kilogram cinsinden ağırlık
        boy (float): Metre cinsinden boy
    
    Returns:
        float: BMI değeri
    
    Examples:
        >>> bmi_hesapla(70, 1.75)
        22.857142857142858
    """
    return kilo / (boy ** 2)

# Docstring yazdığında help() fonksiyonu ile o belgeye erişebilirsin:
#help(bmi_hesapla)

# Ayrıca __doc__ attribute'u ile doğrudan docstring'e erişebilirsin:
print(bmi_hesapla.__doc__)