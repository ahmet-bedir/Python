import mysql.connector

dbConnect = mysql.connector.connect(
    host="127.0.0.1",
    user="user1",
    password="u1",
    database="storedb"
)

dbCursor = dbConnect.cursor()
sql = """SELECT * FROM products
INNER JOIN categories ON products.categoryid = categories.category_id;"""

sql = """SELECT products.product_name, products.price,
products.product_image, products.description,
categories.category_name FROM products
INNER JOIN categories ON products.categoryid = categories.category_id;"""

# sql = """SELECT products.product_name, products.price, products.product_image, products.description, categories.category_name FROM products INNER JOIN categories ON products.categoryid = categories.category_id WHERE categories.category_name = 'telefon';"""

# sql = """
# SELECT p.product_name, p.price, p.product_image,
# p.description, c.category_name
# FROM products AS p 
# INNER JOIN categories AS c ON p.categoryid = c.category_id
# WHERE c.category_name = 'telefon';"""


dbCursor.execute(sql)
try:
    result = dbCursor.fetchall()
    for product in result:
        print(product)
except mysql.connector.Error as err:
    print('hata:', err)
finally:
    dbConnect.close()
    print('database bağlantısı kapandı.')
