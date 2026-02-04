# DATA PIPELINE

- Projet Data Pipeline : entraînement d'un modèle Iris + interface web minimale pour prédictions.
- Dossiers principaux :
  - `iris_project/` : code d'entraînement, export du modèle et backend (ex. `train.py`, `app.py`, `requirements.txt`).
  - `website/src/` : site statique (HTML/CSS/JS).
  - `src/assets/` : images et ressources.


Installation locale (sans Docker)
1. Cloner
   ```bash
   git clone <repo-url>
   cd datapipeline
   ```
2. Créer et activer un venv
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Installer dépendances backend
   ```bash
   pip install -r iris_project/requirements.txt
   ```
4. Entraîner / tester
   ```bash
   python iris_project/train.py
   ```
5. Ouvrir l'interface
   - Ouvrir `website/src/index.html` dans un navigateur

Docker (reproductibilité)
- Exemple : conteneur backend (API) + conteneur pour site statique (nginx).

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
