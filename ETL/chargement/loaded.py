import os
import pandas as pd

# Dossiers source (transformed) et destination (final)
TRANSFORMED_DIR = r"C:\Users\Эли Жоэль\ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE\data\transformed"
FINAL_DIR = r"C:\Users\Эли Жоэль\ANALYSE_DE_PERFORMANCES_ET_OPTIMISATION_DE_SITE_E-COMMERCE\data\loaded"

# Création du dossier de sortie s'il n'existe pas
os.makedirs(FINAL_DIR, exist_ok=True)

def transformer_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    # Exemple supplémentaire de transformations
    data = data.fillna("N/A")
    data = data.loc[:, data.nunique() > 1]
    data.columns = [col.replace(" ", "_") for col in data.columns]
    return data

def traiter_fichiers():
    for filename in os.listdir(TRANSFORMED_DIR):
        filepath = os.path.join(TRANSFORMED_DIR, filename)

        if filename.endswith(".csv"):
            data = pd.read_csv(filepath)
        elif filename.endswith(".json"):
            data = pd.read_json(filepath, lines=True)
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            data = pd.read_excel(filepath)
        else:
            continue

        data_transformed = transformer_dataframe(data)
        output_path = os.path.join(FINAL_DIR, filename.replace(" ", "_"))
        data_transformed.to_csv(output_path if output_path.endswith(".csv") else output_path + ".csv", index=False)

if __name__ == "__main__":
    traiter_fichiers()