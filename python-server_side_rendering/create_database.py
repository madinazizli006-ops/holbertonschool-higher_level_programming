import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    # Cədvəli yaradırıq
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Məlumatları əlavə edirik
    cursor.execute('DELETE FROM Products') # Köhnə məlumat varsa təmizləyirik
    cursor.execute("INSERT INTO Products VALUES (1, 'Laptop', 'Electronics', 799.99)")
    cursor.execute("INSERT INTO Products VALUES (2, 'Coffee Mug', 'Home Goods', 15.99)")
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
