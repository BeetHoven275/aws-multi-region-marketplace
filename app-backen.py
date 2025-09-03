from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)


USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

# Helpers
def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)
    with open(USERS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def find_user_by_email(email):
    users = load_users()
    for user in users:
        if user['email'] == email:
            return user
    return None

# Routes
@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    confirm_password = data.get('confirmPassword')

    if not all([name, email, password, confirm_password]):
        return jsonify({'success': False, 'message': 'Please fill in all fields.'})

    if password != confirm_password:
        return jsonify({'success': False, 'message': 'Passwords do not match.'})

    if find_user_by_email(email):
        return jsonify({'success': False, 'message': 'Email already registered.'})

    users = load_users()
    users.append({
        'name': name,
        'email': email,
        'password': password 
    })
    save_users(users)
    return jsonify({'success': True, 'message': 'Registration successful! Please login.'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = find_user_by_email(email)
    if user and user['password'] == password:
        return jsonify({'success': True, 'message': f'Welcome back, {user["name"]}!'})
    else:
        return jsonify({'success': False, 'message': 'Invalid email or password.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
