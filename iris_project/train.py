import pandas as pd
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import joblib

# Configuration MLflow
mlflow.set_experiment("Iris_LinearRegression_Species")

def train():
    with mlflow.start_run():
        # --- 1. Chargement des donnees ---
        csv_path = "iris_cleaned2.csv"
        try:
            df = pd.read_csv(csv_path)
            print(f"Fichier charge : {csv_path}")
        except FileNotFoundError:
            print(f"Erreur : Le fichier {csv_path} est introuvable.")
            return

        # --- 2. Verification des colonnes ---
        required_cols = ['sepal_width', 'sepal_length', 'species']
        if not all(col in df.columns for col in required_cols):
            print(f"Erreur : Colonnes manquantes. Requis : {required_cols}")
            return

        # Definition des variables
        X = df[['sepal_width', 'species']]
        y = df['sepal_length']

        # --- 3. Construction du Pipeline ---
        # Transformation de l'espece en chiffres (OneHotEncoder)
        preprocessor = make_column_transformer(
            (OneHotEncoder(handle_unknown='ignore'), ['species']),
            remainder='passthrough'
        )

        # Modele : Regression Lineaire (Simple et interpretable)
        model = make_pipeline(
            preprocessor, 
            LinearRegression()
        )

        # --- 4. Entrainement ---
        # random_state=42 pour garantir la reproductibilite
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Entrainement de la Regression Lineaire en cours...")
        model.fit(X_train, y_train)

        # --- 5. Evaluation ---
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print("--- RESULTATS ---")
        print(f"MSE : {mse:.4f}")
        print(f"R2 Score : {r2:.4f}")

        # --- 6. Generation du Graphique ---
        plt.figure(figsize=(8, 6))
        
        # Nuage de points (Reel vs Predit)
        plt.scatter(y_test, predictions, alpha=0.7, color='green', label='Donnees de test')
        
        # Ligne de reference (Idem que pour le Random Forest)
        m, M = min(y_test), max(y_test)
        plt.plot([m, M], [m, M], color='red', linestyle='--', label='Prediction parfaite')
        
        plt.xlabel('Vraie Longueur (cm)')
        plt.ylabel('Longueur Predite (cm)')
        plt.title(f'Regression Lineaire : Reel vs Predit\nR² = {r2:.4f}')
        plt.legend()
        
        plot_filename = "prediction_plot_linear.png"
        plt.savefig(plot_filename)
        print(f"Graphique genere : {plot_filename}")

        # --- 7. Sauvegarde ---
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        mlflow.log_artifact(plot_filename)
        
        mlflow.sklearn.log_model(model, "model")
        joblib.dump(model, "model.pkl")
        print("Modele sauvegarde sous model.pkl")

if __name__ == "__main__":
    train()