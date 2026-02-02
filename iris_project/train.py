import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Configuration de l'expérience MLflow
# Cela crée un dossier "mlruns" localement pour stocker les résultats
mlflow.set_experiment("Iris_Sepal_Prediction")

def train():
    with mlflow.start_run():
        # --- A. Ingestion des données ---
        iris = load_iris()
        # Le dataset Iris a 4 colonnes : 
        # 0: Sepal Length, 1: Sepal Width, 2: Petal Length, 3: Petal Width
        
        # Consigne : Prédire Longueur (y) à partir de Largeur (X)
        X = iris.data[:, 1].reshape(-1, 1) # Colonne 1 : Sepal Width
        y = iris.data[:, 0]                # Colonne 0 : Sepal Length
        
        # --- B. Split des données ---
        # On garde 20% des données pour tester la qualité du modèle
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # --- C. Entraînement (Training) ---
        model = LinearRegression()
        model.fit(X_train, y_train)

        # --- D. Évaluation ---
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        print(f"Modèle entraîné !")
        print(f"MSE (Erreur moyenne au carré): {mse}")
        print(f"R2 Score: {r2}")

        # --- E. Logging avec MLflow (Traçabilité) ---
        # On enregistre les paramètres (ici aucun hyperparamètre complexe)
        mlflow.log_param("model_type", "LinearRegression")
        
        # On enregistre les metrics de performance
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2", r2)
        
        # On sauvegarde le modèle lui-même pour pouvoir le réutiliser plus tard
        mlflow.sklearn.log_model(model, "model")
        print("Modèle sauvegardé dans MLflow.")

if __name__ == "__main__":
    train()