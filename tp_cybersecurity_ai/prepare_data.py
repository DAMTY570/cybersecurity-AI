import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from cryptography.fernet import Fernet
import os
from io import StringIO

# 1. Générer une clé
key = Fernet.generate_key()
fernet = Fernet(key)

# Sauvegarder la clé
key_path = "data/file_key.key"
with open(key_path, "wb") as f:
    f.write(key)

# 2. Lire et chiffrer les données
csv_path = "data/Student_Performance.csv"
df = pd.read_csv(csv_path)
data_str = df.to_csv(index=False)
encrypted_data = fernet.encrypt(data_str.encode())

enc_path = "data/Student_Performance_encrypted.csv"
with open(enc_path, "wb") as f:
    f.write(encrypted_data)

# 3. Déchiffrer pour entraînement
with open(enc_path, "rb") as f:
    encrypted_content = f.read()
decrypted = fernet.decrypt(encrypted_content).decode()
df_decrypted = pd.read_csv(StringIO(decrypted))

# 4. Sample et préparation
df_sample = df_decrypted.sample(n=2000, random_state=42)
X = df_sample[["Hours Studied", "Previous Scores"]]
y = df_sample["Performance Index"]

# 5. Entraîner un modèle
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, preds))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# 6. Sauvegarde
joblib.dump(model, "model/linear_model.pkl")
