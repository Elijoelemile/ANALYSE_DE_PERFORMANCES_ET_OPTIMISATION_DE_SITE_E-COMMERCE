import os
import pandas as pd

# Dossiers source (raw) et destination (transformed)
RAW_DIR = r"C:\Users\Эли Жоэль\ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE\data\raw"
TRANSFORMED_DIR = r"C:\Users\Эли Жоэль\ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE\data\transformed"

# Création du dossier de sortie s'il n'existe pas
os.makedirs(TRANSFORMED_DIR, exist_ok=True)

def transformer_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    """
    Exemple de fonction de transformation.
    Tu peux adapter avec tes vraies règles métier.
    """
    # 🔹 Exemple : suppression des colonnes vides
    data = data.dropna(axis=1, how="all")
    
    # 🔹 Exemple : suppression des doublons
    data = data.drop_duplicates()

    # 🔹 Exemple : mise en minuscules des noms de colonnes
    data.columns = [col.lower().strip() for col in data.columns]

    return data

def traiter_fichiers():
    # Parcours de chaque fichier dans le dossier RAW
    for filename in os.listdir(RAW_DIR):
        filepath = os.path.join(RAW_DIR, filename)

        # On ne traite que les CSV (mais tu peux étendre à JSON, XLSX, etc.)
        if filename.endswith(".csv"):
            print(f" Lecture : {filename}")
            data = pd.read_csv(filepath)

            # Transformation
            df_transformed = transformer_dataframe(data)

            # Sauvegarde dans TRANSFORMED_DIR
            output_path = os.path.join(TRANSFORMED_DIR, filename)
            df_transformed.to_csv(output_path, index=False)
            print(f"Fichier transformé et sauvegardé : {output_path}")

if __name__ == "__main__":
    traiter_fichiers()
