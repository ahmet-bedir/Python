import sqlite3
# Yeni veritabanı oluşturmak için connect() metodu kullanılır. Eğer bu dizin içinde sqlite.db adlı bir veritabanı yoksa, bu ada sahip bir veritabanı oluşturulacaktır. Halihazırda bi veritabanı varsa connect() metodu yardımıyla bağlanırız.
db_connect = sqlite3.connect('sqlite.db')
db_cursor = db_connect.cursor()

# yeni tablo oluşturma.
# sql = """CREATE TABLE personel (id, isim, soyisim, memleket);"""
# db_cursor.execute(sql)

# koşullu tablo oluşturma (aynı isimde tablo varsa hata vermez, yoksa yeni bir tablo oluşturur).
# sql = """CREATE TABLE IF NOT EXISTS personel (id, isim, soyisim, memleket);"""
# db_cursor.execute(sql)

# tabloya veri girişi.
sql = """INSERT INTO personel (isim, soyisim, memleket) VALUES ('ali','tel','adana');"""
db_cursor.execute(sql)
db_connect.commit()
print("Kayıt Eklendi...")

print()
print("Bağlantı nesnesinin metodları:", dir(db_connect), sep='\n')
print()
print("İmleç metodları:", dir(db_cursor), sep='\n')

# tabloyu listeleme.
sql = """SELECT * FROM personel;"""
db_cursor.execute(sql)
table_list = db_cursor.fetchall()
print("Tablo Listesi:")
for i in table_list:
    print(i)

db_connect.close()
