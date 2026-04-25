import json
from flask import Flask, render_template

app = Flask(__name__)

# Əvvəlki tapşırıqdakı əsas marşrut (isteğe bağlı)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r') as f:
            data = json.load(f)
            # "items" açarının içindəki siyahını alırıq
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fayl yoxdursa və ya xətalıdırsa boş siyahı göndəririk
        items_list = []

    # Məlumatı şablona (template) göndəririk
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
