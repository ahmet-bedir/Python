import psycopg

db_connect = psycopg.connect(
    host="127.0.0.1",
    dbname="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)

db_cursor = db_connect.cursor()

sql = """
CREATE TABLE IF NOT EXISTS public.users (
	user_id SERIAL,
	user_name VARCHAR(20) NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id)
);"""

db_cursor.execute(sql)
db_connect.commit()

sql = """
INSERT INTO users
    (user_name)
VALUES
    ('ahmet'),
    ('ali');
"""

db_cursor.execute(sql)
db_connect.commit()

sql = """SELECT * FROM users;"""
db_cursor.execute(sql)
user_list = db_cursor.fetchall()
for user in user_list:
    print(f"{user[0]} -> {user[1]}")
  
db_connect.close()