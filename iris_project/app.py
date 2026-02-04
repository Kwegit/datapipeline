from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import os

app = Flask(__name__, static_folder='website/src', static_url_path='')
CORS(app)  # Active CORS pour permettre les requêtes depuis le front-end

# 1. Chargement du Pipeline
try:
    model = joblib.load('model.pkl')
    print(" Pipeline chargé : Prêt pour les prédictions multi-espèces")
except Exception as e:
    print(f"Erreur : Impossible de charger model.pkl. {e}")
    model = None

@app.route('/')
def index():
    return send_from_directory('website/src', 'index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Modèle non disponible"}), 500

    try:
        # 2. Récupération de la largeur (ex: {"sepal_width": 3.5})
        data = request.get_json()
        width = float(data['sepal_width'])
        
        # 3. Liste des espèces connues dans le dataset Iris
        species_list = ['setosa', 'versicolor', 'virginica']
        results = {}

        # 4. Boucle pour prédire la longueur pour chaque espèce
        for sp in species_list:
            # On crée un DataFrame d'une ligne pour cette espèce précise
            input_df = pd.DataFrame([{
                'sepal_width': width,
                'species': sp
            }])
            
            # Prédiction
            prediction = model.predict(input_df)
            results[sp] = round(float(prediction[0]), 2)
        
        # 5. Retour du dictionnaire complet
        return jsonify({
            "input_sepal_width": width,
            "predictions_by_species": results,
            "unit": "cm",
            "status": "success"
        })

    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"}), 400

if __name__ == '__main__':
    # Récupérer le port depuis les variables d'environnement ou utiliser 5000 par défaut
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)