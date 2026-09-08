import sqlite3

with sqlite3.connect("sqlite.db") as db_connect:
    db_cursor = db_connect.cursor()

    sql = """SELECT * FROM personel;"""
    db_cursor.execute(sql)
    datas = db_cursor.fetchall()
    # veritabanındaki kayıtların uzunluğuna göre tablodaki her kolon uzunluğu otomatik ayarlanıyor.
    filling = 10
    for row in datas:
        if len(row[0]) > filling:
            filling = len(row[0])
        if len(row[1]) > filling:
            filling = len(row[1])
        if len(row[2]) > filling:
            filling = len(row[2])

    counter = 0
    print('+' + '-'*filling + '+' + '-'*filling + '+' + '-'*filling + '+')
    print("|{:^{d}}|{:^{d}}|{:^{d}}|".format("İsim", "Soyisim", "Memleket", d=filling))
    print('+' + '-'*filling + '+' + '-'*filling + '+' + '-'*filling + '+')
    for row in datas:
        counter += 1
        print("|{:<{d}}|{:<{d}}|{:<{d}}|".format(row[0], row[1], row[2], d=filling))
    print('+' + '-'*filling + '+' + '-'*filling + '+' + '-'*filling + '+')

    print(f"Toplam {counter} kayıt.")
