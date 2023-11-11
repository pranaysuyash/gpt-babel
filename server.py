from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from scraper import scrape_data

app = Flask(__name__)
CORS(app, resources={r"/submit-url": {"origins": "http://127.0.0.1:5500"}})  # Enable CORS for the /submit-url route

@app.route('/submit-url', methods=['POST'])
def submit_url():
    data = request.get_json()
    url = data.get('url')
    
    # Validate URL...
    
    result = scrape_data(url)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Could not retrieve data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
