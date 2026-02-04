# 📚 Documentation - Index

Bienvenue dans la documentation complète du projet Iris ML ! Voici un guide pour naviguer dans tous les documents disponibles.

## 🗂️ Documents disponibles

### 1. README.md (Principal)
**Fichier** : [README.md](README.md)

**Contenu** :
- Vue d'ensemble du projet complet
- Architecture globale
- Technologies utilisées
- Guide d'installation
- Utilisation de l'API
- Performances du modèle
- Contribution et licence

**👉 À lire en premier** pour comprendre le projet dans son ensemble.

---

### 2. iris_project/README.md (Application)
**Fichier** : [iris_project/README.md](iris_project/README.md)

**Contenu** :
- Documentation détaillée de l'application Flask
- API REST complète
- Structure du modèle ML
- MLflow tracking
- Guide de développement
- Dépannage détaillé

**👉 À consulter** pour développer ou modifier l'application.

---

### 3. QUICKSTART.md (Démarrage rapide)
**Fichier** : [iris_project/QUICKSTART.md](iris_project/QUICKSTART.md)

**Contenu** :
- Guide de démarrage en 5 minutes
- Options Docker et locale
- Tests rapides
- Résolution des problèmes courants

**👉 À utiliser** pour démarrer rapidement sans lire toute la doc.

---

### 4. DOCKER.md (Guide Docker)
**Fichier** : [iris_project/DOCKER.md](iris_project/DOCKER.md)

**Contenu** :
- Configuration Docker complète
- Docker Compose
- Commandes utiles
- Dépannage Docker
- Best practices
- Déploiement en production

**👉 À consulter** pour tout ce qui concerne Docker et le déploiement.

---

### 5. CONTRIBUTING.md (Guide de contribution)
**Fichier** : [CONTRIBUTING.md](CONTRIBUTING.md)

**Contenu** :
- Comment contribuer au projet
- Standards de code
- Process de Pull Request
- Guide de tests
- Reconnaissance des contributeurs

**👉 À lire** avant de contribuer au projet.

---

## 🎯 Par cas d'usage

### Je veux juste utiliser l'application

1. [QUICKSTART.md](iris_project/QUICKSTART.md) - Démarrage rapide
2. [README.md](README.md) - Vue d'ensemble

### Je veux développer / modifier l'application

1. [iris_project/README.md](iris_project/README.md) - Documentation technique
2. [CONTRIBUTING.md](CONTRIBUTING.md) - Standards de développement
3. [README.md](README.md) - Architecture globale

### Je veux déployer en production

1. [DOCKER.md](iris_project/DOCKER.md) - Guide Docker complet
2. [iris_project/README.md](iris_project/README.md) - Configuration de l'application
3. [QUICKSTART.md](iris_project/QUICKSTART.md) - Tests rapides

### Je veux contribuer au projet

1. [CONTRIBUTING.md](CONTRIBUTING.md) - Guide de contribution
2. [iris_project/README.md](iris_project/README.md) - Structure du code
3. [README.md](README.md) - Vision du projet

## 📖 Scripts et outils

### Scripts de déploiement

| Script | Plateforme | Description |
|--------|-----------|-------------|
| `deploy.sh` | Linux/Mac | Script Bash de déploiement automatique |
| `deploy.ps1` | Windows | Script PowerShell de déploiement |

**Utilisation** :
```bash
# Linux/Mac
./deploy.sh [local|docker|train|test|clean]

# Windows
.\deploy.ps1 [local|docker|train|test|clean]
```

### Fichiers de configuration

| Fichier | Description |
|---------|-------------|
| `requirements.txt` | Dépendances Python de l'application |
| `Dockerfile` | Configuration de l'image Docker |
| `docker-compose.yml` | Orchestration Docker Compose |
| `.dockerignore` | Fichiers exclus de l'image Docker |
| `.gitignore` | Fichiers exclus de Git |

## 🗺️ Plan du site de documentation

```
Documentation/
│
├── README.md                    # Vue d'ensemble du projet
│   ├── Installation
│   ├── Architecture
│   └── Utilisation générale
│
├── iris_project/
│   ├── README.md               # Documentation technique détaillée
│   │   ├── API Documentation
│   │   ├── Structure du code
│   │   ├── MLflow
│   │   └── Développement
│   │
│   ├── QUICKSTART.md          # Guide de démarrage rapide
│   │   ├── Docker
│   │   └── Local
│   │
│   └── DOCKER.md              # Guide Docker complet
│       ├── Configuration
│       ├── Déploiement
│       └── Production
│
└── CONTRIBUTING.md            # Guide de contribution
    ├── Standards de code
    ├── Process de PR
    └── Tests

Scripts/
├── deploy.sh                  # Déploiement Linux/Mac
└── deploy.ps1                 # Déploiement Windows
```

