import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def get_sql_data(p_id=None):
    products = []
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    if p_id:
        cursor.execute('SELECT * FROM Products WHERE id = ?', (p_id,))
    else:
        cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    for row in rows:
        products.append(dict(row))
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    p_id = request.args.get('id', type=int)

    # 1. Source yoxlanışı
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Məlumatın götürülməsi
    if source == 'json':
        data = get_json_data()
    elif source == 'csv':
        data = get_csv_data()
    elif source == 'sql':
        data = get_sql_data(p_id)
        if p_id and not data:
            return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=data)

    # 3. JSON və CSV üçün ID filteri
    if p_id:
        data = [p for p in data if p['id'] == p_id]
        if not data:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
