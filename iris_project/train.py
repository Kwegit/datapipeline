import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Configuration de l'expérience MLflow
mlflow.set_experiment("Iris_Sepal_Prediction")

def train():
    with mlflow.start_run():
        # --- A. Ingestion des données ---
        # On charge le fichier CSV nettoyé par vos camarades
        try:
            df = pd.read_csv("iris_cleaned.csv")
            print("Fichier 'iris_cleaned.csv' chargé.")
        except FileNotFoundError:
            print("Erreur : Le fichier 'iris_cleaned.csv' est introuvable.")
            return

        # --- B. Sélection des Features (X) et Target (y) ---
        # Consigne : Prédire la Longueur (y) à partir de la Largeur (X)
        
        # X = La variable explicative (Largeur). 
        # Note : On met des doubles crochets [[ ]] pour garder un format DataFrame (2D)
        try:
            X = df[["sepal_width"]] 
            y = df["sepal_length"]
        except KeyError as e:
            print(f"Erreur de colonne : {e}")
            print("Vérifiez l'orthographe dans le CSV. Colonnes vues :", df.columns.tolist())
            return

        # --- C. Split des données (Train / Test) ---
        # On garde 20% pour tester
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # --- D. Entraînement ---
        model = LinearRegression()
        model.fit(X_train, y_train)

        # --- E. Évaluation ---
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print(f"Modèle entraîné avec succès !")
        print(f"   MSE: {mse}")
        print(f"   R2: {r2}")

        # --- F. Logging MLflow & Sauvegarde ---
        mlflow.log_param("data_source", "iris_cleaned.csv")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        # Sauvegarde dans MLflow
        mlflow.sklearn.log_model(model, "model")
        
        # Sauvegarde locale pour l'API
        joblib.dump(model, "model.pkl")
        print("Fichier 'model.pkl' mis à jour pour l'API.")

if __name__ == "__main__":
    train()