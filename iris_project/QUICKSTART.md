# 🚀 Quick Start Guide

Ce guide vous permet de démarrer l'application Iris Predictor en quelques minutes.

## Option 1 : Docker (Recommandé) 🐳

### Prérequis
- Docker installé
- Docker Compose installé

### Étapes

```bash
# 1. Se placer dans le dossier du projet
cd iris_project

# 2. Construire et lancer l'application
docker-compose up -d

# 3. Vérifier que tout fonctionne
docker-compose logs -f
```

✅ **L'application est prête !**  
Ouvrez votre navigateur : **http://localhost:5000**

### Arrêter l'application

```bash
docker-compose down
```

---

## Option 2 : Installation locale 💻

### Prérequis
- Python 3.11+
- pip

### Étapes

```bash
# 1. Se placer dans le dossier du projet
cd iris_project

# 2. Créer un environnement virtuel
python -m venv venv

# 3. Activer l'environnement
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Entraîner le modèle (si model.pkl n'existe pas)
python train.py

# 6. Lancer l'application
python app.py
```

✅ **L'application est prête !**  
Ouvrez votre navigateur : **http://localhost:5000**

---

## 🎯 Tester l'application

### Via l'interface web
1. Ouvrez http://localhost:5000
2. Entrez une valeur (ex: 3.5)
3. Cliquez sur "PRÉDIRE"

### Via l'API (curl)
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_width": 3.5}'
```

### Via Python
```python
import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={'sepal_width': 3.5}
)
print(response.json())
```

---

## ❓ Problèmes courants

### Le port 5000 est déjà utilisé

**Solution Docker :**
```bash
# Modifier docker-compose.yml pour utiliser un autre port
ports:
  - "8080:5000"
```

**Solution locale :**
```bash
# Définir une variable d'environnement
export PORT=8080  # Linux/Mac
$env:PORT=8080    # Windows PowerShell
python app.py
```

### Le modèle n'est pas trouvé

```bash
python train.py
```

### Erreur de dépendances

```bash
pip install --upgrade -r requirements.txt
```

---

## 📚 Aller plus loin

- Consulter le [README complet](README.md)
- Explorer [MLflow UI](http://localhost:5000) après avoir lancé `mlflow ui`
- Modifier le modèle dans `train.py`
- Personnaliser le frontend dans `website/src/`

---

**Besoin d'aide ?** Consultez la section [Dépannage](README.md#-dépannage) du README principal.
