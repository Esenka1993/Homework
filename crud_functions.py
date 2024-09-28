import sqlite3

def initiate_db(pr_file="products.db"):
    connection = sqlite3.connect(pr_file)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, title TEXT NOT NULL, description TEXT, price INTEGER NOT NULL)""")
    for i in range(1, 5):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                       (f'Product{i}', f'Описание{i}', i * 100))

    connection.commit()
    connection.close()

def get_all_products(pr_file="products.db"):
    connection = sqlite3.connect(pr_file)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    pr = cursor.fetchall()
    connection.close()
    return pr




