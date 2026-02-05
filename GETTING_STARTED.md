# 🚀 Guide de démarrage - Pour les nouveaux contributeurs

Ce guide vous permet de lancer le projet Iris ML en quelques minutes sur votre ordinateur.

## 📋 Prérequis

### Option Docker (Recommandée - La plus simple)
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Option Locale (Alternative)
- [Git](https://git-scm.com/downloads)
- [Python 3.11+](https://www.python.org/downloads/)

---

## 🐳 OPTION 1 : Avec Docker (Recommandé)

### ⚡ En 3 étapes - Prêt en 5 minutes !

#### 1️⃣ Cloner le projet
```bash
git clone https://github.com/Kwegit/datapipeline.git
cd datapipeline/iris_project
```

#### 2️⃣ Lancer Docker Desktop
- Ouvrir **Docker Desktop**
- Attendre que l'icône devienne verte (Docker est prêt)

#### 3️⃣ Démarrer l'application
```bash
docker-compose up -d
```

#### 🎉 C'est prêt !
Ouvrez votre navigateur : **http://localhost:5000**

### Commandes utiles

```bash
# Voir les logs
docker-compose logs -f

# Arrêter l'application
docker-compose down

# Redémarrer
docker-compose restart

# Reconstruire après des modifications
docker-compose up -d --build
```

---

## 💻 OPTION 2 : Installation Locale

### Si vous préférez ne pas utiliser Docker

#### 1️⃣ Cloner le projet
```bash
git clone https://github.com/Kwegit/datapipeline.git
cd datapipeline/iris_project
```

#### 2️⃣ Créer un environnement virtuel

**Windows (PowerShell)** :
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac** :
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

#### 4️⃣ Entraîner le modèle
```bash
python train.py
```
*Note : Cette étape prend environ 1 minute et génère le fichier `model.pkl`*

#### 5️⃣ Lancer l'application
```bash
python app.py
```

#### 🎉 C'est prêt !
Ouvrez votre navigateur : **http://localhost:5000**

---

## 🧪 Tester l'application

### Via l'interface web
1. Ouvrir http://localhost:5000
2. Entrer une valeur de largeur de sépale (ex: **3.5**)
3. Cliquer sur **"PRÉDIRE"**
4. Voir les prédictions pour les 3 espèces d'iris

### Via l'API (curl)

**Windows (PowerShell)** :
```powershell
Invoke-RestMethod -Uri "http://localhost:5000/predict" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"sepal_width": 3.5}'
```

**Linux/Mac** :
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_width": 3.5}'
```

**Réponse attendue** :
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

---

## 🔄 Mettre à jour le projet

Quand de nouvelles modifications sont poussées :

```bash
# Récupérer les dernières modifications
git pull origin main

# Avec Docker : Reconstruire
docker-compose down
docker-compose up -d --build

# Sans Docker : Réinstaller les dépendances si nécessaire
pip install -r requirements.txt
python train.py
python app.py
```

---

## ❓ Problèmes courants

### Le port 5000 est déjà utilisé

**Solution Docker** :
```bash
docker-compose down
docker-compose up -d
```

**Solution Locale** :
```bash
# Trouver et tuer le processus utilisant le port 5000
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Docker : "unable to connect to daemon"

**Solution** :
1. Lancer Docker Desktop
2. Attendre que l'icône soit verte
3. Réessayer `docker-compose up -d`

### "Module not found" (Installation locale)

**Solution** :
```bash
# Vérifier que l'environnement virtuel est activé
# Réinstaller les dépendances
pip install --upgrade -r requirements.txt
```

### Le modèle n'est pas trouvé

**Solution** :
```bash
python train.py
```

---

## 📚 Documentation complète

Pour plus de détails, consultez :

- **[README.md](../README.md)** - Vue d'ensemble du projet
- **[QUICKSTART.md](QUICKSTART.md)** - Guide de démarrage détaillé
- **[DOCKER.md](DOCKER.md)** - Guide Docker complet
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Guide de contribution
- **[DOCUMENTATION.md](../DOCUMENTATION.md)** - Index de la documentation

---

## 🆘 Besoin d'aide ?

- 🐛 [Signaler un problème](https://github.com/Kwegit/datapipeline/issues/new)
- 💬 [Discussions](https://github.com/Kwegit/datapipeline/discussions)
- 📧 Contacter [@Kwegit](https://github.com/Kwegit)

---

## ✅ Checklist de démarrage

- [ ] Git installé
- [ ] Docker Desktop installé ET lancé (option Docker)
- [ ] OU Python 3.11+ installé (option locale)
- [ ] Repository cloné
- [ ] Application lancée (`docker-compose up -d` ou `python app.py`)
- [ ] Page accessible sur http://localhost:5000
- [ ] Test de prédiction effectué avec succès

---

**Bon développement ! 🎉**

Si vous rencontrez des problèmes, n'hésitez pas à ouvrir une issue ou consulter la documentation complète.
