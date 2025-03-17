import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Securely access API key from environment variables
API_KEY = os.getenv("SECRET_API_KEY")

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

    # Make a request to the actual AI API (Example: OpenAI, Custom DB, etc.)
    response = requests.get(f"https://sentinel-api-x6ks.onrender.com", headers=headers)
    
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
