import os
from flask import Flask, request, jsonify

# Load API key from environment variables
API_KEY = os.getenv("04102017Qd")

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Sentinel API is running!"})

@app.route("/secure-endpoint", methods=["GET"])
def secure_endpoint():
    # Get the API key from the request headers
    provided_key = request.headers.get("Authorization")

    if provided_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 403
    
    return jsonify({"message": "Access granted to secure data!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
