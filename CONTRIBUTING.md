# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer au projet Iris ML ! Ce guide vous explique comment participer efficacement.

## 📋 Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Structure du projet](#structure-du-projet)
- [Configuration de l'environnement](#configuration-de-lenvironnement)
- [Standards de code](#standards-de-code)
- [Tests](#tests)
- [Pull Requests](#pull-requests)

## 🤗 Code de conduite

### Nos engagements

- Respecter tous les contributeurs
- Accepter les critiques constructives
- Se concentrer sur ce qui est meilleur pour la communauté
- Faire preuve d'empathie envers les autres

## 🚀 Comment contribuer

### Signaler un bug

1. Vérifiez que le bug n'a pas déjà été signalé
2. Ouvrez une [Issue](https://github.com/Kwegit/datapipeline/issues/new)
3. Décrivez le bug clairement :
   - Description du problème
   - Étapes pour reproduire
   - Comportement attendu vs actuel
   - Environnement (OS, Python version, etc.)
   - Captures d'écran si pertinent

**Template d'issue pour bug** :
```markdown
**Description**
[Description claire du bug]

**Reproduction**
1. Aller à '...'
2. Cliquer sur '...'
3. Voir l'erreur

**Comportement attendu**
[Ce qui devrait se passer]

**Captures d'écran**
[Si applicable]

**Environnement**
- OS: [e.g. Windows 10, Ubuntu 20.04]
- Python: [e.g. 3.11.5]
- Version du projet: [e.g. commit hash]
```

### Proposer une fonctionnalité

1. Ouvrez une Issue avec le label "enhancement"
2. Expliquez :
   - Le problème que cela résout
   - La solution proposée
   - Les alternatives considérées
   - Impact sur le code existant

### Améliorer la documentation

- Corriger des fautes de frappe
- Clarifier des instructions confuses
- Ajouter des exemples
- Traduire en d'autres langues

## 📁 Structure du projet

```
iris_project/
├── app.py              # API Flask - point d'entrée principal
├── train.py            # Script d'entraînement du modèle
├── train_simple.py     # Version simplifiée de l'entraînement
├── requirements.txt    # Dépendances Python
├── Dockerfile          # Configuration Docker
├── docker-compose.yml  # Orchestration Docker
│
├── website/           # Frontend
│   └── src/
│       ├── index.html # Page principale
│       ├── css/       # Styles
│       ├── js/        # JavaScript
│       └── assets/    # Images, polices
│
├── mlruns/           # Expériences MLflow (ignoré par git)
└── model.pkl         # Modèle sauvegardé (peut être versionné)
```

## ⚙️ Configuration de l'environnement

### 1. Fork et clone

```bash
# Fork via GitHub UI, puis :
git clone https://github.com/VOTRE_USERNAME/datapipeline.git
cd datapipeline
```

### 2. Créer une branche

```bash
git checkout -b feature/ma-nouvelle-fonctionnalite
```

### 3. Environnement virtuel

```bash
cd iris_project
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt

# Dépendances de développement (si disponibles)
pip install -r requirements-dev.txt
```

### 5. Configurer Git

```bash
git config user.name "Votre Nom"
git config user.email "votre@email.com"
```

## 📝 Standards de code

### Python (PEP 8)

- Indentation : 4 espaces
- Longueur de ligne : max 100 caractères
- Noms de variables : `snake_case`
- Noms de classes : `PascalCase`
- Constantes : `UPPER_CASE`

**Exemple** :
```python
# Bon ✅
def predict_sepal_length(sepal_width, species):
    """Prédit la longueur du sépale."""
    input_df = pd.DataFrame([{
        'sepal_width': sepal_width,
        'species': species
    }])
    return model.predict(input_df)

# Mauvais ❌
def PredictSepalLength(SepalWidth, Species):
    InputDF = pd.DataFrame([{'sepal_width':SepalWidth,'species':Species}])
    return model.predict(InputDF)
```

### JavaScript

- Indentation : 2 espaces
- Utiliser `const` et `let`, pas `var`
- Noms de variables : `camelCase`
- Fonctions fléchées quand possible

**Exemple** :
```javascript
// Bon ✅
const predictSepalLength = async (sepalWidth) => {
  const response = await fetch(API_URL, {
    method: 'POST',
    body: JSON.stringify({ sepal_width: sepalWidth })
  });
  return response.json();
};

// Mauvais ❌
var predict_sepal_length = function(sepal_width) {
  var response = fetch(API_URL, {
    method: 'POST',
    body: JSON.stringify({sepal_width:sepal_width})
  });
  return response.json();
}
```

### Documentation

- Ajouter des docstrings à toutes les fonctions
- Commenter le code complexe
- Mettre à jour le README si nécessaire

**Exemple de docstring** :
```python
def predict(sepal_width: float, species: str) -> float:
    """
    Prédit la longueur du sépale en fonction de sa largeur et de l'espèce.
    
    Args:
        sepal_width (float): Largeur du sépale en cm
        species (str): Espèce d'iris ('setosa', 'versicolor', 'virginica')
    
    Returns:
        float: Longueur prédite du sépale en cm
    
    Raises:
        ValueError: Si l'espèce n'est pas reconnue
        
    Example:
        >>> predict(3.5, 'setosa')
        5.12
    """
    # Implementation...
```

## 🧪 Tests

### Lancer les tests

```bash
# Tests unitaires
pytest tests/

# Avec couverture
pytest --cov=. tests/

# Tests spécifiques
pytest tests/test_app.py
```

### Écrire des tests

Créer un fichier dans `tests/` :

```python
# tests/test_predictions.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    """Test de l'endpoint de prédiction."""
    response = client.post('/predict', 
        json={'sepal_width': 3.5})
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'predictions_by_species' in data
    assert 'setosa' in data['predictions_by_species']

def test_predict_invalid_input(client):
    """Test avec entrée invalide."""
    response = client.post('/predict', 
        json={'sepal_width': 'invalid'})
    
    assert response.status_code == 400
```

## 📤 Pull Requests

### Avant de soumettre

- [ ] Le code suit les standards définis
- [ ] Les tests passent
- [ ] La documentation est à jour
- [ ] Les commits sont clairs et atomiques
- [ ] Pas de fichiers inutiles (cache, logs, etc.)

### Message de commit

Format :
```
<type>(<scope>): <sujet>

<corps>

<footer>
```

**Types** :
- `feat` : Nouvelle fonctionnalité
- `fix` : Correction de bug
- `docs` : Documentation
- `style` : Formatage, lint
- `refactor` : Refactoring de code
- `test` : Ajout de tests
- `chore` : Tâches de maintenance

**Exemples** :
```bash
feat(api): ajouter endpoint de batch prediction

Permet de faire des prédictions sur plusieurs entrées simultanément.
Améliore les performances de 50% pour les lots de 100+ entrées.

Closes #42

---

fix(model): corriger gestion des valeurs nulles

Les valeurs NULL dans sepal_width causaient un crash.
Ajout de validation et message d'erreur explicite.

Fixes #38
```

### Créer une PR

1. **Pousser votre branche**
```bash
git push origin feature/ma-nouvelle-fonctionnalite
```

2. **Ouvrir une PR sur GitHub**
   - Titre clair et descriptif
   - Description détaillée
   - Lier les issues concernées
   - Ajouter des captures d'écran si pertinent

3. **Template de PR** :
```markdown
## Description
[Description de la fonctionnalité ou du fix]

## Type de changement
- [ ] Bug fix
- [ ] Nouvelle fonctionnalité
- [ ] Breaking change
- [ ] Documentation

## Checklist
- [ ] Le code suit les standards du projet
- [ ] Tests ajoutés/mis à jour
- [ ] Documentation mise à jour
- [ ] Pas de warnings
- [ ] Tests passent localement

## Screenshots (si applicable)
[Captures d'écran]

## Issues liées
Closes #[numéro]
```

### Processus de review

1. Un mainteneur review votre PR
2. Des modifications peuvent être demandées
3. Faire les modifications et pousser
4. Une fois approuvée, la PR sera mergée

## 🎯 Domaines de contribution

### Backend (Python/Flask)

- Nouveaux endpoints API
- Amélioration des performances
- Gestion d'erreurs
- Validation des données
- Nouveaux algorithmes ML

### Frontend (HTML/CSS/JS)

- Amélioration de l'UI/UX
- Nouvelles fonctionnalités visuelles
- Responsive design
- Accessibilité
- Animations

### Machine Learning

- Nouveaux modèles (Random Forest, XGBoost, etc.)
- Feature engineering
- Optimisation des hyperparamètres
- Validation croisée
- Métriques supplémentaires

### DevOps

- Configuration Docker
- CI/CD pipelines
- Scripts de déploiement
- Monitoring et logs
- Tests automatisés

### Documentation

- Tutorials
- Exemples d'utilisation
- FAQ
- Traductions
- Diagrammes

## 🏆 Reconnaissance

Les contributeurs seront ajoutés au README :

```markdown
## 👥 Contributeurs

- [@username](https://github.com/username) - Description de la contribution
```

## 📞 Questions ?

- Ouvrir une [Issue](https://github.com/Kwegit/datapipeline/issues)
- Discussion sur [GitHub Discussions](https://github.com/Kwegit/datapipeline/discussions)

---

**Merci pour votre contribution ! 🎉**
