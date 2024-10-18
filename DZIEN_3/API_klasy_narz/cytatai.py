from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Lokalna baza cytatów
quotes = [
    {"id": 1, "quote": "Nie czekaj. Nigdy nie będzie odpowiedniego momentu.", "author": "Napoleon Hill"},
    {"id": 2, "quote": "Sukces to suma niewielkich wysiłków, powtarzanych dzień po dniu.", "author": "Robert Collier"},
    {"id": 3, "quote": "Twoje życie staje się lepsze tylko, gdy Ty stajesz się lepszy.", "author": "Brian Tracy"}
]


# Endpoint zwracający losowy cytat
@app.route('/random', methods=['GET'])
def get_random_quote():
    quote = random.choice(quotes)
    return jsonify(quote)


# Endpoint zwracający wszystkie cytaty
@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)


# Endpoint do dodania nowego cytatu
@app.route('/quotes', methods=['POST'])
def add_quote():
    new_quote = request.get_json()
    new_quote["id"] = len(quotes) + 1
    quotes.append(new_quote)
    return jsonify(new_quote), 201


# Endpoint do wyszukiwania cytatów po autorze lub treści
@app.route('/search', methods=['GET'])
def search_quotes():
    search_term = request.args.get('q', '').lower()
    results = [quote for quote in quotes if
               search_term in quote['quote'].lower() or search_term in quote['author'].lower()]

    if not results:
        return jsonify({"message": "Nie znaleziono cytatów."}), 404

    return jsonify(results)


# Endpoint do pobrania konkretnego cytatu po ID
@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_quote_by_id(quote_id):
    quote = next((q for q in quotes if q['id'] == quote_id), None)
    if quote is None:
        return jsonify({"error": "Cytat nie znaleziony"}), 404
    return jsonify(quote)


if __name__ == '__main__':
    app.run(debug=True)
