#!/bin/bash

# Script de déploiement rapide pour Iris ML Project
# Usage: ./deploy.sh [option]

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "🌸 Iris ML Project - Deployment Script"
echo "======================================"

# Fonction pour afficher l'aide
show_help() {
    echo ""
    echo "Usage: ./deploy.sh [option]"
    echo ""
    echo "Options:"
    echo "  local       - Installation locale avec venv"
    echo "  docker      - Déploiement avec Docker Compose"
    echo "  train       - Entraîner le modèle"
    echo "  test        - Tester l'API"
    echo "  clean       - Nettoyer les fichiers temporaires"
    echo "  help        - Afficher cette aide"
    echo ""
}

# Fonction d'installation locale
install_local() {
    echo -e "${YELLOW}📦 Installation locale en cours...${NC}"
    
    cd iris_project
    
    if [ ! -d "venv" ]; then
        echo "Création de l'environnement virtuel..."
        python3 -m venv venv
    fi
    
    echo "Activation de l'environnement virtuel..."
    source venv/bin/activate
    
    echo "Installation des dépendances..."
    pip install --upgrade pip
    pip install -r requirements.txt
    
    echo -e "${GREEN}✅ Installation terminée !${NC}"
    echo ""
    echo "Pour activer l'environnement virtuel:"
    echo "  source iris_project/venv/bin/activate"
    echo ""
    echo "Pour entraîner le modèle:"
    echo "  python train.py"
    echo ""
    echo "Pour lancer l'application:"
    echo "  python app.py"
}

# Fonction de déploiement Docker
deploy_docker() {
    echo -e "${YELLOW}🐳 Déploiement Docker en cours...${NC}"
    
    cd iris_project
    
    if [ ! -f "model.pkl" ]; then
        echo -e "${YELLOW}⚠️  Modèle non trouvé. Entraînement nécessaire d'abord.${NC}"
        echo "Voulez-vous entraîner le modèle maintenant? (y/n)"
        read -r response
        if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
            train_model
        else
            echo -e "${RED}❌ Le modèle est nécessaire pour l'API${NC}"
            exit 1
        fi
    fi
    
    echo "Construction et lancement des conteneurs..."
    docker-compose up -d
    
    echo -e "${GREEN}✅ Déploiement terminé !${NC}"
    echo ""
    echo "Application accessible sur: http://localhost:5000"
    echo ""
    echo "Commandes utiles:"
    echo "  docker-compose logs -f    # Voir les logs"
    echo "  docker-compose down       # Arrêter les conteneurs"
    echo "  docker-compose restart    # Redémarrer"
}

# Fonction d'entraînement
train_model() {
    echo -e "${YELLOW}🎓 Entraînement du modèle...${NC}"
    
    cd iris_project
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    python train.py
    
    echo -e "${GREEN}✅ Modèle entraîné avec succès !${NC}"
    echo "Fichiers générés:"
    echo "  - model.pkl (modèle sauvegardé)"
    echo "  - prediction_plot_linear.png (graphique)"
    echo "  - mlruns/ (expériences MLflow)"
}

# Fonction de test
test_api() {
    echo -e "${YELLOW}🧪 Test de l'API...${NC}"
    
    echo "Tentative de connexion à http://localhost:5000..."
    
    response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000)
    
    if [ "$response" -eq 200 ]; then
        echo -e "${GREEN}✅ API accessible !${NC}"
        
        echo ""
        echo "Test de prédiction..."
        curl -X POST http://localhost:5000/predict \
            -H "Content-Type: application/json" \
            -d '{"sepal_width": 3.5}' \
            | python -m json.tool
        
        echo ""
        echo -e "${GREEN}✅ Test réussi !${NC}"
    else
        echo -e "${RED}❌ L'API n'est pas accessible (code: $response)${NC}"
        echo "Assurez-vous que l'application est lancée:"
        echo "  - Local: python app.py"
        echo "  - Docker: docker-compose up -d"
    fi
}

# Fonction de nettoyage
clean() {
    echo -e "${YELLOW}🧹 Nettoyage en cours...${NC}"
    
    cd iris_project
    
    echo "Suppression des fichiers temporaires..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.pyo" -delete 2>/dev/null || true
    find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
    
    echo -e "${GREEN}✅ Nettoyage terminé !${NC}"
}

# Main
case "${1:-help}" in
    local)
        install_local
        ;;
    docker)
        deploy_docker
        ;;
    train)
        train_model
        ;;
    test)
        test_api
        ;;
    clean)
        clean
        ;;
    help|*)
        show_help
        ;;
esac
