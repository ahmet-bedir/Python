import sqlite3

with sqlite3.connect('sqlite.db') as db_connect:
	db_cursor = db_connect.cursor()
	sql = """CREATE TABLE IF NOT EXISTS personel
	(isim, soyisim, memleket);"""
	db_cursor.execute(sql)

	datas = [('Fırat', 'Özgül', 'Adana'),
			   ('Ahmet', 'Söz', 'Bolvadin'),
			   ('Veli', 'Göz', 'İskenderun'),
			   ('Mehmet', 'Öz', 'Kilis')]

	# for data in datas:
	#	sql = """INSERT INTO personel VALUES (?, ?, ?);"""
	# 	db_cursor.execute(sql, data)
	# db_connect.commit()

	sql = """INSERT INTO personel VALUES (?, ?, ?);"""
	db_cursor.executemany(sql, datas)
	db_connect.commit()
