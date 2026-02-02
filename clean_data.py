
import pandas as pd

# 1. Lecture du fichier CSV original
df = pd.read_csv('iris.csv')

# 2. Création d'une version dupliquée pour travailler sans risquer de corrompre df_original
df_clean = df.copy()

# 3. Suppression des colonnes inutiles pour la consigne
columns_to_delete = ['petal_length', 'petal_width', 'species']  
df_clean.drop(columns=columns_to_delete, inplace=True)

# 4. Sauvegarde de la version nettoyée dans un nouveau fichier
df_clean.to_csv('iris_cleaned.csv', index=False)

print("Le fichier dupliqué 'iris_cleaned.csv' a été créé avec succès !")
print("Colonnes restantes :", df_clean.columns.tolist())