## 🔍 Index par sujet

### Installation et configuration

- [Installation locale](README.md#-installation) - README principal
- [Installation Docker](iris_project/DOCKER.md#-démarrage-rapide) - Guide Docker
- [Quick Start](iris_project/QUICKSTART.md) - Démarrage rapide
- [Configuration Python](iris_project/README.md#installation) - Application README

### Utilisation

- [Interface Web](iris_project/README.md#utilisation) - Guide d'utilisation
- [API REST](iris_project/README.md#api-documentation) - Documentation API
- [Exemples d'utilisation](iris_project/README.md#🎯-utilisation) - Exemples pratiques
- [Tests de l'API](iris_project/QUICKSTART.md#-tester-lapplication) - Tests rapides

### Machine Learning

- [Entraînement du modèle](README.md#-composants-du-projet) - Vue d'ensemble
- [Structure du pipeline](iris_project/README.md#structure-du-modèle) - Détails techniques
- [MLflow Tracking](iris_project/README.md#-mlflow-tracking) - Tracking des expériences
- [Performances](README.md#-performances) - Métriques du modèle

### Docker et déploiement

- [Guide Docker complet](iris_project/DOCKER.md) - Tout sur Docker
- [Docker Compose](iris_project/DOCKER.md#-démarrage-rapide) - Orchestration
- [Production](iris_project/DOCKER.md#-déploiement-en-production) - Déploiement prod
- [Dépannage Docker](iris_project/DOCKER.md#-dépannage) - Résolution de problèmes

### Développement

- [Guide de contribution](CONTRIBUTING.md) - Comment contribuer
- [Standards de code](CONTRIBUTING.md#-standards-de-code) - Conventions
- [Structure du projet](CONTRIBUTING.md#-structure-du-projet) - Architecture
- [Tests](CONTRIBUTING.md#-tests) - Guide de test

### Dépannage

- [Problèmes courants](iris_project/README.md#-dépannage) - Solutions
- [Dépannage Docker](iris_project/DOCKER.md#-dépannage) - Problèmes Docker
- [Quick fixes](iris_project/QUICKSTART.md#-problèmes-courants) - Solutions rapides

## 🆘 Besoin d'aide ?

### Par niveau de connaissance

**Débutant** :
1. [QUICKSTART.md](iris_project/QUICKSTART.md) - Commencer simplement
2. [README.md](README.md) - Comprendre le projet
3. [Dépannage](iris_project/README.md#-dépannage) - Résoudre les problèmes

**Intermédiaire** :
1. [iris_project/README.md](iris_project/README.md) - Documentation technique
2. [DOCKER.md](iris_project/DOCKER.md) - Maîtriser Docker
3. [API Documentation](iris_project/README.md#api-documentation) - Utiliser l'API

**Avancé** :
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Contribuer au projet
2. [Structure du code](CONTRIBUTING.md#-structure-du-projet) - Architecture
3. [Standards](CONTRIBUTING.md#-standards-de-code) - Conventions avancées

## 📞 Support

- 🐛 [Signaler un bug](https://github.com/Kwegit/datapipeline/issues/new?template=bug_report.md)
- 💡 [Proposer une fonctionnalité](https://github.com/Kwegit/datapipeline/issues/new?template=feature_request.md)
- 💬 [Discussion](https://github.com/Kwegit/datapipeline/discussions)
- 📧 Contact : [GitHub Profile](https://github.com/Kwegit)

## 🔗 Liens rapides

| Action | Lien |
|--------|------|
| 🏠 Accueil | [README.md](README.md) |
| 🚀 Démarrer | [QUICKSTART.md](iris_project/QUICKSTART.md) |
| 📖 Documentation complète | [iris_project/README.md](iris_project/README.md) |
| 🐳 Docker | [DOCKER.md](iris_project/DOCKER.md) |
| 🤝 Contribuer | [CONTRIBUTING.md](CONTRIBUTING.md) |
| 🐛 Issues | [GitHub Issues](https://github.com/Kwegit/datapipeline/issues) |

---

**Bon développement ! 🎉**
