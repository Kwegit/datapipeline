# 📊 Data Pipeline - Iris ML Project

Projet complet de Data Science et Machine Learning sur le dataset Iris, incluant le nettoyage de données, l'entraînement de modèles, et le déploiement d'une API web.

## 🎯 Vue d'ensemble

Ce repository contient un pipeline complet de Machine Learning :

1. **Nettoyage des données** (`clean_data.py`)
2. **Entraînement de modèles** (`iris_project/train.py`)
3. **API REST** (`iris_project/app.py`)
4. **Interface Web** (`iris_project/website/`)
5. **Tracking MLflow** (expériences et métriques)
6. **Déploiement Docker** (containerisation complète)

## 📁 Structure du projet

```
datapipeline/
│
├── clean_data.py              # Script de nettoyage des données
├── data/
│   └── iris.csv              # Dataset original
│
├── iris_cleaned.csv          # Dataset nettoyé (version 1)
├── iris_cleaned2.csv         # Dataset nettoyé (version 2)
│
├── iris_project/             # 🌟 APPLICATION PRINCIPALE
│   ├── app.py               # API Flask
│   ├── train.py             # Entraînement du modèle
│   ├── train_simple.py      # Version simplifiée
│   ├── model.pkl            # Modèle ML sauvegardé
│   ├── requirements.txt     # Dépendances Python
│   ├── Dockerfile           # Configuration Docker
│   ├── docker-compose.yml   # Orchestration
│   ├── README.md            # Documentation détaillée
│   ├── QUICKSTART.md        # Guide de démarrage rapide
│   │
│   ├── website/             # Frontend
│   │   └── src/
│   │       ├── index.html
│   │       ├── css/
│   │       ├── js/
│   │       └── assets/
│   │
│   └── mlruns/              # Données MLflow
│
├── mlruns/                   # Expériences MLflow (racine)
├── mlflow.db                 # Base de données MLflow
├── model.pkl                 # Modèle sauvegardé (racine)
├── prediction_plot_linear.png # Graphique de performance
│
└── requirements.txt          # Dépendances globales
```

## 🚀 Démarrage rapide

### Option 1 : Docker (Recommandé)

```bash
cd iris_project
docker-compose up -d
```

Ouvrez : **http://localhost:5000**

### Option 2 : Installation locale

```bash
cd iris_project
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python train.py
python app.py
```

📖 **Guide détaillé** : Consultez [iris_project/QUICKSTART.md](iris_project/QUICKSTART.md)

## 🔧 Composants du projet

### 1. Nettoyage des données

**Fichier** : `clean_data.py`

Prépare et nettoie le dataset Iris :
- Suppression des doublons
- Gestion des valeurs manquantes
- Normalisation des noms de colonnes
- Sauvegarde en CSV propre

```bash
python clean_data.py
```

### 2. Application ML (iris_project/)

**Application complète** avec :
- ✅ Entraînement de modèle (Régression Linéaire)
- ✅ API REST Flask
- ✅ Interface web moderne
- ✅ Tracking MLflow
- ✅ Containerisation Docker

**Documentation complète** : [iris_project/README.md](iris_project/README.md)

### 3. MLflow Tracking

Visualisation des expériences et métriques :

```bash
mlflow ui
```

Puis ouvrez : **http://localhost:5000**

## 🛠️ Technologies

### Data Science & ML
- **Python 3.11**
- **Pandas** - Manipulation de données
- **Scikit-Learn** - Machine Learning
- **MLflow** - Tracking d'expériences
- **Matplotlib** - Visualisation

### Web
- **Flask** - Backend API
- **HTML/CSS/JS** - Frontend
- **Flask-CORS** - CORS handling

### DevOps
- **Docker** - Containerisation
- **Docker Compose** - Orchestration

## 📊 Dataset Iris

Le célèbre dataset Iris contient :
- **150 observations** de fleurs d'iris
- **3 espèces** : Setosa, Versicolor, Virginica
- **4 features** :
  - Longueur du sépale (sepal_length)
  - Largeur du sépale (sepal_width)
  - Longueur du pétale (petal_length)
  - Largeur du pétale (petal_width)

**Notre modèle** prédit `sepal_length` à partir de `sepal_width` et `species`.

## 🎯 Utilisation

### 1. Nettoyer les données

```bash
python clean_data.py
```

### 2. Entraîner le modèle

```bash
cd iris_project
python train.py
```

Ceci va :
- Charger le dataset nettoyé
- Entraîner un modèle de régression linéaire
- Générer des visualisations
- Sauvegarder le modèle (model.pkl)
- Logger les métriques dans MLflow

### 3. Lancer l'API

```bash
python app.py
```

### 4. Tester l'API

**Via l'interface web** : http://localhost:5000

**Via curl** :
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_width": 3.5}'
```

**Réponse** :
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

## 🐳 Docker

### Lancer avec Docker Compose

```bash
cd iris_project
docker-compose up -d
```

### Construire l'image manuellement

```bash
cd iris_project
docker build -t iris-predictor .
docker run -p 5000:5000 iris-predictor
```

### Avantages

- ✅ Environnement isolé et reproductible
- ✅ Pas de conflits de dépendances
- ✅ Déploiement facile
- ✅ Fonctionne partout de manière identique

## 📈 Performances

Métriques du modèle (Régression Linéaire) :

| Métrique   | Valeur |
|------------|--------|
| MSE        | ~0.30  |
| R² Score   | ~0.85  |
| Entraînement | < 1s   |
| Prédiction | < 10ms |

## 🤝 Contribution

Les contributions sont bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commit les changements (`git commit -m 'Ajout de fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrir une Pull Request

## 📚 Documentation

- [README principal de l'application](iris_project/README.md) - Documentation complète
- [Guide de démarrage rapide](iris_project/QUICKSTART.md) - Démarrage en 5 minutes
- [API Documentation](iris_project/README.md#api-documentation) - Endpoints et exemples

## 📄 Licence

Ce projet est sous licence MIT.

## 👨‍💻 Auteur

- **GitHub** : [@Kwegit](https://github.com/Kwegit)
- **Repository** : [datapipeline](https://github.com/Kwegit/datapipeline)

## 🙏 Remerciements

- **Ronald Fisher** - Pour le dataset Iris (1936)
- **Scikit-Learn** - Framework ML
- **Flask** - Framework web
- **MLflow** - Tracking d'expériences
- **Docker** - Containerisation

---

**⭐ Si ce projet vous a aidé, n'oubliez pas de lui donner une étoile !**

---

**Note** : Ce projet est à but éducatif et démontre les bonnes pratiques en Data Science, Machine Learning, développement web et DevOps.

Backend — iris_project/Dockerfile (exemple)
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

Web — website/Dockerfile (exemple)
```dockerfile
FROM nginx:alpine
COPY src /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

docker-compose.yml (exemple minimal)
```yaml
version: "3.8"
services:
  backend:
    build:
      context: ./iris_project
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - MODEL_PATH=/app/model.joblib

  web:
    build:
      context: ./website
      dockerfile: Dockerfile
    ports:
      - "8080:80"
    depends_on:
      - backend
```

Commandes Docker utiles
- Construire : `docker-compose build`
- Lancer : `docker-compose up` (ou `-d` pour détaché)
- Arrêter : `docker-compose down`
- Logs : `docker-compose logs -f`

Variables d'environnement
- Documenter ici les variables attendues par le backend (PORT, MODEL_PATH, etc.) ou fournir un fichier `.env` référencé par docker‑compose.
