import pandas as pd
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Configuration MLflow : Nouvelle experience pour bien separer les resultats
mlflow.set_experiment("Iris_Simple_Baseline")

def train():
    with mlflow.start_run():
        # --- 1. Chargement des donnees ---
        csv_path = "iris_cleaned.csv"
        try:
            df = pd.read_csv(csv_path)
            print(f"Fichier charge : {csv_path}")
        except FileNotFoundError:
            print(f"Erreur : Le fichier {csv_path} est introuvable.")
            return

        # --- 2. Verification des colonnes ---
        if 'sepal_width' not in df.columns or 'sepal_length' not in df.columns:
            print("Erreur : Colonnes manquantes.")
            return

        # Definition des variables STRICTES (Sans espece)
        X = df[['sepal_width']]
        y = df['sepal_length']

        # --- 3. Modele ---
        # Pas de pipeline complexe ici, juste une regression simple
        model = LinearRegression()

        # --- 4. Entrainement ---
        # random_state=42 pour que la comparaison avec l'autre modele soit juste
        # (on utilise exactement les memes lignes de test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Entrainement de la Regression Lineaire (Simple) en cours...")
        model.fit(X_train, y_train)

        # --- 5. Evaluation ---
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print("--- RESULTATS BASELINE ---")
        print(f"MSE : {mse:.4f}")
        print(f"R2 Score : {r2:.4f}")

        # --- 6. Generation du Graphique ---
        plt.figure(figsize=(8, 6))
        
        # Nuage de points (Reel vs Predit)
        # En gris/noir pour montrer que c'est le modele "basique"
        plt.scatter(y_test, predictions, alpha=0.7, color='gray', label='Donnees de test')
        
        # Ligne de reference (Prediction parfaite)
        m, M = min(y_test), max(y_test)
        plt.plot([m, M], [m, M], color='red', linestyle='--', label='Prediction parfaite')
        
        plt.xlabel('Vraie Longueur (cm)')
        plt.ylabel('Longueur Predite (cm)')
        plt.title('Baseline : Largeur uniquement (Sans Espece)')
        plt.legend()
        
        # Nom de fichier different pour ne pas ecraser le bon graphique
        plot_filename = "prediction_plot_simple.png"
        plt.savefig(plot_filename)
        print(f"Graphique genere : {plot_filename}")

        # --- 7. Sauvegarde ---
        mlflow.log_param("model_type", "SimpleLinear_NoSpecies")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        mlflow.log_artifact(plot_filename)
        
        # On sauvegarde sous un nom different pour eviter la confusion
        mlflow.sklearn.log_model(model, "model_simple")
        # Pas de joblib.dump ici pour eviter d'ecraser le "bon" model.pkl destine a l'API
        print("Fin de l'execution baseline.")

if __name__ == "__main__":
    train()