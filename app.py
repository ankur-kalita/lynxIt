from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
import json
import difflib
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  

with open('dictionary.json', 'r') as f:
    dictionary = json.load(f)

CREDENTIALS = {
    "admin": generate_password_hash("password123")
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@login_required
def index():
    return render_template('dictionary.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in CREDENTIALS and check_password_hash(CREDENTIALS[username], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid credentials. Please try again.'
    
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/search', methods=['GET'])
@login_required
def search():
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({"exact_match": None, "suggestions": []})
    
    exact_match = None
    if query.lower() in dictionary:
        exact_match = {"word": query.lower(), "meaning": dictionary[query.lower()]}
    
    suggestions = []
    if not exact_match:
        close_matches = difflib.get_close_matches(query.lower(), dictionary.keys(), n=5, cutoff=0.6)
        suggestions = [{"word": word, "meaning": dictionary[word]} for word in close_matches]
    
    return jsonify({"exact_match": exact_match, "suggestions": suggestions})

if __name__ == '__main__':
    app.run(debug=True)
