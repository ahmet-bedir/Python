import mysql.connector as mysql
from datetime import date
from decimal import Decimal

class Urun:
    def __init__(self):
        self.baglanti = mysql.connect(
            host = "127.0.0.1",
            user = "user1",
            password = "u1",
            database = "storedb")
        
    ###
    def urunEkle(self, urun_adi, fiyat, url, aciklama):
        self.urun_adi = urun_adi
        self.fiyat = fiyat
        self.url = url
        self.aciklama = aciklama

        imlec = self.baglanti.cursor()
        sql = """INSERT INTO products (product_name, price, product_image, description)
        VALUES (%s,%s,%s,%s);"""
        degerler = (self.urun_adi,
                    self.fiyat,
                    self.url,
                    self.aciklama)
        imlec.execute(sql, degerler)  # execute fonksiyonu, değer(value) olarak demet(tuple) alır.
        try:
            self.baglanti.commit()
            print(f'{imlec.rowcount} tane kayıt eklendi')
            print(f'son eklenen kaydın id: {imlec.lastrowid}')
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            print('database bağlantısı kapandı.')
            
    ###
    def cokUrunEkle(self, liste):
        self.liste = liste

        imlec = self.baglanti.cursor()
        sql = """INSERT  INTO products (product_name, price, product_image, description)
        VALUES (%s,%s,%s,%s);"""
        degerler = self.liste
        imlec.executemany(sql,degerler)  # executemany fonksiyonu, değer(value) olarak liste(list) alır.
        try:
            self.baglanti.commit()
            print(f'{imlec.rowcount} tane kayıt eklendi')
            print(f'son eklenen kaydın id: {imlec.lastrowid}')
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            print('database bağlantısı kapandı.')
            
    ###
    def urunListesi(self):
        imlec = self.baglanti.cursor()
        sql = """SELECT * FROM products;"""  # Tüm kayıtları çekmek istediğimiz için * kullanırız.

        sql = """SELECT * FROM products ORDER BY product_name DESC;""" # product_name'na göre azalan sırada sıralamak istediğimiz için ORDER BY kullanırız. Ve DESC ile azalan sırada sıralarız. Eğer artan sırada sıralamak istiyorsak ASC kullanırız.

        sql = """SELECT product_name, price, product_image, description,
        registration_date FROM products;"""  # Sadece belirli sütunları çekmek istediğimiz için * yerine sütun adlarını yazarız.
        imlec.execute(sql)
        try:
            liste = imlec.fetchall() #fetchall fonksiyonu, tüm kayıtları liste(list) olarak döndürür.
            for urun in liste:
                isim, fiyat, resim, aciklama, tarih = urun
                fiyat_yazi = f"{Decimal(str(fiyat)):.2f}" if isinstance(fiyat, Decimal) else f"{float(fiyat):.2f}"
                tarih_yazi = tarih.strftime("%d/%m/%Y") if isinstance(tarih, date) else str(tarih)
                print(f"{isim} | {fiyat_yazi} TL | {resim} | {aciklama} | {tarih_yazi}")
                
            # tekKayit = imlec.fetchone() #fetchone fonksiyonu, tek bir kayıt döndürür. Eğer birden fazla kayıt varsa, ilk kaydı döndürür. Eğer hiç kayıt yoksa, None döndürür.
            # print(tekKayit)
        except mysql.Error as err:
            print('hata:', err)
        finally:
            self.baglanti.close()
            
    ###
    def urunId(self, id):
        imlec = self.baglanti.cursor()
        sql = """SELECT * FROM products WHERE product_id=%s""" #id'ye göre kayıt çekmek istediğimiz için, id'yi parametre olarak alırız. Ve sql sorgusunda %s ile id'yi belirtiriz.
        urunId = (id,) #id'yi demet(tuple) olarak tanımlarız. Çünkü execute fonksiyonu, değer(value) olarak demet(tuple) alır.
        imlec.execute(sql,urunId)
        sonuc = imlec.fetchone()
        fiyat_yazi = f"{Decimal(str(sonuc[2])):.2f}" if isinstance(sonuc[2], Decimal) else f"{float(sonuc[2]):.2f}"
        print(f'id: {sonuc[0]}\nÜrün adı: {sonuc[1]}\nFiyat: {fiyat_yazi} TL')
        self.baglanti.close()
        
    ###
    def urunBilgisi(self):
        imlec = self.baglanti.cursor()

        sql = """SELECT COUNT(*) FROM products;""" #products tablosundaki kayıt sayısını çekmek istediğimiz için COUNT(*) kullanırız.
        sql = """SELECT AVG(price) FROM products;""" #products tablosundaki fiyat ortalamasını çekmek istediğimiz için AVG() kullanırız.
        sql = """SELECT SUM(price) FROM products;""" #products tablosundaki fiyat toplamını çekmek istediğimiz için SUM() kullanırız.
        sql = """SELECT MIN(price) FROM products;""" #products tablosundaki en düşük fiyatı çekmek istediğimiz için MIN() kullanırız.
        sql = """SELECT MAX(price) FROM products;"""  # products tablosundaki en yüksek fiyatı çekmek istediğimiz için MAX() kullanırız.
        sql = """SELECT product_name,price FROM products
        WHERE price = (SELECT MAX(price) FROM products);"""  # products tablosundaki en yüksek fiyata sahip ürünleri çekmek istediğimiz için bu sorguyu kullanırız.

        imlec.execute(sql)

        sonuc = imlec.fetchone()    

        print(f'En Pahalı Ürün: {sonuc[0]} - Fiyat: {sonuc[1]} - Kayıt Tarihi:')
        self.baglanti.close()

        
###
# nesneUrunEkle = Urun()
# nesneUrunEkle.urunEkle("dell laptop",21000,"dell.jpg","dizüstü bilgisayar")

###
# liste = [
# ('android tv',20000,'and.png','hd'),
# ('elektirikli süpürge',15000,'supurge.jpeg','sil süpür'),
# ('lc tv',20000,'lcd.png','full hd'),
# ('dell laptop',15000,'dell.jpeg','güçlü pc'),
# ('samsung s3',15000,'tel.jpeg','akıllı tel')
# ]
# nesneCokUrunEkle = Urun()
# nesneCokUrunEkle.cokUrunEkle(liste)

###
nesneUrunleriListele = Urun()
nesneUrunleriListele.urunListesi()
print('-'*75)

###
nesneUrunId = Urun()
nesneUrunId.urunId(1)
print('-'*75)

###
nesneUrunBilgisi = Urun()
nesneUrunBilgisi.urunBilgisi()
