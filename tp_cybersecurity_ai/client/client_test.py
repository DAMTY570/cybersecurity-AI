import requests
from cryptography.fernet import Fernet
import os

# Charger la clé depuis file_key.key
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "..", "data", "file_key.key")

with open(KEY_PATH, "rb") as f:
    ENCRYPTION_KEY = f.read()

API_KEY = "super_secret_api_key"
fernet = Fernet(ENCRYPTION_KEY)

# Données test
hours = 5.0
previous = 70.0
plaintext = f"{hours},{previous}"
encrypted = fernet.encrypt(plaintext.encode()).decode()

# Envoi de la requête POST
response = requests.post(
    "https://86be-46-193-68-8.ngrok-free.app/predict",
    json={"data": encrypted},
    headers={"x-api-key": API_KEY}
)

try:
    print("Réponse JSON :", response.json())
except Exception as e:
    print("Erreur JSON :", e)
print("Statut HTTP :", response.status_code)
print("Contenu brut :", response.text)


