def sablon_uygula(sablon, **degiskenler):
    """Basit şablon motoru — {degisken} yerine değer koy"""
    sonuc = sablon
    for anahtar, deger in degiskenler.items():
        sonuc = sonuc.replace("{" + anahtar + "}", str(deger))
    return sonuc

sablon = """
Sayın {isim},

{tarih} tarihli siparişiniz #{siparis_no} hazırlanmıştır.
Toplam tutar: ₺{tutar}

Teşekkür ederiz.
"""

mesaj = sablon_uygula(
    sablon,
    isim="Ali Yılmaz",
    tarih="2024-01-15",
    siparis_no=12345,
    tutar="249.90"
)
print(mesaj)
