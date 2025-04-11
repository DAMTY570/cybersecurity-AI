### `tp_cybersecurity_ai/README.md`

```markdown
# TP - Sécurité des Données et Intelligence Artificielle

Ce projet met en œuvre un pipeline complet de chiffrement, modélisation, et sécurisation d'une API prédictive. Il est divisé en 3 grandes parties : préparation des données, création d’une API Flask, et renforcement de la sécurité.

---

## Structure du projet

```
tp_cybersecurity_ai/
├── data/                         # Données sources et clés
│   ├── Student_Performance.csv
│   ├── Student_Performance_encrypted.csv
│   └── file_key.key
│
├── model/                        # Modèle sauvegardé
│   └── linear_model.pkl
│
├── api/                          # Code de l’API Flask
│   ├── app.py
│   └── secrets.py
│
├── client/                       # Script client test
│   └── client_test.py
│
├── prepare_data.py              # Préparation et entraînement du modèle
├── requirements.txt             # Dépendances Python
└── README.md
```

---

##  Étapes réalisées

###  Partie 1 : Préparation des données

- Génération d'une **clé de chiffrement Fernet**
- Chiffrement du fichier `Student_Performance.csv`
- Déchiffrement pour entraînement du modèle
- Sélection de variables (`Hours Studied`, `Previous Scores`) → `Performance Index`
- Entraînement d'un **modèle de régression linéaire**
- Sauvegarde du modèle avec `joblib`

###  Partie 2 : Création de l’API Flask

- API Flask exposée localement (`http://127.0.0.1:5000`)
- Route `/predict` :
  - Reçoit des données chiffrées
  - Vérifie la clé API (`x-api-key`)
  - Retourne la prédiction du modèle
- Possibilité d’exposer l’API publiquement avec `ngrok`

###  Partie 3 : Renforcement de la sécurité 

| Sécurité                  | Implémentée | Description |
|---------------------------|-------------|-------------|
| 🔐 Chiffrement des données | ✅           | Le client chiffre les entrées avec `Fernet`. |
| 🗝️ Authentification         | ✅           | L’API vérifie la clé `x-api-key`.            |
| 🔒 Hachage SHA-256         | ✅           | Le serveur compare le **hash** de la clé API. |

---

##  Utilisation

### 1. Préparer les données et entraîner le modèle

```bash
python3 prepare_data.py
```

### 2. Lancer l’API Flask

```bash
python3 -m tp_cybersecurity_ai.api.app
```

Accessible sur : `http://127.0.0.1:5000`

### 3. Tester avec le client sécurisé

```bash
python3 tp_cybersecurity_ai/client/client_test.py
```

---

## Exposer l’API avec Ngrok

```bash
ngrok http 5000
```

Utilise ensuite l’URL générée (`https://xxxxx.ngrok-free.app/predict`) dans `client_test.py` pour tester l’API depuis l’extérieur.

---

## Dépendances

```
flask
joblib
cryptography
requests
scikit-learn
```

Installe-les avec :

```bash
pip install -r requirements.txt
```

---

## Auteur

Abraham Krah  
M2 IA School · TP Sécurité des Données & IA – 2025
```

