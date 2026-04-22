from flask import Flask, jsonify, request

app = Flask(__name__)

# İstifadəçiləri yaddaşda saxlamaq üçün lüğət
users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    # Bütün istifadəçi adlarının siyahısını qaytarır
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    # JSON-u parse edirik. Əgər JSON formatı yanlışdırsa, None qaytarır.
    data = request.get_json(silent=True)
    
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    
    username = data.get("username")
    
    # Şərt 1: İstifadəçi adı mütləqdir
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    # Şərt 2: İstifadəçi adı artıq mövcuddursa (FAIL olan hissə buradır)
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    
    # İstifadəçini əlavə edirik
    users[username] = data
    
    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201

if __name__ == "__main__":
    app.run()
