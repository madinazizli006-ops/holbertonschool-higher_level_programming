import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON oxuma funksiyası
def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

# CSV oxuma funksiyası
def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# SQL oxuma funksiyası
def read_sql(product_id=None):
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # Sətirləri lüğət (dictionary) formatında almaq üçün:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
            
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    # Mənbə yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    products = []
    
    # Mənbəyə görə məlumatın çəkilməsi
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql(product_id)
        # SQL-də filteri birbaşa query-də etdiyimiz üçün burada dayanırıq
        if product_id and not products:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)

    # JSON və CSV üçün filterləmə (çünki onlar bütün faylı oxuyur)
    if product_id:
        products = [p for p in products if p['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
