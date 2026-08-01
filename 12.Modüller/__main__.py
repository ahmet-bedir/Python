"""
Her Python dosyasının özel bir __name__ değişkeni var:

Dosya doğrudan çalıştırılırsa __name__ değeri: __name__ = "__main__" olur

Dosya import edilirse __name__ değeri: __name__ = modül adı olur
"""

if __name__ == "__main__":
    # Bu kod sadece dosya doğrudan çalıştırıldığında çalışır
    pass

# hesapla.py
print(f"__name__ = {__name__}")

def topla(a, b):
    return a + b

if __name__ == "__main__":
    # Test kodu — sadece doğrudan çalışınca
    print(topla(3, 5))