from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint powitalny
@app.route('/')
def welcome():
    return jsonify({"message": "Witaj w prostym API!"})

# Endpoint zwracający odwrócony tekst
@app.route('/reverse', methods=['POST'])
def reverse_string():
    data = request.get_json()
    text = data.get('text', '')
    reversed_text = text[::-1]
    return jsonify({"original": text, "reversed": reversed_text})

# Endpoint do sprawdzania palindromu
@app.route('/is_palindrome', methods=['POST'])
def is_palindrome():
    data = request.get_json()
    text = data.get('text', '')
    is_palindrome = text == text[::-1]
    return jsonify({"text": text, "is_palindrome": is_palindrome})

if __name__ == '__main__':
    app.run(debug=True)
