import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


connect = create_connection('hw.db')

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL, 
price DOUBLE(8, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) DEFAULT 0
)
'''


def insert_product(conn, product):
    sql = '''
    INSERT INTO products (product_title, price, quantity) 
    VALUES (?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_by_quan(conn, product):
    sql = '''
    UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_product_by_price(conn, product):
    sql = '''
    UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, id):
    sql = '''
    DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_p_q(conn, limit, limit2):
    sql = '''SELECT * FROM products WHERE price < ? and quantity > ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (limit, limit2))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_title(conn, title):
    sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (title,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


if connect is not None:
    print('Connected successfully')

# create_table(connect, sql_create_products_table)
# insert_product(connect, ('Milk', 70.00, 20))
# insert_product(connect, ('Eggs', 110.00, 10))
# insert_product(connect, ('Beer', 90.00, 35))
# insert_product(connect, ('Snickers bar', 45.00, 50))
# insert_product(connect, ('Mars bar', 42.00, 60))
# insert_product(connect, ('Greenfield tea', 130.00, 30))
# insert_product(connect, ('Tess tea', 105.00, 45))
# insert_product(connect, ('Jardin coffee', 250.00, 15))
# insert_product(connect, ('Jockey coffee', 180.00, 32))
# insert_product(connect, ('Lays', 95.00, 12))
# insert_product(connect, ('Oreo', 55.00, 10))
# insert_product(connect, ('Coke', 50.00, 15))
# insert_product(connect, ('Sprite', 48.00, 17))
# insert_product(connect, ('Waffles', 60.00, 22))
# insert_product(connect, ('Truffles', 120.00, 5))

# update_product_by_quan(connect, (58, 1))
# update_product_by_price(connect, (100, 3))
# delete_product(connect, 13)
# select_all_products(connect)
# select_products_by_p_q(connect, 100, 5)
select_products_by_title(connect, '%bar')