# Script de déploiement rapide pour Iris ML Project (Windows)
# Usage: .\deploy.ps1 [option]

param(
    [Parameter(Position=0)]
    [ValidateSet('local', 'docker', 'train', 'test', 'clean', 'help')]
    [string]$Action = 'help'
)

Write-Host "🌸 Iris ML Project - Deployment Script" -ForegroundColor Cyan
Write-Host "======================================" -ForegroundColor Cyan
Write-Host ""

function Show-Help {
    Write-Host "Usage: .\deploy.ps1 [option]" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  local       - Installation locale avec venv"
    Write-Host "  docker      - Déploiement avec Docker Compose"
    Write-Host "  train       - Entraîner le modèle"
    Write-Host "  test        - Tester l'API"
    Write-Host "  clean       - Nettoyer les fichiers temporaires"
    Write-Host "  help        - Afficher cette aide"
    Write-Host ""
}

function Install-Local {
    Write-Host "📦 Installation locale en cours..." -ForegroundColor Yellow
    
    Set-Location iris_project
    
    if (-not (Test-Path "venv")) {
        Write-Host "Création de l'environnement virtuel..."
        python -m venv venv
    }
    
    Write-Host "Activation de l'environnement virtuel..."
    .\venv\Scripts\Activate.ps1
    
    Write-Host "Installation des dépendances..."
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    
    Write-Host "✅ Installation terminée !" -ForegroundColor Green
    Write-Host ""
    Write-Host "Pour activer l'environnement virtuel:"
    Write-Host "  cd iris_project"
    Write-Host "  .\venv\Scripts\Activate.ps1"
    Write-Host ""
    Write-Host "Pour entraîner le modèle:"
    Write-Host "  python train.py"
    Write-Host ""
    Write-Host "Pour lancer l'application:"
    Write-Host "  python app.py"
    
    Set-Location ..
}

function Deploy-Docker {
    Write-Host "🐳 Déploiement Docker en cours..." -ForegroundColor Yellow
    
    Set-Location iris_project
    
    if (-not (Test-Path "model.pkl")) {
        Write-Host "⚠️  Modèle non trouvé. Entraînement nécessaire d'abord." -ForegroundColor Yellow
        $response = Read-Host "Voulez-vous entraîner le modèle maintenant? (y/n)"
        if ($response -eq 'y' -or $response -eq 'Y') {
            Train-Model
        } else {
            Write-Host "❌ Le modèle est nécessaire pour l'API" -ForegroundColor Red
            Set-Location ..
            exit 1
        }
    }
    
    Write-Host "Construction et lancement des conteneurs..."
    docker-compose up -d
    
    Write-Host "✅ Déploiement terminé !" -ForegroundColor Green
    Write-Host ""
    Write-Host "Application accessible sur: http://localhost:5000"
    Write-Host ""
    Write-Host "Commandes utiles:"
    Write-Host "  docker-compose logs -f    # Voir les logs"
    Write-Host "  docker-compose down       # Arrêter les conteneurs"
    Write-Host "  docker-compose restart    # Redémarrer"
    
    Set-Location ..
}

function Train-Model {
    Write-Host "🎓 Entraînement du modèle..." -ForegroundColor Yellow
    
    Set-Location iris_project
    
    if (Test-Path "venv\Scripts\Activate.ps1") {
        .\venv\Scripts\Activate.ps1
    }
    
    python train.py
    
    Write-Host "✅ Modèle entraîné avec succès !" -ForegroundColor Green
    Write-Host "Fichiers générés:"
    Write-Host "  - model.pkl (modèle sauvegardé)"
    Write-Host "  - prediction_plot_linear.png (graphique)"
    Write-Host "  - mlruns/ (expériences MLflow)"
    
    Set-Location ..
}

function Test-API {
    Write-Host "🧪 Test de l'API..." -ForegroundColor Yellow
    
    Write-Host "Tentative de connexion à http://localhost:5000..."
    
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5000" -UseBasicParsing -ErrorAction Stop
        Write-Host "✅ API accessible !" -ForegroundColor Green
        
        Write-Host ""
        Write-Host "Test de prédiction..."
        
        $body = @{
            sepal_width = 3.5
        } | ConvertTo-Json
        
        $result = Invoke-RestMethod -Uri "http://localhost:5000/predict" `
            -Method Post `
            -ContentType "application/json" `
            -Body $body
        
        $result | ConvertTo-Json -Depth 10
        
        Write-Host ""
        Write-Host "✅ Test réussi !" -ForegroundColor Green
    }
    catch {
        Write-Host "❌ L'API n'est pas accessible" -ForegroundColor Red
        Write-Host "Assurez-vous que l'application est lancée:"
        Write-Host "  - Local: python app.py"
        Write-Host "  - Docker: docker-compose up -d"
    }
}

function Clean-Project {
    Write-Host "🧹 Nettoyage en cours..." -ForegroundColor Yellow
    
    Set-Location iris_project
    
    Write-Host "Suppression des fichiers temporaires..."
    
    Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Recurse -Filter "*.pyc" | Remove-Item -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Recurse -Filter "*.pyo" | Remove-Item -Force -ErrorAction SilentlyContinue
    Get-ChildItem -Path . -Recurse -Directory -Filter "*.egg-info" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    
    Write-Host "✅ Nettoyage terminé !" -ForegroundColor Green
    
    Set-Location ..
}

# Main
switch ($Action) {
    'local'  { Install-Local }
    'docker' { Deploy-Docker }
    'train'  { Train-Model }
    'test'   { Test-API }
    'clean'  { Clean-Project }
    'help'   { Show-Help }
    default  { Show-Help }
}
