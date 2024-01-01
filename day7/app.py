from flask import Flask, jsonify
from googlesearch import search
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/<string:query>", methods=['GET', 'POST'])
def index(query):
    result = search(
        query=query, 
        tld="co.in", 
        num=10, 
        stop=10, 
        pause=2
    )
    search_links = list(result)
    return jsonify(search_links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6012)