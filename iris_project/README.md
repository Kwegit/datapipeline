# 🌸 Iris Sepal Length Predictor

Application de Machine Learning pour prédire la longueur des sépales d'iris en fonction de leur largeur et de leur espèce.

## 📋 Table des matières

- [Aperçu](#aperçu)
- [Architecture](#architecture)
- [Technologies utilisées](#technologies-utilisées)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Docker](#docker)
- [Structure du projet](#structure-du-projet)
- [API Documentation](#api-documentation)
- [MLflow Tracking](#mlflow-tracking)
- [Développement](#développement)

## 🎯 Aperçu

Ce projet est une application complète de Machine Learning qui :
- Entraîne un modèle de régression linéaire sur le dataset Iris
- Fournit une API REST Flask pour faire des prédictions
- Offre une interface web moderne pour interagir avec le modèle
- Utilise MLflow pour le tracking des expériences
- Est entièrement containerisé avec Docker

### Fonctionnalités

✨ **Prédiction multi-espèces** : Prédit la longueur des sépales pour les 3 espèces d'iris  
📊 **Visualisation** : Génère des graphiques de performance avec R² score  
🔄 **API RESTful** : Interface HTTP simple et documentée  
🎨 **Interface web** : Frontend moderne et responsive  
📦 **Containerisé** : Déploiement facile avec Docker  
📈 **MLflow** : Tracking complet des expériences et métriques  

## 🏗️ Architecture

```
┌─────────────────┐      HTTP      ┌─────────────────┐
│   Frontend      │ ────────────► │   Flask API     │
│  (HTML/CSS/JS)  │                │   (Port 5000)   │
└─────────────────┘                └────────┬────────┘
                                            │
                                   ┌────────▼────────┐
                                   │  ML Pipeline    │
                                   │ (Scikit-Learn)  │
                                   └────────┬────────┘
                                            │
                                   ┌────────▼────────┐
                                   │  Model (PKL)    │
                                   │  + MLflow       │
                                   └─────────────────┘
```

## 🛠️ Technologies utilisées

### Backend
- **Python 3.11** - Langage de programmation
- **Flask 3.1.2** - Framework web
- **Flask-CORS 6.0.2** - Gestion des requêtes cross-origin
- **Scikit-Learn 1.8.0** - Machine Learning
- **Pandas 2.3.3** - Manipulation de données
- **MLflow 3.9.0** - Tracking des expériences ML

### Frontend
- **HTML5/CSS3** - Structure et style
- **JavaScript (Vanilla)** - Logique côté client
- **Fetch API** - Communication avec l'API

### DevOps
- **Docker** - Containerisation
- **Docker Compose** - Orchestration

## 📦 Installation

### Prérequis

- Python 3.11 ou supérieur
- pip (gestionnaire de paquets Python)
- Git

### Installation locale

1. **Cloner le repository**
```bash
git clone <votre-repo-url>
cd datapipeline/iris_project
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Entraîner le modèle**
```bash
python train.py
```

Cette commande va :
- Charger le dataset iris_cleaned2.csv
- Entraîner un modèle de régression linéaire
- Générer un graphique de performance (prediction_plot_linear.png)
- Sauvegarder le modèle (model.pkl)
- Logger les métriques dans MLflow

5. **Lancer l'application**
```bash
python app.py
```

L'application sera accessible sur : **http://localhost:5000**

## 🚀 Utilisation

### Interface Web

1. Ouvrez votre navigateur à l'adresse : `http://localhost:5000`
2. Entrez une valeur de largeur de sépale (ex: 3.5)
3. Cliquez sur "PRÉDIRE"
4. Les prédictions pour les 3 espèces s'affichent :
   - **Setosa** : Iris Setosa
   - **Versicolor** : Iris Versicolor
   - **Virginica** : Iris Virginica

### API REST

#### Endpoint de prédiction

**POST** `/predict`

**Request Body:**
```json
{
  "sepal_width": 3.5
}
```

**Response:**
```json
{
  "input_sepal_width": 3.5,
  "predictions_by_species": {
    "setosa": 5.12,
    "versicolor": 6.34,
    "virginica": 7.21
  },
  "unit": "cm",
  "status": "success"
}
```

**Exemple avec curl:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_width": 3.5}'
```

**Exemple avec Python:**
```python
import requests

response = requests.post(
    'http://localhost:5000/predict',
    json={'sepal_width': 3.5}
)
print(response.json())
```

## 🐳 Docker

### Construction de l'image

```bash
docker build -t iris-predictor .
```

### Lancement avec Docker

```bash
docker run -p 5000:5000 iris-predictor
```

### Utilisation de Docker Compose (recommandé)

```bash
# Lancer l'application
docker-compose up -d

# Voir les logs
docker-compose logs -f

# Arrêter l'application
docker-compose down
```

L'application sera accessible sur : **http://localhost:5000**

### Avantages de Docker

- ✅ **Portabilité** : Fonctionne partout de manière identique
- ✅ **Isolation** : Environnement isolé et reproductible
- ✅ **Simplicité** : Une seule commande pour démarrer
- ✅ **Persistance** : Les modèles et données sont préservés via volumes

## 📁 Structure du projet

```
iris_project/
├── app.py                          # Application Flask principale
├── train.py                        # Script d'entraînement du modèle
├── train_simple.py                 # Version simplifiée de l'entraînement
├── model.pkl                       # Modèle ML sauvegardé
├── iris_cleaned2.csv              # Dataset nettoyé
├── prediction_plot_linear.png     # Graphique de performance
├── requirements.txt               # Dépendances Python
├── Dockerfile                     # Configuration Docker
├── docker-compose.yml             # Orchestration Docker
├── .dockerignore                  # Fichiers exclus de Docker
├── README.md                      # Ce fichier
│
├── website/                       # Frontend
│   └── src/
│       ├── index.html            # Page principale
│       ├── css/
│       │   └── styles.css        # Styles CSS
│       ├── js/
│       │   └── main.js           # Logique JavaScript
│       └── assets/               # Images et polices
│
└── mlruns/                       # Données MLflow
    └── ...
```

## 📊 API Documentation

### Routes disponibles

| Route      | Méthode | Description                    |
|------------|---------|--------------------------------|
| `/`        | GET     | Page d'accueil (interface web) |
| `/predict` | POST    | Endpoint de prédiction         |

### Codes de statut HTTP

| Code | Description                              |
|------|------------------------------------------|
| 200  | Succès                                   |
| 400  | Erreur de validation des données         |
| 500  | Erreur serveur (modèle non disponible)   |

## 📈 MLflow Tracking

### Visualiser les expériences

```bash
mlflow ui
```

Puis ouvrez : **http://localhost:5000**

### Métriques trackées

- **MSE** (Mean Squared Error) : Erreur quadratique moyenne
- **R² Score** : Coefficient de détermination
- **Paramètres** : Type de modèle, hyperparamètres
- **Artifacts** : Graphiques, modèle sauvegardé

### Expériences disponibles

- `Iris_LinearRegression_Species` : Régression linéaire avec encodage des espèces

## 🔧 Développement

### Structure du modèle

Le pipeline ML comprend :

1. **Préprocessing** : OneHotEncoder pour la variable catégorielle 'species'
2. **Modèle** : LinearRegression de scikit-learn
3. **Features** : sepal_width (numérique) + species (catégorielle)
4. **Target** : sepal_length

### Entraîner un nouveau modèle

```bash
python train.py
```

Options de configuration dans `train.py` :
- `test_size` : Taille de l'ensemble de test (défaut: 0.2)
- `random_state` : Seed pour la reproductibilité (défaut: 42)

### Modifier l'API

Le fichier `app.py` contient la logique de l'API Flask. Points clés :

- **CORS activé** : Permet les requêtes depuis n'importe quelle origine
- **Gestion d'erreurs** : Try/catch avec messages explicites
- **Logging** : Affichage du statut du modèle au démarrage

### Personnaliser le frontend

Fichiers à modifier :
- `website/src/index.html` : Structure HTML
- `website/src/css/styles.css` : Styles visuels
- `website/src/js/main.js` : Logique d'interaction

## 🐛 Dépannage

### Le serveur ne démarre pas

**Problème** : `ModuleNotFoundError: No module named 'flask'`

**Solution** :
```bash
pip install -r requirements.txt
```

### Le modèle n'est pas trouvé

**Problème** : `Erreur : Impossible de charger model.pkl`

**Solution** :
```bash
python train.py  # Entraîner le modèle
```

### CORS bloque les requêtes

**Problème** : Erreur CORS dans la console du navigateur

**Solution** : Vérifiez que Flask-CORS est installé et que `CORS(app)` est présent dans `app.py`

### Port déjà utilisé

**Problème** : `Address already in use`

**Solution** :
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

## 📝 Dataset

Le dataset Iris contient :
- **150 observations** de fleurs d'iris
- **3 espèces** : Setosa, Versicolor, Virginica
- **4 features** : sepal_length, sepal_width, petal_length, petal_width

Dans ce projet, on prédit `sepal_length` à partir de `sepal_width` et `species`.

## 🎯 Performances du modèle

Après entraînement avec `train.py` :

- **MSE** : ~0.30 (varie selon le split)
- **R² Score** : ~0.85
- **Temps d'entraînement** : < 1 seconde
- **Temps de prédiction** : < 10ms

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout de fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👨‍💻 Auteur

**Votre Nom**
- GitHub: [@Kwegit](https://github.com/Kwegit)

## 🙏 Remerciements

- Dataset Iris de Fisher (1936)
- Scikit-Learn pour les outils ML
- Flask pour le framework web
- MLflow pour le tracking d'expériences

---

**Note** : Ce projet est à but éducatif et démontre les bonnes pratiques en Machine Learning, développement web et DevOps.
