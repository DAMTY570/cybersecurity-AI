import hashlib
import os

# Chemin absolu vers le fichier de clé
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "..", "data", "file_key.key")

# Chargement dynamique de la clé de chiffrement depuis le fichier
with open(KEY_PATH, "rb") as f:
    ENCRYPTION_KEY = f.read()

# Clé API
API_KEY = "super_secret_api_key"
API_KEY_HASH = hashlib.sha256(API_KEY.encode()).hexdigest()
