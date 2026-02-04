# 🐳 Guide Docker

Ce guide explique comment utiliser Docker pour déployer l'application Iris Predictor.

## Prérequis

- Docker Desktop installé et en cours d'exécution
- Docker Compose installé (inclus avec Docker Desktop)

## Structure des fichiers Docker

```
iris_project/
├── Dockerfile              # Configuration de l'image Docker
├── docker-compose.yml      # Orchestration des services
├── .dockerignore          # Fichiers exclus de l'image
└── requirements.txt       # Dépendances Python
```

## 🚀 Démarrage rapide

### 1. Construction de l'image

```bash
cd iris_project
docker build -t iris-predictor .
```

### 2. Lancement avec Docker Compose (Recommandé)

```bash
docker-compose up -d
```

Cette commande va :
- Construire l'image si nécessaire
- Créer et démarrer le conteneur
- Monter les volumes pour la persistance
- Exposer le port 5000

### 3. Vérifier l'état

```bash
docker-compose ps
```

### 4. Voir les logs

```bash
docker-compose logs -f
```

### 5. Tester l'application

Ouvrez votre navigateur : **http://localhost:5000**

Ou testez l'API :
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_width": 3.5}'
```

## 🛑 Arrêt et nettoyage

### Arrêter les conteneurs

```bash
docker-compose down
```

### Arrêter et supprimer les volumes

```bash
docker-compose down -v
```

### Supprimer l'image

```bash
docker rmi iris-predictor
```

## 📋 Commandes utiles

### Logs en temps réel

```bash
docker-compose logs -f iris-predictor
```

### Redémarrer le service

```bash
docker-compose restart
```

### Accéder au shell du conteneur

```bash
docker-compose exec iris-predictor /bin/bash
```

### Reconstruire après modification

```bash
docker-compose up -d --build
```

### Voir les statistiques d'utilisation

```bash
docker stats iris-ml-app
```

## 🔧 Configuration

### Variables d'environnement

Vous pouvez configurer l'application via docker-compose.yml :

```yaml
environment:
  - FLASK_ENV=production
  - PORT=5000
  - PYTHONUNBUFFERED=1
```

### Changer le port

Modifier dans `docker-compose.yml` :

```yaml
ports:
  - "8080:5000"  # Port_hôte:Port_conteneur
```

### Volumes persistants

Les volumes suivants sont montés :
- `./model.pkl:/app/model.pkl` - Modèle ML
- `./mlruns:/app/mlruns` - Expériences MLflow

## 🐛 Dépannage

### Le conteneur ne démarre pas

```bash
# Voir les logs d'erreur
docker-compose logs

# Vérifier la configuration
docker-compose config
```

### Port déjà utilisé

```bash
# Windows PowerShell
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Modifier puis reconstruire

```bash
# Arrêter
docker-compose down

# Reconstruire et relancer
docker-compose up -d --build
```

### Le modèle n'est pas trouvé

Assurez-vous que `model.pkl` existe avant de lancer :

```bash
# Entraîner le modèle localement
python train.py

# Puis lancer Docker
docker-compose up -d
```

### Problèmes de permissions (Linux/Mac)

```bash
# Donner les bonnes permissions
chmod -R 755 iris_project/
```

## 📦 Dockerfile expliqué

```dockerfile
FROM python:3.11-slim          # Image de base légère
WORKDIR /app                    # Répertoire de travail
COPY requirements.txt .         # Copier les dépendances
RUN pip install --no-cache-dir -r requirements.txt  # Installer
COPY . .                        # Copier le code
EXPOSE 5000                     # Port exposé
CMD ["python", "app.py"]       # Commande de démarrage
```

## 🔄 Workflow de développement

### 1. Développement local

```bash
# Modifier le code
vim app.py

# Tester localement
python app.py
```

### 2. Test avec Docker

```bash
# Reconstruire l'image
docker-compose up -d --build

# Vérifier
docker-compose logs -f
```

### 3. Déploiement

```bash
# Production ready
docker-compose -f docker-compose.prod.yml up -d
```

## 🚀 Déploiement en production

### Utiliser Gunicorn

Modifier le `Dockerfile` :

```dockerfile
# Installer Gunicorn
RUN pip install gunicorn

# Commande de production
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

### Variables d'environnement de production

```yaml
environment:
  - FLASK_ENV=production
  - WORKERS=4
  - TIMEOUT=120
```

### Healthcheck

Le fichier `docker-compose.yml` inclut déjà un healthcheck :

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:5000/"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

## 📊 Monitoring

### Logs

```bash
# Tous les logs
docker-compose logs

# Seulement les 100 dernières lignes
docker-compose logs --tail=100

# Suivre en temps réel
docker-compose logs -f
```

### Métriques

```bash
# CPU, mémoire, réseau
docker stats iris-ml-app
```

## 🔐 Sécurité

### Best practices

1. ✅ Utiliser des images officielles
2. ✅ Minimiser les couches Docker
3. ✅ Ne pas exécuter en tant que root
4. ✅ Scanner les vulnérabilités
5. ✅ Utiliser des secrets pour les credentials

### Scanner l'image

```bash
docker scan iris-predictor
```

## 📚 Ressources

- [Documentation Docker](https://docs.docker.com/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

**Note** : Pour une utilisation en production, considérez l'utilisation de Kubernetes ou Docker Swarm pour l'orchestration à grande échelle.
