from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

SENTINEL_MODULES = ["Sentinel_Intelligence"]  # Add other intelligence modules here

@app.route('/query_other_intelligence', methods=['POST'])
def query_other():
    data = request.json
    intelligence = data.get("intelligence")  # Name of intelligence module
    query_type = data.get("type")

    if intelligence in SENTINEL_MODULES:
        # Forward request to the correct intelligence API
        api_url = f"http://localhost:5001/query"  # Modify this based on the module
        response = requests.post(api_url, json={"type": query_type})
        return response.json()
    else:
        return jsonify({"error": "Invalid intelligence module"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
