# veritabani.py
"""Veritabanı yardımcı modülü."""

def baglan(host, port):
    """Veritabanına bağlanır."""
    print(f"Bağlanılıyor: {host}:{port}")
    return {"baglanti": True}

def sorgu_calistir(baglanti, sql):
    """SQL sorgusu çalıştırır."""
    print(f"Sorgu: {sql}")
    return []

# Bu pattern olmadan test kodu her import'ta çalışır!
if __name__ == "__main__":
    # Modülü test et
    conn = baglan("localhost", 5432)
    sonuc = sorgu_calistir(conn, "SELECT * FROM users")
    print(f"Sonuç: {sonuc}")
    
"""
if __name__ == "__main__": olmadan baglan() ve sorgu_calistir() test kodları, modül import edildiğinde de çalışırdı. Bu pattern ile test kodunu izole edersin.

Bu pattern ayrıca bir dosyanın hem modül hem de script olarak kullanılmasını sağlar. Çok yaygın bir Python convention'ıdır.
"""