from flask import Flask, request, jsonify
import joblib
import numpy as np
from cryptography.fernet import Fernet
import hashlib
from .secrets import ENCRYPTION_KEY, API_KEY_HASH

app = Flask(__name__)
model = joblib.load("model/linear_model.pkl")
fernet = Fernet(ENCRYPTION_KEY)

def verify_key(client_key):
    return hashlib.sha256(client_key.encode()).hexdigest() == API_KEY_HASH

@app.route("/")
def home():
    return "Bienvenue sur l’API de prédiction de performance étudiante !"

@app.route("/predict", methods=["POST"])
def predict():
    api_key = request.headers.get("x-api-key")
    if not api_key or not verify_key(api_key):
        return jsonify({"error": "Unauthorized"}), 401

    encrypted_data = request.json.get("data")
    if not encrypted_data:
        return jsonify({"error": "Missing data"}), 400

    decrypted = fernet.decrypt(encrypted_data.encode()).decode()
    hours, previous = map(float, decrypted.split(","))
    prediction = model.predict(np.array([[hours, previous]]))[0]
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(port=5000)
