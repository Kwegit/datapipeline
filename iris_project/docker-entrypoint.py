#!/usr/bin/env python3
"""
Script d'initialisation du conteneur Docker
Vérifie si le modèle existe, sinon l'entraîne avant de lancer l'API
"""

import os
import subprocess
import sys

def main():
    print("🚀 Démarrage de l'application Iris ML...")
    
    # Vérifier si le modèle existe
    if not os.path.exists("model.pkl"):
        print("📦 Modèle non trouvé. Entraînement en cours...")
        try:
            subprocess.run([sys.executable, "train.py"], check=True)
            print("✅ Modèle entraîné avec succès !")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'entraînement : {e}")
            sys.exit(1)
    else:
        print("✅ Modèle trouvé. Pas besoin d'entraînement.")
    
    # Lancer l'application Flask
    print("🌐 Lancement de l'API Flask...")
    try:
        subprocess.run([sys.executable, "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Arrêt de l'application...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
